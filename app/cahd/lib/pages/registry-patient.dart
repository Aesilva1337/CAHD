import 'package:cahd/services/pacientes-service.dart';
import 'package:flutter/material.dart';

class RegistryPatientPage extends StatefulWidget {
  @override
  RegistryPatientPageState createState() => RegistryPatientPageState();
}

class RegistryPatientPageState extends State<RegistryPatientPage> {
  String select = '1';
  Paciente paciente;
  var pacienteService = PacienteService();

  var ctrl_cpf = TextEditingController();
  var ctrl_name = TextEditingController();
  var ctrl_nome_mae = TextEditingController();
  var ctrl_data_nascimento = TextEditingController();
  var ctrl_sexo = TextEditingController();
  var ctrl_endereco = TextEditingController();
  var ctrl_cep = TextEditingController();
  var ctrl_cidade = TextEditingController();
  var ctrl_telefone = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Cadastrar Paciente"),
      ),
      body: Container(
        padding: EdgeInsets.only(top: 60, left: 40, right: 40),
        color: Colors.white,
        child: ListView(
          children: getFields(),
        ),
      ),
    );
  }

  List<Widget> getFields() {
    var fields = List<Widget>();
    fields.add(_fieldCPF());
    if (this.paciente == null) {
      fields.add(_fieldName());
      fields.add(_fieldNomeMae());
      fields.add(_fieldDataNascimento());
      fields.add(_fieldSexo());
      fields.add(_fieldEndereco());
      fields.add(_fieldCep());
      fields.add(_fieldCidade());
      fields.add(_fieldTelefone());
    }
    fields.add(SizedBox(
      height: 10,
    ));

    fields.add(_buttonSalvar());
    return fields;
  }

  Widget _fieldCPF() {
    Paciente res;
    return TextField(
      onChanged: (value) => {
        this.pacienteService.getPacienteByCpf(ctrl_cpf.text).then((em) => {
              setState(() {
                paciente = em;
              }),
            }),
      },
      // autofocus: true,
      keyboardType: TextInputType.number,
      maxLength: 11,
      autofocus: false,
      controller: ctrl_cpf,
      decoration: InputDecoration(
        labelText: "CPF",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldName() {
    return TextFormField(
      controller: ctrl_name,
      // autofocus: true,
      keyboardType: TextInputType.text,
      maxLength: 50,
      decoration: InputDecoration(
        labelText: "Nome",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldDataNascimento() {
    return TextFormField(
      controller: ctrl_data_nascimento,
      keyboardType: TextInputType.datetime,
      maxLength: 8,
      decoration: InputDecoration(
        labelText: "Data Nascimento",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  DropdownButton _fieldSexo() => DropdownButton<String>(
        hint: Text(
          "Sexo",
        ),
        isExpanded: true,
        items: [
          DropdownMenuItem(
            value: "1",
            child: Text(
              "M",
            ),
          ),
          DropdownMenuItem(
            value: "2",
            child: Text(
              "F",
            ),
          ),
        ],
        onChanged: (value) {
          setState(() {
            select = value;
          });
        },
        value: this.select,
      );
  Widget _fieldEndereco() {
    return TextFormField(
      controller: ctrl_endereco,
      keyboardType: TextInputType.text,
      maxLength: 50,
      decoration: InputDecoration(
        labelText: "Endereco",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldCep() {
    return TextFormField(
      controller: ctrl_cep,
      keyboardType: TextInputType.text,
      maxLength: 15,
      decoration: InputDecoration(
        labelText: "Cep",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldTelefone() {
    return TextFormField(
      controller: ctrl_telefone,
      keyboardType: TextInputType.number,
      maxLength: 12,
      decoration: InputDecoration(
        labelText: "Telefone",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldCidade() {
    return TextFormField(
      controller: ctrl_cidade,
      keyboardType: TextInputType.text,
      maxLength: 50,
      decoration: InputDecoration(
        labelText: "Cidade",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  Widget _fieldNomeMae() {
    return TextFormField(
      controller: ctrl_nome_mae,
      keyboardType: TextInputType.text,
      maxLength: 50,
      decoration: InputDecoration(
        labelText: "Nome Mae",
        labelStyle: TextStyle(
          color: Colors.black38,
          fontWeight: FontWeight.w400,
          fontSize: 20,
        ),
      ),
      style: TextStyle(fontSize: 20),
    );
  }

  _buttonSalvar() {
    return Container(
      width: double.infinity,
      color: Colors.blue,
      child: FlatButton(
        onPressed: () {
          if (paciente == null) {
            this
                .pacienteService
                .salvar(
                  new Paciente(
                      cpf: this.ctrl_cpf.text,
                      address: ctrl_endereco.text,
                      bornDate: DateTime.now().millisecondsSinceEpoch,
                      city: ctrl_cidade.text,
                      motherName: ctrl_nome_mae.text,
                      telephone: ctrl_telefone.text,
                      name: ctrl_name.text,
                      sex: select == "1" ? 'M' : 'F',
                      zipCode: ctrl_cep.text),
                )
                .then((e) => {
                      showDialog(
                        context: context,
                        builder: (context) {
                          return AlertDialog(
                            title: Text('Informação'),
                            content: Text("Paciente Cadastrado"),
                          );
                        },
                      )
                    });
          }
          pacienteService.postListaEspera(ctrl_cpf.text).then((e) => {
                showDialog(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      actions: <Widget>[
                        FlatButton(
                          onPressed: () => {Navigator.pop(context)},
                          child: Text('OK'),
                        )
                      ],
                      title: Text('Informação'),
                      content: Text("Paciente Adicionado na Lista de Espera"),
                    );
                  },
                )
              });
        },
        child: Text(
          paciente == null
              ? 'Cadastrar e Adicionar na Lista de Espera'
              : 'Adicionar na lista de Espera',
          style: TextStyle(fontSize: 16),
        ),
      ),
    );
  }
}
