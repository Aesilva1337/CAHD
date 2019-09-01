# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz

class DorToracica(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Dor = request.args.get('Dor')
        FrequenciaDor = request.args.get('FrequenciaDor')
        Idade = request.args.get('Idade')
        #endregion

        #region .: Verificação de valores da API :.
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 10
        if Dor is None or Dor == '': Dor = 10 
        if FrequenciaDor is None or FrequenciaDor == '': FrequenciaDor = 10 
        if Idade is None or Idade == '': Idade = 10 
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_DadosVitaisAlterados = np.arange(0, 101, 1)
        vl_Dor = np.arange(0, 101, 1) 
        vl_FrequenciaDor = np.arange(0, 101, 1) 
        vl_Idade = np.arange(0, 101, 1) 
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        DadosVitaisAlterados_baixo = fuzz.trimf(vl_DadosVitaisAlterados, [0, 30, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trimf(vl_DadosVitaisAlterados, [80, 90, 100])

        Dor_baixo = fuzz.trimf(vl_Dor, [0, 25, 50])
        Dor_moderado = fuzz.trimf(vl_Dor, [40, 50, 70])
        Dor_normal = fuzz.trimf(vl_Dor, [65, 80, 90])
        Dor_alto = fuzz.trimf(vl_Dor, [80, 95, 100])

        FrequenciaDor_baixo = fuzz.trimf(vl_FrequenciaDor, [0, 30, 45])
        FrequenciaDor_normal = fuzz.trimf(vl_FrequenciaDor, [35, 60, 85])
        FrequenciaDor_alto = fuzz.trimf(vl_FrequenciaDor, [80, 90, 100])

        Idade_baixo = fuzz.trimf(vl_Idade, [0, 30, 40])
        Idade_normal = fuzz.trimf(vl_Idade, [40, 50, 55])
        Idade_alto = fuzz.trimf(vl_Idade, [55, 85, 100])

        saida_azul = fuzz.trimf(x_saida, [0, 7, 15])
        saida_verde = fuzz.trimf(x_saida, [15, 22, 29])
        saida_amarelo = fuzz.trimf(x_saida, [29, 36, 43])
        saida_vermelho = fuzz.trimf(x_saida, [43, 50, 60])
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
  
        FrequenciaDor_level_baixo = fuzz.interp_membership(vl_FrequenciaDor, FrequenciaDor_baixo, FrequenciaDor)
        FrequenciaDor_level_medio = fuzz.interp_membership(vl_FrequenciaDor, FrequenciaDor_normal,FrequenciaDor)
        FrequenciaDor_level_alto = fuzz.interp_membership(vl_FrequenciaDor, FrequenciaDor_alto, FrequenciaDor)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_alto, Dor_level_alto)
                    , FrequenciaDor_level_alto)
                , saida_vermelho
            )

            saida_amarelo_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_medio, Dor_level_medio),
                    np.fmax(FrequenciaDor_level_medio, Idade_level_alto)
                )
                , saida_amarelo
            )
                    
            saida_verde_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_baixo, Dor_level_moderado),
                    np.fmax(Idade_level_medio, FrequenciaDor_level_baixo)
                    )
                , saida_verde
            )

            saida_azul_regras = np.fmin(
                np.fmax(
                    np.fmax(DadosVitaisAlterados_level_baixo, Dor_level_baixo)
                    , Idade_level_baixo
                    )
                , saida_azul
            )

            aggregated = np.fmax(np.fmax(saida_azul_regras, saida_verde_regras), np.fmax(saida_amarelo_regras, saida_vermelho_regras))
            #endregion

            #region .: Defuzzificação e retorno de label para o serviço :.
            result = fuzz.defuzzify.defuzz(x_saida, aggregated, 'mom')

            defuzz = ''

            if result > 0 and result <= 15:
                defuzz = 'Azul'
            elif result > 16 and result <= 29:
                defuzz = 'Verde'
            elif result > 30 and result <= 43:
                defuzz = 'Amarelo'
            else:
                defuzz = 'Vermelho'


            #endregion

            return { 'manchester': defuzz }
        except Exception as e:
            return {'erro': e.__str__()}