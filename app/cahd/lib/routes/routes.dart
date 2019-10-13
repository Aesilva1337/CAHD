import 'package:cahd/constants/navigation.dart';
import 'package:cahd/pages/classificacao.dart';
import 'package:cahd/pages/home.dart';
import 'package:cahd/pages/list-patients.dart';
import 'package:cahd/pages/login.dart';
import 'package:cahd/pages/patient.dart';
import 'package:cahd/pages/triagem.dart';
import 'package:flutter/material.dart';

class Routes {
  static Route generateRoutes(RouteSettings settings) {
    switch (settings.name) {
      case NavigationConstrants.HOME:
        return buildRoute(settings, HomePage());
      case NavigationConstrants.LIST_PATIENTS:
        return buildRoute(settings, ListPatientsPage());
      case NavigationConstrants.PATIENT:
        return buildRoute(settings, PatientPage());
      case NavigationConstrants.CLASSIFIC:
        return buildRoute(settings, Classificacao());
      case NavigationConstrants.CLASSIFICT:
        return buildRoute(settings, ClassificacaoT());
      case NavigationConstrants.LOGIN:
        return buildRoute(settings, LoginPage());
      default:
        return buildRoute(settings, HomePage());
    }
  }

  static MaterialPageRoute buildRoute(RouteSettings settings, Widget builder) {
    return new MaterialPageRoute(
      settings: settings,
      builder: (BuildContext context) => builder,
    );
  }
}
