import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/classificacao.model.dart';
import 'package:cahd/services/base.dart';
import 'package:cahd/services/classificacao-service.dart';
import 'package:cahd/services/diagnostico-service.dart';
import 'package:cahd/services/pacientes-service.dart';
import 'package:flutter/material.dart';

class ClassificacaoState extends State<Classificacao> {
  String pathService;
  Map<int, bool> checked = new Map();
  Map<int, bool> expd = new Map();
  Map<int, int> slider = new Map();
  Map<String, String> props = new Map();

  Color classificacao = Colors.blue;

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

  bool isCheked(int index) {
    var ret = checked[index] == null ? false : checked[index];
    return ret;
  }

  bool isExpand(int index) {
    var ret = expd[index] == null ? false : expd[index];
    return ret;
  }

  int getSlider(int index, {int min = 0}) {
    var ret = slider[index] == null ? min : slider[index];
    return ret;
  }

  bool isSlider(args, index) {
    return args[index].type == 1;
  }

  getClassificao() {
    new ClassificacaoService()
        .classificar(this.props, this.pathService)
        .then((e) => {
              setState(() {
                classificacao = e.manchester;
              })
            });
  }

  classificar(args, index, check) {
    if (!check) {
      setState(() {
        props[args[index].property] = null;
      });
    } else {
      setState(() {
        if (isSlider(args, index)) {
          props[args[index].property] = getSlider(index).toString();
        } else {
          props[args[index].property] = args[index].value.toString();
        }
      });
    }
    getClassificao();
  }

  @override
  Widget build(BuildContext context) {
    var manc = Manchester.getValues();
    var api = new PacienteService();
    TriagemArgs arguments = ModalRoute.of(context).settings.arguments;
    final List<Sympton> args = arguments.diagnosticos;
    setState(() {
      pathService = arguments.pathService;
    });

    return Scaffold(
      appBar: AppBar(
        title: Text("Triagem"),
      ),
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
                    color: this.classificacao,
                    child: RotatedBox(
                      quarterTurns: 1,
                      child: Container(
                        padding: EdgeInsets.all(2),
                        child: Center(
                          child: Text(
                            manc[this.classificacao].title,
                            textScaleFactor: 0.8,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
                Expanded(
                  child: SizedBox(
                    width: double.infinity,
                    height: 75,
                    child: Card(
                      color: this.classificacao,
                      child: Center(
                        child: Container(
                          padding: EdgeInsets.all(10),
                          child: Text(manc[this.classificacao].descricao),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
            ExpansionPanelList(
              children: List.generate(
                args.length,
                (index) {
                  return ExpansionPanel(
                    headerBuilder: (BuildContext context, bool isExpanded) {
                      return ListTile(
                        selected: isCheked(index),
                        title: Text(args[index].name),
                        onTap: () {
                          setState(() {
                            expd[index] = !isExpanded;
                          });
                        },
                        leading: Checkbox(
                          onChanged: (bool check) {
                            change();
                            setState(() {
                              checked[index] = check;
                              expd[index] = check;
                            });
                            classificar(args, index, check);
                          },
                          value: isCheked(index),
                        ),
                      );
                    },
                    body: isSlider(args, index)
                        ? Container(
                            child: Stack(
                              children: <Widget>[
                                Row(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceBetween,
                                  children: <Widget>[
                                    Container(
                                      width: 100,
                                      alignment: Alignment.center,
                                      child: Text('Escala:',
                                          style: Theme.of(context)
                                              .textTheme
                                              .headline),
                                    ),
                                    Flexible(
                                      flex: 1,
                                      child: Slider(
                                          label: "Values",
                                          activeColor: Colors.blueGrey,
                                          onChanged: (double change) {
                                            setState(() {
                                              slider[index] = change.round();
                                            });
                                            classificar(args, index, true);
                                          },
                                          value: getSlider(index,
                                                  min: args[index].min)
                                              .toDouble(),
                                          max: args[index].max.toDouble(),
                                          min: args[index].min.toDouble()),
                                    ),
                                    Container(
                                      width: 100,
                                      alignment: Alignment.center,
                                      child: Text('${getSlider(index)}',
                                          style: Theme.of(context)
                                              .textTheme
                                              .display1),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          )
                        : Text(""),
                    isExpanded: isSlider(args, index) &&
                        isCheked(index) &&
                        isExpand(index),
                  );
                },
              ),
            ),
            Container(
              height: 50,
              child: FlatButton(
                child: Text("Finalizar"),
                color: Colors.grey,
                onPressed: () {
                  if (props.length > 0) {
                    var finalizar = new FinalizarClassificacao(
                        attendance_date: DateTime.now().toString(),
                        cpf: arguments.paciente.cpf,
                        crm: "123",
                        doctor: "doctor",
                        main_complaint: "queixa",
                        manchester_classification:
                            ColorManchester.convertColorToClassification(
                                this.classificacao),
                        sympton: []);
                    for (var key in props.keys) {
                      finalizar.sympton.add(FinalizarClassificacaoSintoma(
                          sympton_name: key, value: props[key]));
                    }
                    api.finalizar(finalizar);
                    Navigator.popAndPushNamed(
                        context, NavigationConstrants.LIST_PATIENTS);
                  } else {
                    showDialog(
                      context: context,
                      builder: (context) {
                        return AlertDialog(
                          // Retrieve the text the user has entered by using the
                          // TextEditingController.
                          content: Text("Selecione um ou mais Sintoma(s)"),
                        );
                      },
                    );
                  }
                },
              ),
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

class TriagemArgs {
  TriagemArgs(
      {this.diagnosticos,
      this.typeClassificacao,
      this.paciente,
      this.pathService});
  List<Sympton> diagnosticos;
  ClassficacaoEnum typeClassificacao;
  Paciente paciente;
  String pathService;
}
