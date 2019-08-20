# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz

class Diabetes(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        Glicemia = request.args.get('Glicemia')
        Sudorose = request.args.get('Sudorose')
        Desidratacao = request.args.get('Desidratacao')
        AlteracaoMental = request.args.get('AlteracaoMental')
        Febre = request.args.get('Febre')
        Pulso = request.args.get('Pulso')
        Vomito = request.args.get('Vomito')
        VisaoBorrada = request.args.get('VisaoBorrada')
        Dispneia = request.args.get('Dispneia')
        #endregion

        #region .: Verificação de valores da API :.
        if Glicemia is None or Glicemia == '': Glicemia = 0 
        if Sudorose is None or Sudorose == '': Sudorose = 0 
        if Desidratacao is None or Desidratacao == '': Desidratacao = 0 
        if AlteracaoMental is None or AlteracaoMental == '': AlteracaoMental = 0 
        if Febre is None or Febre == '': Febre = 0 
        if Pulso is None or Pulso == '': Pulso = 0 
        if Vomito is None or Vomito == '': Vomito = 0 
        if VisaoBorrada is None or VisaoBorrada == '': VisaoBorrada = 0 
        if Dispneia is None or Dispneia == '': Dispneia = 0 
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_Glicemia = np.arange(0, 361, 1)
        vl_Sudorose = np.arange(0, 101, 1)
        vl_Desidratacao = np.arange(0, 101, 1)
        vl_AlteracaoMental = np.arange(0, 101, 1)
        vl_Febre = np.arange(0, 101, 1)
        vl_Pulso = np.arange(0, 101, 1)
        vl_Vomito = np.arange(0, 101, 1)
        vl_VisaoBorrada = np.arange(0, 101, 1)
        vl_Dispneia = np.arange(0, 101, 1)
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        Glicemia_baixo = fuzz.trimf(vl_Glicemia, [50, 170, 250])
        Glicemia_normal = fuzz.trimf(vl_Glicemia, [250, 285, 320])
        Glicemia_alto = fuzz.trimf(vl_Glicemia,[320, 340, 360])
        Glicemia_baixo_alto = fuzz.trimf(vl_Glicemia, [0, 25, 50])

        Sudorose_baixo = fuzz.trimf(vl_Sudorose, [0, 30, 45])
        Sudorose_normal = fuzz.trimf(vl_Sudorose, [35, 60, 85])
        Sudorose_alto = fuzz.trimf(vl_Sudorose, [80, 90, 100])

        Desidratacao_baixo = fuzz.trimf(vl_Desidratacao, [0, 30, 45])
        Desidratacao_normal = fuzz.trimf(vl_Desidratacao, [35, 60, 85])
        Desidratacao_alto = fuzz.trimf(vl_Desidratacao, [80, 90, 100])

        AlteracaoMental_baixo = fuzz.trimf(vl_AlteracaoMental, [0, 30, 45])
        AlteracaoMental_normal = fuzz.trimf(vl_AlteracaoMental, [35, 60, 85])
        AlteracaoMental_alto = fuzz.trimf(vl_AlteracaoMental, [80, 90, 100])

        Febre_baixo = fuzz.trimf(vl_Febre, [0, 30, 45])
        Febre_normal = fuzz.trimf(vl_Febre, [35, 60, 85])
        Febre_alto = fuzz.trimf(vl_Febre, [80, 90, 100])

        Pulso_baixo = fuzz.trimf(vl_Pulso, [0, 30, 45])
        Pulso_normal = fuzz.trimf(vl_Pulso, [35, 60, 85])
        Pulso_alto = fuzz.trimf(vl_Pulso, [80, 90, 100])

        Vomito_baixo = fuzz.trimf(vl_Vomito, [0, 30, 45])
        Vomito_normal = fuzz.trimf(vl_Vomito, [35, 60, 85])
        Vomito_alto = fuzz.trimf(vl_Vomito, [80, 90, 100])

        VisaoBorrada_baixo = fuzz.trimf(vl_VisaoBorrada, [0, 30, 45])
        VisaoBorrada_normal = fuzz.trimf(vl_VisaoBorrada, [35, 60, 85])
        VisaoBorrada_alto = fuzz.trimf(vl_VisaoBorrada, [80, 90, 100])

        Dispneia_baixo = fuzz.trimf(vl_Dispneia, [0, 30, 45])
        Dispneia_normal = fuzz.trimf(vl_Dispneia, [35, 60, 85])
        Dispneia_alto = fuzz.trimf(vl_Dispneia, [80, 90, 100])

        saida_azul = fuzz.trimf(x_saida, [0, 7, 15])
        saida_verde = fuzz.trimf(x_saida, [15, 22, 29])
        saida_amarelo = fuzz.trimf(x_saida, [29, 36, 43])
        saida_vermelho = fuzz.trimf(x_saida, [43, 50, 60])
        #endregion

        #region .: Função de ativação para cada nivel definido anteriormente :.
        Glicemia_level_baixo = fuzz.interp_membership(vl_Glicemia, Glicemia_baixo, Glicemia)
        Glicemia_level_medio = fuzz.interp_membership(vl_Glicemia, Glicemia_normal, Glicemia)
        Glicemia_level_alto = fuzz.interp_membership(vl_Glicemia, Glicemia_alto, Glicemia)
        Glicemia_level_baixo_alto = fuzz.interp_membership(vl_Glicemia, Glicemia_baixo_alto, Glicemia)

        Sudorose_level_baixo = fuzz.interp_membership(vl_Sudorose, Sudorose_baixo, Sudorose)
        Sudorose_level_medio = fuzz.interp_membership(vl_Sudorose, Sudorose_normal, Sudorose)
        Sudorose_level_alto = fuzz.interp_membership(vl_Sudorose, Sudorose_alto, Sudorose)

        Desidratacao_level_baixo = fuzz.interp_membership(vl_Desidratacao, Desidratacao_baixo, Desidratacao)
        Desidratacao_level_medio = fuzz.interp_membership(vl_Desidratacao, Desidratacao_normal, Desidratacao)
        Desidratacao_level_alto = fuzz.interp_membership(vl_Desidratacao, Desidratacao_alto, Desidratacao)

        AlteracaoMental_level_baixo = fuzz.interp_membership(vl_AlteracaoMental, AlteracaoMental_baixo, Desidratacao)
        AlteracaoMental_level_medio = fuzz.interp_membership(vl_AlteracaoMental, AlteracaoMental_normal, Desidratacao)
        AlteracaoMental_level_alto = fuzz.interp_membership(vl_AlteracaoMental, AlteracaoMental_alto, Desidratacao)

        Febre_level_baixo = fuzz.interp_membership(vl_Febre, Febre_baixo, Febre)
        Febre_level_medio = fuzz.interp_membership(vl_Febre, Febre_normal, Febre)
        Febre_level_alto = fuzz.interp_membership(vl_Febre, Febre_alto, Febre)

        Pulso_level_baixo = fuzz.interp_membership(vl_Pulso, Pulso_baixo, Pulso)
        Pulso_level_medio = fuzz.interp_membership(vl_Pulso, Pulso_normal, Pulso)
        Pulso_level_alto = fuzz.interp_membership(vl_Pulso, Pulso_alto, Pulso)

        Vomito_level_baixo = fuzz.interp_membership(vl_Vomito, Vomito_baixo, Vomito)
        Vomito_level_medio = fuzz.interp_membership(vl_Vomito, Vomito_normal, Vomito)
        Vomito_level_alto = fuzz.interp_membership(vl_Vomito, Vomito_alto, Vomito)

        VisaoBorrada_level_baixo = fuzz.interp_membership(vl_VisaoBorrada, VisaoBorrada_baixo, VisaoBorrada)
        VisaoBorrada_level_medio = fuzz.interp_membership(vl_VisaoBorrada, VisaoBorrada_normal, VisaoBorrada)
        VisaoBorrada_level_alto = fuzz.interp_membership(vl_VisaoBorrada, VisaoBorrada_alto, VisaoBorrada)

        Dispneia_level_baixo = fuzz.interp_membership(vl_Dispneia, Dispneia_baixo, Dispneia)
        Dispneia_level_medio = fuzz.interp_membership(vl_Dispneia, Dispneia_normal, Dispneia)
        Dispneia_level_alto = fuzz.interp_membership(vl_Dispneia, Dispneia_alto, Dispneia)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                np.fmax(
                    np.fmax(AlteracaoMental_level_alto, Sudorose_level_alto),
                    np.fmax(
                        np.fmax(
                            np.fmax(Febre_level_alto, Pulso_level_alto),
                            np.fmax(Vomito_level_alto, VisaoBorrada_level_alto)
                        )
                        , Dispneia_level_alto
                    )
                )
                , saida_vermelho)

            saida_amarelo_regras = np.fmin(
                np.fmax(
                    np.fmin(Glicemia_level_alto, Glicemia_level_baixo_alto)
                    , Desidratacao_level_alto)
                , saida_amarelo)
                    
            saida_verde_regras = np.fmin(
                Glicemia_level_medio
                , saida_verde)

            saida_azul_regras = np.fmin(
                Glicemia_level_baixo
                , saida_azul)

            aggregated = np.fmax(np.fmax(saida_azul_regras, saida_verde_regras), np.fmax(saida_amarelo_regras, saida_vermelho_regras))
            #endregion

            #region .: Defuzzificação e retorno de label para o serviço :.
            result = fuzz.defuzzify.defuzz(x_saida, aggregated, 'mom')

            defuzz = ''

            if result < 0 and result >= 15:
                defuzz = 'Azul'
            elif result < 16 and result >= 29:
                defuzz = 'Verde'
            elif result < 30 and result >= 43:
                defuzz = 'Amarelo'
            else:
                defuzz = 'Vermelho'
            #endregion

            return {'manchester': defuzz }
        except:
            return {'erro': 'Ocorreu um erro, por favor tente novamente!'}