# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist

class Ferida(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Coriza = request.args.get('Coriza')
        RinorreiaPurulenta = request.args.get('RinorreiaPurulenta')
        DorGarganta = request.args.get('DorGarganta')
        DorOuvido = request.args.get('DorOuvido')
        Tosse = request.args.get('Tosse')
        Mialgia = request.args.get('Mialgia')
        #endregion

        #region .: Verificação de valores da API :.
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 10
        if Coriza is None or Coriza == '': Coriza = 10 
        if RinorreiaPurulenta is None or RinorreiaPurulenta == '': RinorreiaPurulenta = 10 
        if DorGarganta is None or DorGarganta == '': DorGarganta = 10 
        if DorOuvido is None or DorOuvido == '': DorOuvido = 10 
        if Tosse is None or Tosse == '': Tosse = 10 
        if Mialgia is None or Mialgia == '': Mialgia = 10 
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_DadosVitaisAlterados = np.arange(0, 101, 1)
        vl_Dor = np.arange(0, 101, 1) 
        vl_Idade = np.arange(0, 101, 1) 
        vl_Temperatura = np.arange(25, 46, 1) 
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        DadosVitaisAlterados_baixo = fuzz.trapmf(vl_DadosVitaisAlterados, [0, 20, 40, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trapmf(vl_DadosVitaisAlterados, [80, 85, 95, 100])

        Dor_baixo = fuzz.trapmf(vl_Dor, [0, 20, 40, 50])
        Dor_moderado = fuzz.trimf(vl_Dor, [40, 50, 70])
        Dor_normal = fuzz.trimf(vl_Dor, [65, 80, 90])
        Dor_alto = fuzz.trapmf(vl_Dor, [80, 85, 95, 100])

        Idade_baixo = fuzz.trapmf(vl_Idade, [0, 20, 40, 45])
        Idade_normal = fuzz.trimf(vl_Idade, [35, 50, 65])
        Idade_alto = fuzz.trapmf(vl_Idade, [65, 70, 90, 100])

        Temperatura_baixo = fuzz.trapmf(vl_Temperatura, [25, 30, 35, 36])
        Temperatura_normal = fuzz.trimf(vl_Temperatura, [36, 37, 39])
        Temperatura_alto = fuzz.trapmf(vl_Temperatura, [39, 40, 44, 45])

        saida_azul = fuzz.trapmf(x_saida, [0, 3, 12, 15])
        saida_verde = fuzz.trimf(x_saida, [15, 22, 29])
        saida_amarelo = fuzz.trimf(x_saida, [29, 36, 43])
        saida_vermelho = fuzz.trapmf(x_saida, [43, 45, 55, 60])
        #endregion

        #region .: Função de ativação para cada nivel definido anteriormente :.
        DadosVitaisAlterados_level_baixo = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_baixo, DadosVitaisAlterados)
        DadosVitaisAlterados_level_medio = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_normal, DadosVitaisAlterados)
        DadosVitaisAlterados_level_alto = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_alto, DadosVitaisAlterados)

        Dor_level_baixo = fuzz.interp_membership(vl_Dor, Dor_baixo, Dor)
        Dor_level_moderado = fuzz.interp_membership(vl_Dor, Dor_moderado, Dor)
        Dor_level_medio = fuzz.interp_membership(vl_Dor, Dor_normal, Dor)
        Dor_level_alto = fuzz.interp_membership(vl_Dor, Dor_alto, Dor)

        Idade_level_baixo = fuzz.interp_membership(vl_Idade, Idade_baixo, Idade)
        Idade_level_medio = fuzz.interp_membership(vl_Idade, Idade_normal, Idade)
        Idade_level_alto = fuzz.interp_membership(vl_Idade, Idade_alto, Idade)

        Temperatura_level_baixo = fuzz.interp_membership(vl_Temperatura, Temperatura_baixo, Temperatura)
        Temperatura_level_medio = fuzz.interp_membership(vl_Temperatura, Temperatura_normal, Temperatura)
        Temperatura_level_alto = fuzz.interp_membership(vl_Temperatura, Temperatura_alto, Temperatura)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                np.fmax(DadosVitaisAlterados_level_alto, Dor_level_alto)
                , saida_vermelho
            )

            saida_amarelo_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_medio, Dor_level_medio),
                    np.fmax(Temperatura_level_alto, Idade_level_alto)
                )
                , saida_amarelo
            )
                    
            saida_verde_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_baixo, Dor_level_moderado)
                    , Temperatura_level_medio
                    )
                , saida_verde
            )

            saida_azul_regras = np.fmin(
                np.fmax(DadosVitaisAlterados_level_baixo, Dor_level_baixo)
                , saida_azul
            )

            aggregated = np.fmax(np.fmax(saida_azul_regras, saida_verde_regras), np.fmax(saida_amarelo_regras, saida_vermelho_regras))
            #endregion

            #region .: Defuzzificação e retorno de label para o serviço :.
            result = fuzz.defuzzify.defuzz(x_saida, aggregated, 'mom')

            defuzz = ''

            if result > 0 and result <= 15:
                defuzz = 'Azul'
            elif result > 15 and result <= 30:
                defuzz = 'Verde'
            elif result > 30 and result <= 43:
                defuzz = 'Amarelo'
            else:
                defuzz = 'Vermelho'


            #endregion

            return resp_ok('Ferida', MSG_SUCCESS, defuzz)
        except Exception as e:
            return resp_exception('Ferida', description=e.__str__())