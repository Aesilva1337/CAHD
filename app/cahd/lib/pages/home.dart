import 'package:cahd/constants/navigation.dart';
import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: LayoutBuilder(
        builder: (BuildContext context, BoxConstraints viewportConstraints) {
          return SingleChildScrollView(
            child: ConstrainedBox(
              constraints: BoxConstraints(
                minHeight: viewportConstraints.maxHeight,
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                mainAxisAlignment: MainAxisAlignment.start,
                children: <Widget>[
                  _buildCard(
                      context,
                      'Diagnostico',
                      'Processo de Triagem',
                      'assets/images/medical.png',
                      NavigationConstrants.LIST_PATIENTS),
                  _buildCard(
                      context,
                      'Paciente',
                      'Adicionar Paciente',
                      'assets/images/medical.png',
                      NavigationConstrants.REGISTRY_PATIENT),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildCard(BuildContext context, String title, String subTitle,
          String urlImg, String route) =>
      SizedBox(
        child: Card(
          color: Color.fromRGBO(87, 202, 195, 1.0),
          child: ListTile(
            onTap: () => {Navigator.pushNamed(context, route)},
            title: Text(title,
                style: TextStyle(
                    fontWeight: FontWeight.w500, color: Colors.white70)),
            subtitle: Text(subTitle),
            leading: Image.asset(
              urlImg,
              color: Colors.black,
            ),
          ),
        ),
      );
}
