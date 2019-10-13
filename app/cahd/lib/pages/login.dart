import 'package:cahd/constants/navigation.dart';
import 'package:cahd/services/user-service.dart';
import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var api = UserService();
    var cpfControl = TextEditingController(text: "12558384694");
    var passControl = TextEditingController(text: "Stefanini@10");
    return Scaffold(
      body: Container(
        padding: EdgeInsets.only(top: 60, left: 40, right: 40),
        color: Colors.white,
        child: ListView(
          children: <Widget>[
            SizedBox(
              width: 128,
              height: 128,
              child: Image.asset("assets/images/medical.png"),
            ),
            SizedBox(
              height: 20,
            ),
            TextFormField(
              // autofocus: true,
              keyboardType: TextInputType.number,
              maxLength: 11,
              autofocus: true,
              decoration: InputDecoration(
                labelText: "CPF",
                labelStyle: TextStyle(
                  color: Colors.black38,
                  fontWeight: FontWeight.w400,
                  fontSize: 20,
                ),
              ),
              style: TextStyle(fontSize: 20),
              controller: cpfControl,
            ),
            SizedBox(
              height: 10,
            ),
            TextFormField(
              // autofocus: true,
              keyboardType: TextInputType.text,
              obscureText: true,
              decoration: InputDecoration(
                labelText: "Senha",
                labelStyle: TextStyle(
                  color: Colors.black38,
                  fontWeight: FontWeight.w400,
                  fontSize: 20,
                ),
              ),
              style: TextStyle(fontSize: 20),
              controller: passControl,
            ),
            SizedBox(
              height: 40,
            ),
            Container(
              height: 60,
              alignment: Alignment.centerLeft,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  stops: [0.3, 1],
                  colors: [
                    Colors.blueAccent,
                    Color(0XFFF92B7F),
                  ],
                ),
                borderRadius: BorderRadius.all(
                  Radius.circular(5),
                ),
              ),
              child: SizedBox.expand(
                child: FlatButton(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: <Widget>[
                      Text(
                        "Entrar",
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                          fontSize: 20,
                        ),
                        textAlign: TextAlign.left,
                      ),
                      Container(
                        child: SizedBox(
                          child: Icon(Icons.input),
                          height: 28,
                          width: 28,
                        ),
                      )
                    ],
                  ),
                  onPressed: () {
                    api.login(cpfControl.text, passControl.text).then((e) => {
                          if (!e)
                            {
                              showDialog(
                                context: context,
                                builder: (context) {
                                  return AlertDialog(
                                    // Retrieve the text the user has entered by using the
                                    // TextEditingController.
                                    content: Text("Cpf ou Senha Incorreto"),
                                  );
                                },
                              )
                            }
                          else
                            {
                              Navigator.popAndPushNamed(
                                  context, NavigationConstrants.HOME),
                            }
                        });

                    // Navigator.push(
                    //   context,
                    //   MaterialPageRoute(
                    //     builder: (context) => HomePage(),
                    //   ),
                    // );
                  },
                ),
              ),
            ),
            SizedBox(
              height: 10,
            ),
          ],
        ),
      ),
    );
  }
}
