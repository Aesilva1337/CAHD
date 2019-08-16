# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz

class Cefaleia(Resource):

    def get(self):

        en = {20:"AMARELO",30:"VERDE", 10:"VERMELHO"}
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Dor = request.args.get('Dor')
        Nuca = request.args.get('Nuca')

        vl_DadosVitaisAlterados = np.arange(0, 100, 1)
        vl_Dor = np.arange(0, 100, 1) 
        vl_Nuca = np.arange(0, 100, 1) 
        x_saida = np.arange(0, 60,1) 

        DadosVitaisAlterados_baixo = fuzz.trimf(vl_DadosVitaisAlterados, [0, 21, 42])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [28, 50, 71])
        DadosVitaisAlterados_alto = fuzz.trimf(vl_DadosVitaisAlterados, [57, 78, 100])

        Dor_baixo = fuzz.trimf(vl_Dor, [0, 15, 30])
        Dor_normal = fuzz.trimf(vl_Dor, [23, 35, 46])
        Dor_alto = fuzz.trimf(vl_Dor, [40, 70, 100])

        Nuca_baixo = fuzz.trimf(vl_Nuca, [0, 16, 33])
        Nuca_normal = fuzz.trimf(vl_Nuca, [26, 33, 40])
        Nuca_alto = fuzz.trimf(vl_Nuca, [33, 50, 100])

        saida_vermelho = fuzz.trimf(x_saida, [0, 10, 20])
        saida_amarelo = fuzz.trimf(x_saida, [10, 20, 40])
        saida_verde = fuzz.trimf(x_saida, [20, 45, 60])

        DadosVitaisAlterados_level_baixo = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_baixo, DadosVitaisAlterados)
        DadosVitaisAlterados_level_normal = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_normal, Dor)
        DadosVitaisAlterados_level_alto = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_alto, Nuca)

        Dor_level_baixo = fuzz.interp_membership(vl_Dor, Dor_baixo, Dor)
        Dor_level_medio = fuzz.interp_membership(vl_Dor, Dor_normal, Dor)
        Dor_level_alto = fuzz.interp_membership(vl_Dor, Dor_alto, Dor)

        Nuca_level_baixo = fuzz.interp_membership(vl_Nuca, Nuca_baixo, Nuca)
        Nuca_level_medio = fuzz.interp_membership(vl_Nuca, Nuca_normal, Nuca)
        Nuca_level_alto = fuzz.interp_membership(vl_Nuca, Nuca_alto, Nuca)

        saida_verde_regras = np.fmin(np.fmin(Dor_level_baixo, Dor_level_medio),
                                    np.fmin(DadosVitaisAlterados_level_baixo, Nuca_level_baixo), saida_verde)

        saida_amarelo_regras = np.fmin(np.fmin(Nuca_level_medio, Nuca_level_alto), saida_amarelo)

        saida_vermelho_regras = np.fmin(np.fmin(np.fmin(DadosVitaisAlterados_level_alto, Nuca_level_alto), Dor_level_alto), saida_vermelho)

        aggregated = np.fmax(saida_verde, np.fmax(saida_amarelo, saida_vermelho))

        #result = fuzz.defuzzify.dcentroid(x_saida, aggregated, 61.4)
        result = fuzz.defuzzify.defuzz(x_saida, aggregated, 'som')

        defuzz = en[result]

        return {'manchester': defuzz }
