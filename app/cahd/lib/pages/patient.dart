import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/formulario.model.dart';
import 'package:cahd/pages/triagem.page.dart';
import 'package:flutter/material.dart';

class PatientPageArguments {
  final int idPatient;
  PatientPageArguments(this.idPatient);
}

class PatientPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final PatientPageArguments args = ModalRoute.of(context).settings.arguments;

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
                    title: Text("Arthur Elidio da Silva",
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
                  About(),
                  Center(
                    child: FlatButton(
                      child: Text("Iniciar Classificacao"),
                      color: Colors.blueAccent,
                      onPressed: () {
                        Navigator.pushNamed(
                            context, NavigationConstrants.CLASSIFIC);
                      },
                    ),
                  ),
                  Text("Teste"),
                  Text("Teste"),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

class About extends StatelessWidget {
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
    form.bairro = "Jardim Sonia";
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
            FieldForm(
              label: "Médico",
              text: form.medico,
            ),
            FieldForm(
              label: "CRM",
              text: form.crm,
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
