import 'dart:io';

import 'package:cahd/services/base.dart';
import 'package:cahd/services/classificacao-service.dart';
import 'package:cahd/services/diagnostico-service.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class PacienteService {
  Future<PacienteResponse> getListaEspera() async {
    var response =
        await http.get('${BaseService.BASE}/${BaseService.LISTA_ESPERA}');
    var ret = json.decode(response.body)['data'];
    var obj = PacienteResponse.fromJson(ret);
    return obj;
  }

  Future<PacienteResponse> getPaciente(cpf) async {
    var response =
        await http.get('${BaseService.BASE}/${BaseService.PACIENTE}/$cpf');
    var ret = json.decode(response.body)['data'];
    var obj = PacienteResponse.fromJson([ret]);
    return obj;
  }

  Future<List<FinalizarClassificacao>> getHistorico(cpf) async {
    var response = await http.get(
        '${BaseService.BASE}/${BaseService.CLASSIFICACAO_MANCHESTER}?cpf=$cpf');
    var ret = json.decode(response.body)['data'];
    if (ret == null) {
      return [];
    }
    List<FinalizarClassificacao> list = [];
    ret.forEach((e) => {list.add(FinalizarClassificacao.fromJson(e))});
    return list;
  }

  Future<bool> finalizar(FinalizarClassificacao finalizar) async {
    var dev = finalizar.toJson();
    var response = await http.post(
        '${BaseService.BASE}/${BaseService.CLASSIFICACAO_MANCHESTER}',
        headers: {"Content-Type": "application/json"},
        body: json.encode(finalizar.toJson()));
    var ret = json.decode(response.body);
    var obj = ret["data"] == null ? false : ret["data"]["valido"];
    return obj;
  }
}

class PacienteResponse {
  PacienteResponse({this.lista});

  factory PacienteResponse.fromJson(List<dynamic> json) {
    if (json != null) {
      var ret = new PacienteResponse(lista: []);
      json.forEach(
        (v) => ret.lista.add(Paciente.fromJson(v)),
      );
      return ret;
    }
    return null;
  }

  List<Paciente> lista;
}

class Paciente {
  Paciente(
      {this.id,
      this.name,
      this.cpf,
      this.enterDate,
      this.bornDate,
      this.sex,
      this.address,
      this.zipCode,
      this.telephone,
      this.city,
      this.motherName});
  factory Paciente.fromJson(dynamic json) {
    return Paciente(
      id: json["_id"]["\$oid"],
      cpf: json["cpf"],
      enterDate: json["enter_date"] != null ? json["enter_date"]["\$date"] : 0,
      name: json["name"],
      bornDate: json["born_date"] != null ? json["born_date"]["\$date"] : 0,
      sex: json["sex"],
      address: json["address"],
      zipCode: json["zip_code"],
      telephone: json["telephone"],
      city: json["city"],
      motherName: json["mother_name"],
    );
  }
  String id;
  String cpf;
  String name;
  num enterDate;
  num bornDate;
  String sex;
  String address;
  String zipCode;
  String telephone;
  String city;
  String motherName;
}

class FinalizarClassificacao {
  FinalizarClassificacao(
      {this.cpf,
      this.doctor,
      this.main_complaint,
      this.attendance_date,
      this.crm,
      this.manchester_classification,
      this.sympton});

  String cpf;
  String doctor;
  String main_complaint;
  String attendance_date;
  String crm;
  int manchester_classification;
  List<FinalizarClassificacaoSintoma> sympton;

  Map<String, dynamic> toJson() => {
        'cpf': cpf,
        'doctor': doctor,
        'main_complaint': main_complaint,
        'attendance_date': attendance_date,
        'crm': crm,
        'manchester_classification': manchester_classification.toString(),
        'sympton': getRes(sympton)
      };
  factory FinalizarClassificacao.fromJson(dynamic json) {
    return FinalizarClassificacao(
      manchester_classification: json["manchester_classification"],
      attendance_date: json["attendance_date"] != null
          ? json["attendance_date"]["\$date"].toString()
          : 0,
    );
  }
  getRes(List<FinalizarClassificacaoSintoma> symptons) {
    List jsonList = List();
    symptons.map((item) => jsonList.add(item.toJson())).toList();
    return jsonList;
  }
}

class FinalizarClassificacaoSintoma {
  FinalizarClassificacaoSintoma({this.sympton_name, this.value});
  String sympton_name;
  String value;

  Map<String, dynamic> toJson() => {
        'sympton_name': sympton_name,
        'value': value,
      };
}
