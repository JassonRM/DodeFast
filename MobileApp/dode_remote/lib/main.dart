import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:core';
import 'dart:io';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  List<dynamic> code = [];
  var playing = false;

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
                Text("DodeFast Remote", style: TextStyle(fontSize: 30),),
                SizedBox(height: 150,),
                MaterialButton(
                  minWidth: 200,
                  height: 60,
                  child: Icon(
                    Icons.play_arrow,
                  ),
                  onPressed: _play,
                  color: Colors.green
                ),
                SizedBox(height: 50),
                MaterialButton(
                    minWidth: 200,
                    height: 60,
                    child: Icon(
                      Icons.stop,
                    ),
                    onPressed: _stop,
                    color: Colors.red
                ),
                SizedBox(height: 50),
                MaterialButton(
                    minWidth: 200,
                    height: 60,
                    child: Icon(
                      Icons.refresh,
                    ),
                    onPressed: _reload,
                    color: Colors.yellow
                )
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
      playing = true;
      var counter = 0;
      while (playing && counter < code.length) {
        print(code[counter]);
        counter++;
        await new Future.delayed(Duration(seconds: 2));
      }
    }
  }

  _stop() async{
    playing = false;
    print("Stopping");
  }

  _reload() async {
    final response = await http.get("http://localhost:5000/code");
    String stringResponse = response.body.replaceAll("\\", "");
    String json = stringResponse.substring(1, stringResponse.length - 2);
    code = jsonDecode(json);
  }
}