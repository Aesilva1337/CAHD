import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/patient.dart';
import 'package:cahd/pages/patient.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class ListPatientsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: _buildPatients(context),
    );
  }

  Widget _buildPatients(BuildContext _) {
    var cards = [
      _buildCard(
          _,
          Patient(
              id: 1,
              nome: "Leonardo Oliveira de Freitas",
              data: DateTime.now().toString())),
      _buildCard(
          _,
          Patient(
              id: 2,
              nome: "Arthue ELidio da Silva",
              data: DateTime.now().toString())),
      _buildCard(
          _,
          Patient(
              id: 3,
              nome: "Matheus Donizete Batista",
              data: DateTime.now().toString()))
    ];
    return _buildListCard(cards);
  }

  SizedBox _buildCard(BuildContext _, Patient patient) => SizedBox(
        height: 80,
        child: Card(
          color: Color.fromRGBO(149, 165, 166, 1.0),
          child: ListTile(
            onTap: () => {
              Navigator.pushNamed(_, NavigationConstrants.PATIENT,
                  arguments: PatientPageArguments(patient.id))
            },
            title: Text(patient.nome,
                style: TextStyle(
                    fontWeight: FontWeight.w500, color: Colors.white70)),
            subtitle: Text('Data: ${patient.data}'),
            leading: Icon(Icons.people),
          ),
        ),
      );

  Widget _buildListCard(List<Widget> lista) => Column(children: lista);
}
