import 'dart:convert';

import 'package:cahd/services/base.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart' as http;

class ClassificacaoService {
  Future<dynamic> classificar(Map<String, String> props, classificacao) async {
    var response = await http.get(
        '${BaseService.BASE}/$classificacao${BaseService.formatQuery(props)}');
    var ret = json.decode(response.body);
    var obj = ClassificacaoService.fromJson(ret);
    return obj;
  }

  factory ClassificacaoService.fromJson(Map<String, dynamic> json) {
    var ret = ClassificacaoService(
      manchester: ColorManchester.convert(json['data']),
    );
    return ret;
  }
  ClassificacaoService({this.manchester});

  Color manchester;
}

class ColorManchester {
  static const String AZUL = "AZUL";
  static const String VERDE = "VERDE";
  static const String AMARELO = "AMARELO";
  static const String LARANJA = "LARANJA";
  static const String VERMELHO = "VERMELHO";

  static Color convert(manchester) {
    switch (manchester.toUpperCase()) {
      case AZUL:
        return Colors.blue;
      case VERDE:
        return Colors.green;
      case AMARELO:
        return Colors.yellow;
      case LARANJA:
        return Colors.orange;
      case VERMELHO:
        return Colors.red;
      default:
        return Colors.blue;
    }
  }

  static int convertColorToClassification(Color color) {
    if (color == Colors.blue)
      return 1;
    else if (color == Colors.green)
      return 2;
    else if (color == Colors.yellow)
      return 3;
    else if (color == Colors.orange)
      return 4;
    else if (color == Colors.red)
      return 5;
    else
      return 1;
  }
}
