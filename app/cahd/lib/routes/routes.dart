import 'package:cahd/constants/navigation.dart';
import 'package:cahd/pages/home.dart';
import 'package:cahd/pages/patients.dart';
import 'package:flutter/material.dart';

class Routes{
  

static Route generateRoutes(RouteSettings settings) {
  switch (settings.name) {
    case NavigationConstrants.HOME:
      return buildRoute(settings, Home());
    case NavigationConstrants.PATIENTS:
      return buildRoute(settings,Patients());
    default:
      return buildRoute(settings, Home());
  }
}

static MaterialPageRoute buildRoute(RouteSettings settings, Widget builder) {
  return new MaterialPageRoute(
    settings: settings,
    builder: (BuildContext context) => builder,
  );
}
}