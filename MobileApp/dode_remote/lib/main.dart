import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
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
                    onPressed: _play,
                    color: Colors.red
                ),
                SizedBox(height: 50),
                MaterialButton(
                    minWidth: 200,
                    height: 60,
                    child: Icon(
                      Icons.refresh,
                    ),
                    onPressed: _play,
                    color: Colors.yellow
                )
              ],
            )
          )
        )
      )
    );
  }


  _play(){
    print("Hola");
  }

}