class BaseService {
  static const String BASE = "https://cahd-251618.appspot.com";
  static const String DIAGNOSTICO = "diagnostico";
  static const String LISTA_ESPERA = "lista_espera";
  static const String PACIENTE = "pacientes";
  static const String CLASSIFICACAO_MANCHESTER = "classificacao_machester";
  static const String LOGIN = "login";
  static const String CEFALEIA = "cefaleia";
  static const String CONVULSAO = "convulsao";
  static const String DIABETES = "diabetes";
  static const String DOENCAPSC = "doencaPsiquiatrica";
  static const String DORABN = "dor_abdominal";
  static const String DORTOR = "dor_toracica";
  static const String FERIDA = "ferida";

  static String formatQuery(Map<String, String> props) {
    String result = "?";
    props.forEach((key, value) =>
        {result = value != null ? "$result$key=$value&" : "$result"});
    return result;
  }

  static String getPathClassificacao(ClassficacaoEnum classificacao) {
    switch (classificacao) {
      case ClassficacaoEnum.DIAGNOSTICO:
        return DIAGNOSTICO;
      case ClassficacaoEnum.CEFALEIA:
        return CEFALEIA;
      case ClassficacaoEnum.CONVULSAO:
        return CONVULSAO;
      case ClassficacaoEnum.DIABETES:
        return DIABETES;
      case ClassficacaoEnum.DOENCAPSC:
        return DOENCAPSC;
      case ClassficacaoEnum.DORABN:
        return DORABN;
      case ClassficacaoEnum.DORTOR:
        return DORTOR;
      case ClassficacaoEnum.FERIDA:
        return FERIDA;
      default:
        return "";
    }
  }
}

enum ClassficacaoEnum {
  DIAGNOSTICO,
  CEFALEIA,
  CONVULSAO,
  DIABETES,
  DOENCAPSC,
  DORABN,
  DORTOR,
  FERIDA,
}
