import 'dart:convert';

import 'package:cahd/services/base.dart';
import 'package:http/http.dart' as http;

class UserService {
  Future<bool> login(cpf, password) async {
    var request = Login(cpf: cpf, password: password);
    var response = await http.post('${BaseService.BASE}/${BaseService.LOGIN}',
        headers: {"Content-Type": "application/json"},
        body: json.encode(request.toJson()));
    var ret = json.decode(response.body);
    var obj = ret["data"];
    return response.statusCode == 200;
  }
}

class Login {
  Login({this.cpf, this.password});
  String cpf;
  String password;
  Map<String, dynamic> toJson() => {
        'cpf': cpf,
        'password': password,
      };
}
