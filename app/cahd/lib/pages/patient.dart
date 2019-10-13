import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/formulario.model.dart';
import 'package:cahd/pages/classificacao.dart';
import 'package:cahd/pages/triagem.dart';
import 'package:cahd/services/pacientes-service.dart';
import 'package:flutter/material.dart';
import 'package:intl/date_symbol_data_file.dart';
import 'package:intl/intl.dart';

class PatientPageArguments {
  final String cpf;
  PatientPageArguments(this.cpf);
}

class PatientPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final PatientPageArguments args = ModalRoute.of(context).settings.arguments;
    var api = new PacienteService();
    return FutureBuilder<PacienteResponse>(
        future: api.getPaciente(args.cpf),
        builder: (context, snapshot) {
          if (snapshot.data == null) {
            return new Center(
              child: new CircularProgressIndicator(),
            );
          }
          var paciente = snapshot.data?.lista[0];

          return Scaffold(
            body: Container(
              child: DefaultTabController(
                length: 4,
                child: NestedScrollView(
                  headerSliverBuilder:
                      (BuildContext context, bool innerBoxIsScrolled) {
                    return <Widget>[
                      SliverAppBar(
                        expandedHeight: 200.0,
                        floating: false,
                        pinned: true,
                        flexibleSpace: FlexibleSpaceBar(
                          centerTitle: true,
                          title: Text(paciente.name,
                              style: TextStyle(
                                color: Colors.white,
                                fontSize: 16.0,
                              )),
                          background: person(),
                        ),
                      ),
                      SliverPersistentHeader(
                        delegate: _SliverAppBarDelegate(
                          TabBar(
                            labelColor: Colors.black87,
                            unselectedLabelColor: Colors.grey,
                            tabs: [
                              Tab(
                                icon: Icon(Icons.recent_actors),
                              ),
                              Tab(
                                icon: Icon(Icons.local_hospital),
                              ),
                              Tab(
                                icon: Icon(Icons.assignment_ind),
                              ),
                              Tab(
                                icon: Icon(Icons.history),
                              ),
                            ],
                          ),
                        ),
                        pinned: false,
                      ),
                    ];
                  },
                  body: Container(
                    child: TabBarView(
                      children: <Widget>[
                        About(paciente),
                        Center(
                          child: FlatButton(
                            child: Text("Iniciar Classificacao"),
                            color: Colors.blueAccent,
                            onPressed: () {
                              Navigator.popAndPushNamed(
                                context,
                                NavigationConstrants.CLASSIFICT,
                                arguments:
                                    ClassificacaoArgs(paciente: paciente),
                              );
                            },
                          ),
                        ),
                        Doctor(),
                        Container(
                          child: FutureBuilder<List<FinalizarClassificacao>>(
                            future: api.getHistorico(args.cpf),
                            builder: (context, snapshot) {
                              var hist = snapshot.data;

                              if (hist == null || hist.length == 0) {
                                return Center(
                                  child: Text("Sem Histórico"),
                                );
                              }
                              return Column(
                                children: List.generate(hist.length, (index) {
                                  return Center(
                                      child: Row(
                                    children: <Widget>[
                                      Container(
                                        padding: EdgeInsets.all(10),
                                        width: 150,
                                        child: Text(
                                            "Classificacao: ${hist[index].manchester_classification.toString()}"),
                                      ),
                                      Text(
                                          "Data: ${DateFormat("dd/MM/yyyy hh:mm:ss").format(DateTime.fromMillisecondsSinceEpoch(int.parse(hist[index].attendance_date))).toString()}")
                                    ],
                                  ));
                                }),
                              );
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          );
        });
  }
}

class About extends StatelessWidget {
  Paciente paciente;
  About(this.paciente);
  @override
  Widget build(BuildContext context) {
    final form = new FormularioModel();
    form.nome = paciente.name;
    form.dataNasc = paciente.bornDate.toString();
    form.endereco = "";
    form.cep = "";
    form.municipio = "";
    form.bairro = "";
    form.nomeMae = paciente.motherName;
    form.telefone = paciente.telephone;
    form.idade = 21;
    form.sexo = paciente.sex;
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Container(
              padding: EdgeInsets.only(bottom: 10, top: 10),
              child: Center(
                child: Text(
                  "Informações Paciente",
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
            ),
            FieldForm(
              label: "Nome Paciente",
              text: form.nome,
            ),
            FieldForm(
              label: "Data Nascimento",
              text: form.dataNasc,
            ),
            FieldForm(
              label: "Sexo",
              text: form.sexo,
            ),
            FieldForm(
              label: "Idade",
              text: "${form.idade}",
            ),
            FieldForm(
              label: "Bairro",
              text: form.bairro,
            ),
            FieldForm(
              label: "CEP",
              text: form.cep,
            ),
            FieldForm(
              label: "Municipio",
              text: form.municipio,
            ),
            FieldForm(
              label: "Telefone",
              text: form.telefone,
            ),
            FieldForm(
              label: "Nome Mãe",
              text: form.nomeMae,
            ),
          ],
        ),
      ),
    );
  }
}

class Doctor extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Container(
              padding: EdgeInsets.only(bottom: 10, top: 10),
              child: Center(
                child: Text(
                  "Informações Médico",
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
            ),
            FieldForm(
              label: "Nome Médico",
              text: "Aline Stivanin",
            ),
            FieldForm(
              label: "CRM",
              text: "1889974",
            ),
          ],
        ),
      ),
    );
  }
}

class TabBarDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final form = new FormularioModel();
    form.nome = "Arthur Elidio da Silva";
    form.dataNasc = "04/05/1997";
    form.endereco = "Rua RIo Gande do Sul";
    form.cep = "13911170";
    form.municipio = "Jaguariuna";
    form.nomeMae = "Alaine Cristina Marcfelino da Silva";
    form.telefone = "99999999";
    form.crm = "188974";
    form.medico = "Aline Stivanin Texeira";
    form.idade = 21;
    form.sexo = "M";
    return Scaffold(
      backgroundColor: Color(0xFFF5F5F5),
      body: Column(
        children: <Widget>[],
      ),
    );
  }
}

