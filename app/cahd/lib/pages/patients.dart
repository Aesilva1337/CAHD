import 'package:cahd/models/patient.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class Patients extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return _buildPatients();
  }

  Widget _buildPatients(){
    var cards = [
        _buildCard(Patient(nome: "Leonardo Oliveira de Freitas", data:DateTime.now().toString())),
        _buildCard(Patient(nome: "Arthue ELidio da Silva", data:DateTime.now().toString())),
        _buildCard(Patient(nome: "Matheus Donizete Batista", data:DateTime.now().toString()))
    ];
    return _buildListCard(cards);
  }

  SizedBox _buildCard(Patient patient) => SizedBox(
            height: 80,
            child: Card(
              color: Color.fromRGBO(149, 165, 166,1.0),
              child: ListTile(
                title: Text(patient.nome,
                    style: TextStyle(
                        fontWeight: FontWeight.w500,
                        color: Colors.white70)),
                subtitle: Text('Data: ${patient.data}'),
                leading: Icon(Icons.people),
              ),
            ),
          );

  Widget _buildListCard(List<Widget> lista) => Column(children: lista);
}
