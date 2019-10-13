import 'dart:convert';

import 'package:cahd/services/base.dart';
import 'package:http/http.dart' as http;

class DiagnosticoService {
  Future<DiagnosticoResponse> getDiagnostico() async {
    var response =
        await http.get('${BaseService.BASE}/${BaseService.DIAGNOSTICO}');
    var ret = json.decode(response.body)['data'];
    var obj = DiagnosticoResponse.fromJson(ret);
    return obj;
  }
}

class DiagnosticoResponse {
  List<Diagnostico> lista;

  DiagnosticoResponse({this.lista});

  factory DiagnosticoResponse.fromJson(List<dynamic> json) {
    var ret = new DiagnosticoResponse(lista: []);
    json.forEach(
      (v) => ret.lista.add(Diagnostico.fromJson(v)),
    );
    return ret;
  }
}

class Diagnostico {
  static List<Sympton> listSympton(dynamic json) {
    var symptons = List<Sympton>();
    json.forEach((v) => {symptons.add(Sympton.fromJson(v))});
    return symptons;
  }

  factory Diagnostico.fromJson(Map<String, dynamic> json) {
    var ret = Diagnostico(
      id: json['_id']['\$oid'],
      name: json['diagnosis_name'],
      sympton: listSympton(json['sympton']),
      pathService: json['path_service'],
    );
    return ret;
  }
  Diagnostico({this.id, this.name, this.sympton, this.pathService});

  String id;
  String name;
  String pathService;
  List<Sympton> sympton;
}

class Sympton {
  factory Sympton.fromJson(Map<String, dynamic> json) {
    var name = json['sympton_name'];
    var max = json['max_value'] != null ? json['max_value'] : 0;
    var min = json['min_value'] != null ? json['min_value'] : 0;
    var property = json['property_name'];
    var type = json['type_input'];
    var value = json['value'] != null ? json['value'] : 0;

    var ret = Sympton(
      name: name,
      max: max,
      min: min,
      property: property,
      type: type,
      value: value,
    );

    return ret;
  }

  Sympton(
      {this.name, this.min, this.max, this.type, this.property, this.value});
  String name;
  int min;
  int max;
  int type;
  String property;
  int value;
}