person() {
  return Container(
    color: Colors.blueAccent,
    height: 150,
    width: double.infinity,
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Container(
          height: 70,
          child: CircleAvatar(
            child: Icon(
              Icons.person,
              size: 40,
            ),
            radius: 100,
          ),
        ),
      ],
    ),
  );
}

class ActionButton extends StatelessWidget {
  final IconData icon;

  final String text;

  ActionButton({this.icon, this.text});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        color: Color(0xFFF5F5F5),
        child: FlatButton(
          onPressed: () {},
          child: Column(
            children: <Widget>[
              Icon(icon),
              Text(
                text,
                style: TextStyle(fontSize: 12),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class FieldForm extends StatelessWidget {
  final String label;
  final String text;

  FieldForm({this.label, this.text});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          label,
          style: TextStyle(
            color: Colors.blueAccent,
            fontWeight: FontWeight.w500,
          ),
        ),
        Container(
          padding: EdgeInsets.only(left: 10),
          child: Text(
            text != null ? text : "",
            style: TextStyle(
              fontWeight: FontWeight.w400,
            ),
          ),
        ),
        Divider()
      ],
    );
  }
}

class _SliverAppBarDelegate extends SliverPersistentHeaderDelegate {
  _SliverAppBarDelegate(this._tabBar);

  final TabBar _tabBar;

  @override
  double get minExtent => _tabBar.preferredSize.height;
  @override
  double get maxExtent => _tabBar.preferredSize.height;

  @override
  Widget build(
      BuildContext context, double shrinkOffset, bool overlapsContent) {
    return new Container(
      child: _tabBar,
    );
  }

  @override
  bool shouldRebuild(_SliverAppBarDelegate oldDelegate) {
    return false;
  }
}

class Historico extends StatefulWidget {
  @override
  ClassificacaoState createState() => ClassificacaoState();
}
