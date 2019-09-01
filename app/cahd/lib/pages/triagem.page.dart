import 'package:cahd/models/classificacao.model.dart';
import 'package:flutter/material.dart';

class ClassificacaoState extends State<Classificacao> {
  bool checked = false;
  bool expd = false;
  double slider = 0.0;
  int mans = int.parse("0");

  change() {
    var value = mans;
    if (value > 3) {
      value--;
    } else {
      value++;
    }
    setState(() {
      mans = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    var manc = Manchester.getValues();

    return Scaffold(
      appBar: AppBar(),
      body: Container(
        child: ListView(
          children: <Widget>[
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                SizedBox(
                  width: 50,
                  height: 75,
                  child: Card(
                    color: manc[mans].color,
                    child: RotatedBox(
                        quarterTurns: 1,
                        child: Container(
                          padding: EdgeInsets.all(2),
                          child: Center(
                            child: Text(
                              manc[mans].title,
                              textScaleFactor: 0.8,
                            ),
                          ),
                        )),
                  ),
                ),
                Expanded(
                  child: SizedBox(
                    width: double.infinity,
                    height: 75,
                    child: Card(
                      color: manc[mans].color,
                      child: Center(
                        child: Container(
                          padding: EdgeInsets.all(10),
                          child: Text(manc[mans].descricao),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
            ExpansionPanelList(
              expansionCallback: (int index, bool isExpanded) {
                setState(() {});
              },
              children: [
                ExpansionPanel(
                  headerBuilder: (BuildContext context, bool isExpanded) {
                    return ListTile(
                      selected: checked,
                      title: Text("Sudorese (hipoglicemia)"),
                      onTap: () {
                        setState(() {
                          expd = !isExpanded;
                        });
                      },
                      leading: Checkbox(
                        onChanged: (bool check) {
                          change();
                          setState(() {
                            checked = check;
                            expd = check;
                          });
                        },
                        value: checked,
                      ),
                    );
                  },
                  body: Container(
                      child: Stack(
                    children: <Widget>[
                      Text("P"),
                      Slider(
                        label: "Values",
                        activeColor: Colors.blueGrey,
                        onChanged: (double change) {
                          setState(() {
                            slider = change;
                          });
                        },
                        value: slider,
                        max: 100,
                      ),
                    ],
                  )),
                  isExpanded: checked && expd,
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}

class Classificacao extends StatefulWidget {
  @override
  ClassificacaoState createState() => ClassificacaoState();
}
