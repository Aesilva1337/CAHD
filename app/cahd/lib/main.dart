import 'package:cahd/constants/navigation.dart';
import 'package:cahd/routes/routes.dart';
import 'package:flutter/material.dart';
import 'package:intl/date_symbol_data_file.dart';
import 'package:intl/intl.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Intl.defaultLocale = 'pt_BR';
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Collect and Analysis of Health data',
      theme: ThemeData(
        brightness: Brightness.light,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: MaterialApp(
        debugShowCheckedModeBanner: false,
        onGenerateRoute: Routes.generateRoutes,
        initialRoute: NavigationConstrants.LOGIN,
      ),
    );
  }
}
