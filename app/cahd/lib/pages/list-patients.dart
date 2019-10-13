import 'package:cahd/constants/navigation.dart';
import 'package:cahd/models/patient.dart';
import 'package:cahd/pages/patient.dart';
import 'package:cahd/services/pacientes-service.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:intl/date_symbol_data_local.dart';
import 'package:intl/intl.dart';

class ListPatientsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var api = new PacienteService();
    return FutureBuilder<PacienteResponse>(
      future: api.getListaEspera(),
      builder: (context, snapshot) {
        var listaPacientes = snapshot.data?.lista;
        return Scaffold(
          appBar: AppBar(
            title: Text("Fila para Triagem"),
          ),
          body: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: _buildPatients(context, listaPacientes),
            ),
          ),
        );
      },
    );
  }

  Widget _buildPatients(BuildContext _, List<Paciente> listaPacientes) {
    List<Widget> cards = [];
    if (listaPacientes == null) {
      return Text("Sem Pacientes");
    }
    initializeDateFormatting("pt_BR", null);
    listaPacientes.forEach(
      (e) => {
        cards.add(
          _buildCard(
            _,
            Patient(
              cpf: e.cpf,
              id: e.id,
              nome: e.name,
              data: DateFormat("dd/MM/yyyy hh:mm:ss")
                  .format(DateTime.fromMillisecondsSinceEpoch(e.enterDate))
                  .toString(),
            ),
          ),
        ),
      },
    );
    return _buildListCard(cards);
  }

  SizedBox _buildCard(BuildContext _, Patient patient) => SizedBox(
        height: 80,
        child: Card(
          color: Colors.blueAccent,
          child: ListTile(
            onTap: () => {
              Navigator.pushNamed(_, NavigationConstrants.PATIENT,
                  arguments: PatientPageArguments(patient.cpf))
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
