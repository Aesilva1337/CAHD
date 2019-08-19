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
                children: <Widget>[_buildCard(context)],
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildCard(BuildContext context) => SizedBox(
        child: Card(
          color: Color.fromRGBO(87, 202, 195, 1.0),
          child: ListTile(
            onTap: () => {
              Navigator.pushNamed(context, NavigationConstrants.LIST_PATIENTS)
            },
            title: Text('Diagnostico',
                style: TextStyle(
                    fontWeight: FontWeight.w500, color: Colors.white70)),
            subtitle: Text('Processo de Triagem'),
            leading: Image.asset(
              "assets/images/medical.png",
              color: Colors.black,
            ),
          ),
        ),
      );
}
