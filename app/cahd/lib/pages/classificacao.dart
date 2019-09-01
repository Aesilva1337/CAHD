import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/classificacao.model.dart';
import 'package:flutter/material.dart';

class ClassificacaoT extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var values = ClassificacaoModelMock.getValues();
    return Scaffold(
      appBar: AppBar(),
      backgroundColor: Color(0xFFF5F5F5),
      body: LayoutBuilder(
        builder: (BuildContext context, BoxConstraints viewportConstraints) {
          return SingleChildScrollView(
            child: ConstrainedBox(
              constraints: BoxConstraints(
                minHeight: viewportConstraints.maxHeight,
              ),
              child: Center(
                child: Column(
                  children: List.generate(6, (index) {
                    var nome = values[index].descricao;
                    return Card(
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: <Widget>[
                          ListTile(
                            leading: Icon(Icons.select_all),
                            title: Text(nome),
                            subtitle: Text('subtitle'),
                          ),
                          ButtonTheme.bar(
                            // make buttons use the appropriate styles for cards
                            child: ButtonBar(
                              children: <Widget>[
                                FlatButton(
                                  child: const Text('Selecionar'),
                                  onPressed: () {
                                    Navigator.pushNamed(context,
                                        NavigationConstrants.CLASSIFIC);
                                  },
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    );
                  }),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
