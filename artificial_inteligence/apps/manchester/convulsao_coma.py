# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist

class ConsulsaoComa(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Glasgow = request.args.get('Glasgow')
        IntoxicacaoExogena = request.args.get('IntoxicacaoExogena')
        Convulsao = request.args.get('Convulsao')
        Epilepsia = request.args.get('Epilepsia')
        #endregion

        #region .: Verificação de valores da API :.
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 10
        if Glasgow is None or Glasgow == '': Glasgow = 10  
        if IntoxicacaoExogena is None or IntoxicacaoExogena == '': IntoxicacaoExogena = 10
        if Convulsao is None or Convulsao == '': Convulsao = 10  
        if Epilepsia is None or Epilepsia == '': Epilepsia = 10  
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_DadosVitaisAlterados = np.arange(0, 101, 1)
        vl_Glasgow = np.arange(3, 16, 1)
        vl_IntoxicacaoExogena = np.arange(0, 101, 1)
        vl_Convulsao = np.arange(0, 101, 1)
        vl_Epilepsia = np.arange(0, 101, 1)
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        DadosVitaisAlterados_baixo = fuzz.trapmf(vl_DadosVitaisAlterados, [0, 20, 30, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trapmf(vl_DadosVitaisAlterados, [80, 85, 95, 100])

        Glasgow_alto = fuzz.trapmf(vl_Glasgow, [3, 5, 8, 9])
        Glasgow_normal = fuzz.trimf(vl_Glasgow, [9, 11, 13])
        Glasgow_baixo = fuzz.trapmf(vl_Glasgow, [12, 13, 14, 15])

        IntoxicacaoExogena_baixo = fuzz.trapmf(vl_IntoxicacaoExogena, [0, 20, 30, 45])
        IntoxicacaoExogena_normal = fuzz.trimf(vl_IntoxicacaoExogena, [35, 60, 85])
        IntoxicacaoExogena_alto = fuzz.trapmf(vl_IntoxicacaoExogena, [80, 85, 95, 100])

        Convulsao_baixo = fuzz.trapmf(vl_Convulsao, [0, 20, 30, 45])
        Convulsao_normal = fuzz.trimf(vl_Convulsao, [35, 60, 85])
        Convulsao_alto = fuzz.trapmf(vl_Convulsao, [80, 85, 95, 100])

        Epilepsia_baixo = fuzz.trapmf(vl_Epilepsia, [0, 20, 30, 45])
        Epilepsia_normal = fuzz.trimf(vl_Epilepsia, [35, 60, 85])
        Epilepsia_alto = fuzz.trapmf(vl_Epilepsia, [80, 85, 95, 100])

        saida_azul = fuzz.trapmf(x_saida, [0, 3, 12, 15])
        saida_verde = fuzz.trimf(x_saida, [15, 22, 29])
        saida_amarelo = fuzz.trimf(x_saida, [29, 36, 43])
        saida_vermelho = fuzz.trapmf(x_saida, [43, 47, 57, 60])
        #endregion

        #region .: Função de ativação para cada nivel definido anteriormente :.
        DadosVitaisAlterados_level_baixo = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_baixo, DadosVitaisAlterados)
        DadosVitaisAlterados_level_medio = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_normal, DadosVitaisAlterados)
        DadosVitaisAlterados_level_alto = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_alto, DadosVitaisAlterados)
        
        #Glasgow_level_baixo = fuzz.interp_membership(vl_Glasgow, Glasgow_baixo, Glasgow)
        #Glasgow_level_medio = fuzz.interp_membership(vl_Glasgow, Glasgow_normal, Glasgow)
        Glasgow_level_alto = fuzz.interp_membership(vl_Glasgow, Glasgow_alto, Glasgow)

        #IntoxicacaoExogena_level_baixo = fuzz.interp_membership(vl_IntoxicacaoExogena, IntoxicacaoExogena_baixo, IntoxicacaoExogena)
        #IntoxicacaoExogena_level_medio = fuzz.interp_membership(vl_IntoxicacaoExogena, IntoxicacaoExogena_normal, IntoxicacaoExogena)
        IntoxicacaoExogena_level_alto = fuzz.interp_membership(vl_IntoxicacaoExogena, IntoxicacaoExogena_alto, IntoxicacaoExogena)
        
        Convulsao_level_baixo = fuzz.interp_membership(vl_Convulsao, Convulsao_baixo, Convulsao)
        Convulsao_level_medio = fuzz.interp_membership(vl_Convulsao, Convulsao_normal, Convulsao)
        Convulsao_level_alto = fuzz.interp_membership(vl_Convulsao, Convulsao_alto, Convulsao)
        
        #Epilepsia_level_baixo = fuzz.interp_membership(vl_Epilepsia, Epilepsia_baixo, Epilepsia)
        #Epilepsia_level_medio = fuzz.interp_membership(vl_Epilepsia, Epilepsia_normal, Epilepsia)
        Epilepsia_level_alto = fuzz.interp_membership(vl_Epilepsia, Epilepsia_alto, Epilepsia)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                np.fmax(
                    np.fmax(Glasgow_level_alto, DadosVitaisAlterados_level_alto),
                    np.fmax(Convulsao_level_alto, IntoxicacaoExogena_level_alto)
                )
                , saida_vermelho)

            saida_amarelo_regras = np.fmin(
                np.fmax(
                    np.fmax(Convulsao_level_medio, DadosVitaisAlterados_level_medio),
                    Epilepsia_level_alto)
                , saida_amarelo)
                    
            saida_verde_regras = np.fmin(
                np.fmax(
                    np.fmin(Convulsao_level_baixo, DadosVitaisAlterados_level_baixo)
                    , Convulsao_level_medio)
                , saida_verde)

            saida_azul_regras = np.fmin(
                np.fmax(Convulsao_level_baixo, DadosVitaisAlterados_level_baixo)
                , saida_azul)

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

            return resp_ok('Convulsão ou Coma', MSG_SUCCESS, defuzz)
        except Exception as e:
            return resp_exception('Convulsão ou Coma', description=e.__str__())