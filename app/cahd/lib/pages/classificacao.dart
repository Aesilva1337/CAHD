import 'package:cahd/constants/navigation.dart';
import 'package:cahd/pages/triagem.dart';
import 'package:cahd/services/diagnostico-service.dart';
import 'package:cahd/services/pacientes-service.dart';
import 'package:flutter/material.dart';

class ClassificacaoT extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    ClassificacaoArgs args = ModalRoute.of(context).settings.arguments;

    var api = new DiagnosticoService();
    return FutureBuilder<DiagnosticoResponse>(
      future: api.getDiagnostico(),
      builder: (context, snapshot) {
        var diagnosticos = snapshot.data?.lista;

        return Scaffold(
          appBar: AppBar(
            title: Text("Triagem"),
          ),
          backgroundColor: Color(0xFFF5F5F5),
          body: LayoutBuilder(
            builder:
                (BuildContext context, BoxConstraints viewportConstraints) {
              return SingleChildScrollView(
                child: ConstrainedBox(
                  constraints: BoxConstraints(
                    minHeight: viewportConstraints.maxHeight,
                  ),
                  child: Center(
                    child: Column(
                      children: diagnosticos == null
                          ? []
                          : List.generate(
                              diagnosticos.length,
                              (index) {
                                var nome = diagnosticos[index].name;
                                return Card(
                                  child: Column(
                                    mainAxisSize: MainAxisSize.min,
                                    children: <Widget>[
                                      ListTile(
                                        leading: Icon(
                                          Icons.select_all,
                                          color: Colors.greenAccent,
                                        ),
                                        trailing: Icon(Icons.arrow_forward),
                                        title: Text(
                                          nome,
                                          style: TextStyle(
                                              fontWeight: FontWeight.w400),
                                        ),
                                        onTap: () => {
                                          Navigator.popAndPushNamed(
                                            context,
                                            NavigationConstrants.CLASSIFIC,
                                            arguments: TriagemArgs(
                                                diagnosticos:
                                                    diagnosticos[index].sympton,
                                                pathService: diagnosticos[index]
                                                    .pathService,
                                                paciente: args.paciente),
                                          ),
                                        },
                                        //subtitle: Text('subtitle'),
                                      ),
                                      // ButtonTheme.bar(
                                      //   // make buttons use the appropriate styles for cards
                                      //   child: ButtonBar(
                                      //     children: <Widget>[
                                      //       FlatButton(
                                      //         child: const Text('Selecionar'),
                                      //         onPressed: () {
                                      //           Navigator.pushNamed(context,
                                      //               NavigationConstrants.CLASSIFIC);
                                      //         },
                                      //       ),
                                      //     ],
                                      //   ),
                                      // ),
                                    ],
                                  ),
                                );
                              },
                            ),
                    ),
                  ),
                ),
              );
            },
          ),
        );
      },
    );
  }
}

class ClassificacaoArgs {
  ClassificacaoArgs({this.paciente});
  Paciente paciente;
}
