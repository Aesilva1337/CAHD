import 'package:cahd/constants/navigation.dart';
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return _buildCard(context);
  }

  Widget _buildCard(BuildContext context) => Column(
        children: <Widget>[
          SizedBox(
            height: 80,
            child: Card(
              color: Color.fromRGBO(87, 202, 195, 1.0),
              child: ListTile(
                onTap: ()=>{
                  Navigator.pushNamed(context, NavigationConstrants.PATIENTS)
                },
                title: Text('Diagnostico',
                    style: TextStyle(
                        fontWeight: FontWeight.w500,
                        color: Colors.white70)),
                subtitle: Text('Processo de Triagem'),
                leading: Image.asset(
                  "assets/images/medical.png",
                  color: Colors.black,
                ),
              ),
            ),
          )
        ],
      );
}
