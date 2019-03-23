import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:core';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';

void main(){
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown
  ]);
  runApp(MyApp());
}

class MyApp extends StatefulWidget{
  @override
  _MyAppState createState() => new _MyAppState();
}

class _MyAppState extends State<MyApp> {

  List<dynamic> code = [];
  bool _playing = false;
  int _counter = 0;
  var _ipAddress = "";


  FlutterBluetoothSerial bluetooth = FlutterBluetoothSerial.instance;
  List<BluetoothDevice> _devices = [];
  BluetoothDevice _device;
  bool _connected = false;

  @override
  void initState() {
    super.initState();
    initPlatformState();
  }

  Future<void> initPlatformState() async {
    List<BluetoothDevice> devices = [];

    try {
      devices = await bluetooth.getBondedDevices();
    } on PlatformException {
      // TODO - Error
    }

    bluetooth.onStateChanged().listen((state) {
      switch (state) {
        case FlutterBluetoothSerial.CONNECTED:
          setState(() {
            _connected = true;
          });
          break;
        case FlutterBluetoothSerial.DISCONNECTED:
          setState(() {
            _connected = false;
          });
          break;
        default:
        // TODO
          break;
      }
    });

    if (!mounted) return;
    setState(() {
      _devices = devices;
    });

  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DodeFast Remote',
      home: Scaffold(
        appBar: null,
        body: Padding(
          padding: EdgeInsets.all(50),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Expanded(
                  child: SizedBox(),
                  flex: 2,
                ),
                Text("DodeFast Remote", style: TextStyle(fontSize: 30),),
                Expanded(
                  child: SizedBox(),
                  flex: 2,
                ),
                MaterialButton(
                  minWidth: 200,
                  height: 60,
                  child: _playing ? Icon(
                    Icons.pause,
                  ) : Icon(
                    Icons.play_arrow,
                  ),
                  onPressed: _playing ? _pause : _play,
                  color: Colors.green
                ),
                Expanded(
                    child: SizedBox(),
                    flex: 1,
                ),
                MaterialButton(
                    minWidth: 200,
                    height: 60,
                    child: Icon(
                      Icons.stop,
                    ),
                    onPressed: _stop,
                    color: Colors.red
                ),
                Expanded(
                  child: SizedBox(),
                  flex: 1,
                ),
                MaterialButton(
                    minWidth: 200,
                    height: 60,
                    child: Icon(
                      Icons.refresh,
                    ),
                    onPressed: _reload,
                    color: Colors.yellow
                ),
                Expanded(
                  child: SizedBox(),
                  flex: 1,
                ),
                Container(
                  width: 200,
                  child: TextField(
                    onChanged: (text) {
                      _ipAddress = text;
                    },
                    textAlign: TextAlign.center,
                    decoration: InputDecoration(
                      hintText: "IP Address"
                    ),
                    keyboardType: TextInputType.numberWithOptions(decimal: true),
                  )
                ),
                Expanded(
                  child: SizedBox(),
                  flex: 2,
                ),
              ],
            )
          )
        )
      )
    );
  }


  _play() async{
    if (code.isEmpty) {
      print("No hay codigo");
    } else {
      setState(() {
        _playing = true;
      });
      while (_playing && _counter < code.length) {
        _sendDode(code[_counter]);
        setState(() {
          _counter++;
        });
        await new Future.delayed(Duration(seconds: 2));
      }
      if(_counter == code.length) {
        _stop();
      }
    }
  }

  _pause(){
    setState(() {
      _playing = false;
    });
  }

  _stop() async{
    setState(() {
      _playing = false;
      _counter = 0;
    });
  }

  _reload() async {
    //Connects bluetooth
    _devices.forEach((device) {
      if(device.name == "HC-06"){
        _device = device;
      }
    });
    _connect();

    _stop();
    //Connects server
    try {
      var server = "http://" + _ipAddress + ":5000/code";
      final response = await http.get(server);
      String stringResponse = response.body.replaceAll("\\", "");
      String json = stringResponse.substring(1, stringResponse.length - 2);
      code = jsonDecode(json);
    } on Exception {
      print("No conection with the server");
    }
  }

  void _connect() {
    bluetooth.isConnected.then((isConnected) {
      if (!isConnected) {
        bluetooth.connect(_device).catchError((error) {});
      }
    });
  }

  void _sendDode(String command) {
    bluetooth.isConnected.then((isConnected) {
      if (isConnected) {
        bluetooth.write(command);
      }
    });
  }
}