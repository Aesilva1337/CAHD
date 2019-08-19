# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz

class Cefaleia(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Dor = request.args.get('Dor')
        Nuca = request.args.get('Nuca')
        SinaisNeurologicos = request.args.get('SinaisNeurologicos')
        PAS = request.args.get('PAS')
        PAD = request.args.get('PAD')
        #endregion

        #region .: Verificação de valores da API :.
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 0
        if Dor is None or Dor == '': Dor = 0
        if Nuca is None or Nuca == '': Nuca = 0
        if SinaisNeurologicos is None or SinaisNeurologicos == '': SinaisNeurologicos = 0
        if PAD is None or PAD == '': PAD = 0
        if PAS is None or PAS == '': PAD = 0    
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_DadosVitaisAlterados = np.arange(0, 101, 1)
        vl_Dor = np.arange(0, 101, 1) 
        vl_Nuca = np.arange(0, 101, 1) 
        vl_SinaisNeurologicos = np.arange(0, 101, 1) 
        vl_PAS = np.arange(0, 101, 1) 
        vl_PAD = np.arange(0, 101, 1) 
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        DadosVitaisAlterados_baixo = fuzz.trimf(vl_DadosVitaisAlterados, [0, 30, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trimf(vl_DadosVitaisAlterados, [80, 90, 100])

        Dor_baixo = fuzz.trimf(vl_Dor, [0, 50, 70])
        Dor_normal = fuzz.trimf(vl_Dor, [65, 80, 90])
        Dor_alto = fuzz.trimf(vl_Dor, [75, 95, 100])

        Nuca_baixo = fuzz.trimf(vl_Nuca, [0, 30, 60])
        Nuca_normal = fuzz.trimf(vl_Nuca, [50, 60, 80])
        Nuca_alto = fuzz.trimf(vl_Nuca, [80, 90, 100])

        SinaisNeurologicos_baixo = fuzz.trimf(vl_SinaisNeurologicos, [0, 50, 70])
        SinaisNeurologicos_normal = fuzz.trimf(vl_SinaisNeurologicos, [65, 80, 90])
        SinaisNeurologicos_alto = fuzz.trimf(vl_SinaisNeurologicos, [75, 95, 100])

        #PAS_baixo = fuzz.trimf(vl_PAS, [0, 50, 70])
        #PAS_normal = fuzz.trimf(vl_PAS, [65, 80, 90])
        PAS_alto = fuzz.trimf(vl_PAS, [75, 95, 100])

        #PAD_baixo = fuzz.trimf(vl_PAD, [0, 50, 70])
        #PAD_normal = fuzz.trimf(vl_PAD, [65, 80, 90])
        PAD_alto = fuzz.trimf(vl_PAD, [75, 95, 100])

        saida_verde = fuzz.trimf(x_saida, [0, 10, 20])
        saida_amarelo = fuzz.trimf(x_saida, [20, 30, 40])
        saida_vermelho = fuzz.trimf(x_saida, [40, 50, 60])
        #endregion

        #region .: Função de ativação para cada nivel definido anteriormente :.
        DadosVitaisAlterados_level_baixo = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_baixo, DadosVitaisAlterados)
        DadosVitaisAlterados_level_medio = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_normal, DadosVitaisAlterados)
        DadosVitaisAlterados_level_alto = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_alto, DadosVitaisAlterados)

        Dor_level_baixo = fuzz.interp_membership(vl_Dor, Dor_baixo, Dor)
        Dor_level_medio = fuzz.interp_membership(vl_Dor, Dor_normal, Dor)
        Dor_level_alto = fuzz.interp_membership(vl_Dor, Dor_alto, Dor)

        Nuca_level_baixo = fuzz.interp_membership(vl_Nuca, Nuca_baixo, Nuca)
        Nuca_level_medio = fuzz.interp_membership(vl_Nuca, Nuca_normal, Nuca)
        Nuca_level_alto = fuzz.interp_membership(vl_Nuca, Nuca_alto, Nuca)

        SinaisNeurologicos_level_baixo = fuzz.interp_membership(vl_SinaisNeurologicos, SinaisNeurologicos_baixo, SinaisNeurologicos)
        SinaisNeurologicos_level_medio = fuzz.interp_membership(vl_SinaisNeurologicos, SinaisNeurologicos_normal, SinaisNeurologicos)
        SinaisNeurologicos_level_alto = fuzz.interp_membership(vl_SinaisNeurologicos, SinaisNeurologicos_alto, SinaisNeurologicos)

        #PAS_level_baixo = fuzz.interp_membership(vl_PAS, PAS_baixo, PAS)
        #PAS_level_medio = fuzz.interp_membership(vl_PAS, PAS_normal, PAS)
        PAS_level_alto = fuzz.interp_membership(vl_PAS, PAS_alto, PAS)

        #PAD_level_baixo = fuzz.interp_membership(vl_PAD, PAD_baixo, PAD)
        #PAD_level_medio = fuzz.interp_membership(vl_PAD, PAD_normal, PAD)
        PAD_level_alto = fuzz.interp_membership(vl_PAD, PAD_alto, PAD)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                        np.fmax(
                                np.fmax(np.fmax(PAS_level_alto, Dor_level_alto), DadosVitaisAlterados_level_alto),
                                np.fmax(np.fmax(PAD_level_alto, SinaisNeurologicos_level_alto), Nuca_level_alto)
                                ), saida_vermelho
                        )

            saida_amarelo_regras = np.fmin(        
                        np.fmax(
                            np.fmax(
                                    np.fmin(Nuca_level_medio, Nuca_level_alto),
                                    np.fmin(SinaisNeurologicos_level_medio, Dor_level_alto)
                                    )
                                , DadosVitaisAlterados_level_medio)
                            , saida_amarelo
                            )
                    
            saida_verde_regras = np.fmin(
                        np.fmin(
                            np.fmax(Dor_level_baixo, Dor_level_medio),
                            np.fmax(np.fmax(DadosVitaisAlterados_level_baixo, Nuca_level_baixo), SinaisNeurologicos_level_baixo)
                            ), saida_verde
                        )

            aggregated = np.fmax(saida_verde_regras, np.fmax(saida_amarelo_regras, saida_vermelho_regras))
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

            return { 'manchester': defuzz }
        except:
            return {'erro': 'Ocorreu um erro, por favor tente novamente!'}