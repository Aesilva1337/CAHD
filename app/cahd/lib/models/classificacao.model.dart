import 'package:cahd/services/base.dart';
import 'package:cahd/services/classificacao-service.dart';
import 'package:flutter/material.dart';

class ClassificacaoModel {
  ClassificacaoModel(this.descricao, [this.value]);
  String descricao;
  List<SintomasModel> value;
}

class SintomasModel {
  SintomasModel(
    this.descricao,
    this.type,
  );
  String descricao;
  TypeValueSintoma type;
  bool min;
  bool max;
}

class Manchester {
  Manchester(this.color, this.descricao, this.title);
  Color color;
  String title;
  String descricao;

  static Map<Color, Manchester> getValues() {
    return {
      Colors.red: Manchester(
          Colors.red,
          "Emergência: Caso gravìssimo, com necessidade de atendimento imediato e risco de morte.",
          "Emergência"),
      Colors.orange: Manchester(
          Colors.orange,
          "Muito Urgente: Caso grave e risco sifnificativo de evoluir para morte. Atendimento urgente.",
          "Muito Urgente"),
      Colors.yellow: Manchester(
          Colors.yellow,
          "Urgente: Caso de gravidade moderada, necessidade de atendimento médico, sem risco imediato.",
          "Urgente"),
      Colors.green: Manchester(
          Colors.green,
          "Pouco Urgente: Caso para atendimento preferencial nas unidades de atenção básica.",
          "Pouco Urgente"),
      Colors.blue: Manchester(
          Colors.blueAccent,
          "Não Urgente: Caso para atendimento na unidade de saúde mais próxima da residência. Atendimento de acordo com o horário de chegada ou serão direcionadas às Estratégias de Saúde da Família ou Unidades Básicas de Saúde. Queixas crônicas; resfriados; contusões; escoriações; dor de garganta; ferimentos que não requerem fechamento e outros.",
          "Não Urgente"),
    };
  }
}

enum TypeValueSintoma { RANGE, CHECK, SELECT }

class ClassificacaoModelMock {
  static List<ClassificacaoModel> getValues() {
    return [
      ClassificacaoModel(
        "Vomito e Diarreia",
        [
          SintomasModel("Com desidratacao", TypeValueSintoma.CHECK),
          SintomasModel("Persistentes", TypeValueSintoma.CHECK),
          SintomasModel("Letargia", TypeValueSintoma.CHECK),
          SintomasModel("Mucosas ressecadas", TypeValueSintoma.CHECK),
          SintomasModel("Turgor pastoso", TypeValueSintoma.CHECK),
          SintomasModel("Dados vitais", TypeValueSintoma.SELECT),
          SintomasModel("Mucosas úmidas", TypeValueSintoma.CHECK),
          SintomasModel("Diurese normal", TypeValueSintoma.CHECK),
          SintomasModel("Turgor de pele normal", TypeValueSintoma.CHECK),
          SintomasModel("< 5 - 10 evacuações / dia", TypeValueSintoma.CHECK),
          SintomasModel("< 5 - 10 vômitos / dia", TypeValueSintoma.CHECK),
        ],
      ),
      ClassificacaoModel(
        "Diabetes",
        [
          SintomasModel("Sudorose (hipoglicemia)", TypeValueSintoma.CHECK),
          SintomasModel(
              "Alteração mental (hipo-hiperglicemia)", TypeValueSintoma.CHECK),
          SintomasModel("Febre", TypeValueSintoma.CHECK),
          SintomasModel("Pulso anormal", TypeValueSintoma.CHECK),
          SintomasModel("Vômito", TypeValueSintoma.CHECK),
          SintomasModel("Visão borrado", TypeValueSintoma.CHECK),
          SintomasModel("Dispneia", TypeValueSintoma.CHECK),
          SintomasModel("Desisdratacao acentuada", TypeValueSintoma.CHECK),
          SintomasModel("GLicemia > 320 ou < 50 mg/dL", TypeValueSintoma.CHECK),
          SintomasModel(
              "Glicemia > 250 e assistomático", TypeValueSintoma.CHECK),
          SintomasModel(
              "Glicemia < 250 e assintomático", TypeValueSintoma.CHECK),
        ],
      ),
      ClassificacaoModel("teste"),
      ClassificacaoModel("teste"),
      ClassificacaoModel("teste"),
      ClassificacaoModel("teste"),
    ];
  }
}
