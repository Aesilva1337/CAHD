# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz

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
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 0
        if Glasgow is None or Glasgow == '': Glasgow = 0  
        if IntoxicacaoExogena is None or IntoxicacaoExogena == '': IntoxicacaoExogena = 0
        if Convulsao is None or Convulsao == '': Convulsao = 0  
        if Epilepsia is None or Epilepsia == '': Epilepsia = 0  
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
        DadosVitaisAlterados_baixo = fuzz.trimf(vl_DadosVitaisAlterados, [0, 30, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trimf(vl_DadosVitaisAlterados, [80, 90, 100])

        Glasgow_alto = fuzz.trimf(vl_Glasgow, [3, 5, 9])
        Glasgow_normal = fuzz.trimf(vl_Glasgow, [9, 11, 13])
        Glasgow_baixo = fuzz.trimf(vl_Glasgow, [13, 14, 15])

        IntoxicacaoExogena_baixo = fuzz.trimf(vl_IntoxicacaoExogena, [0, 30, 45])
        IntoxicacaoExogena_normal = fuzz.trimf(vl_IntoxicacaoExogena, [35, 60, 85])
        IntoxicacaoExogena_alto = fuzz.trimf(vl_IntoxicacaoExogena, [80, 90, 100])

        Convulsao_baixo = fuzz.trimf(vl_Convulsao, [0, 30, 45])
        Convulsao_normal = fuzz.trimf(vl_Convulsao, [35, 60, 85])
        Convulsao_alto = fuzz.trimf(vl_Convulsao, [80, 90, 100])

        Epilepsia_baixo = fuzz.trimf(vl_Epilepsia, [0, 30, 45])
        Epilepsia_normal = fuzz.trimf(vl_Epilepsia, [35, 60, 85])
        Epilepsia_alto = fuzz.trimf(vl_Epilepsia, [80, 90, 100])

        saida_verde = fuzz.trimf(x_saida, [0, 10, 20])
        saida_amarelo = fuzz.trimf(x_saida, [20, 30, 40])
        saida_vermelho = fuzz.trimf(x_saida, [40, 50, 60])
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
                , saida_verde)

            aggregated = np.fmax(np.fmax(saida_azul_regras, saida_verde_regras), np.fmax(saida_amarelo_regras, saida_vermelho_regras))
            #endregion

            #region .: Defuzzificação e retorno de label para o serviço :.
            result = fuzz.defuzzify.defuzz(x_saida, aggregated, 'mom')

            defuzz = ''

            if result < 0 and result >= 10:
                defuzz = 'Azul'
            elif result < 11 and result >= 20:
                defuzz = 'Verde'
            elif result < 21 and result >= 30:
                defuzz = 'Amarelo'
            elif result < 31 and result >= 40:
                defuzz = 'Laranja'
            else:
                defuzz = 'Vermelho'

            #endregion

            return {'manchester': defuzz }
        except:
            return {'erro': 'Ocorreu um erro, por favor tente novamente!'}