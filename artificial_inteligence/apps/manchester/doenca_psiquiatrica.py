# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from flask import request
import numpy as np
import skfuzzy as fuzz
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist

class DoencaPsiquiatrica(Resource):

    def get(self):
        #en = {1:"Azul", 2: "Verde", 3: "Amarelo", 4: "Laranja", 5: "Vermelho"} // Classificação de Manchester
        #region .: Variaveis de Entrada :.
        DadosVitaisAlterados = request.args.get('DadosVitais')
        Agitacao = request.args.get('Agitacao')
        Depressao = request.args.get('Depressao')
        EstadoMental = request.args.get('EstadoMental')
        #endregion

        #region .: Verificação de valores da API :.
        if DadosVitaisAlterados is None or DadosVitaisAlterados == '': DadosVitaisAlterados = 10
        if Agitacao is None or Agitacao == '': Agitacao = 10
        if Depressao is None or Depressao == '': Depressao = 10
        if EstadoMental is None or EstadoMental == '': EstadoMental = 10
        #endregion

        #region .: Definição do range de cada sintoma :.
        vl_DadosVitaisAlterados = np.arange(0, 101, 1)
        vl_Agitacao = np.arange(0, 101, 1)
        vl_Depressao = np.arange(0, 101, 1)
        vl_EstadoMental = np.arange(0, 101, 1)
        x_saida = np.arange(0, 61, 1) 
        #endregion

        #region .: Definição do range da pertinencia de cada sintoma :.
        DadosVitaisAlterados_baixo = fuzz.trimf(vl_DadosVitaisAlterados, [0, 30, 45])
        DadosVitaisAlterados_normal = fuzz.trimf(vl_DadosVitaisAlterados, [35, 60, 85])
        DadosVitaisAlterados_alto = fuzz.trimf(vl_DadosVitaisAlterados, [80, 90, 100])

        Agitacao_baixo = fuzz.trimf(vl_Agitacao, [0, 30, 45])
        Agitacao_normal = fuzz.trimf(vl_Agitacao, [35, 60, 85])
        Agitacao_alto = fuzz.trimf(vl_Agitacao, [80, 90, 100])
        
        Depressao_baixo = fuzz.trimf(vl_Depressao, [0, 30, 45])
        Depressao_normal = fuzz.trimf(vl_Depressao, [35, 60, 85])
        Depressao_alto = fuzz.trimf(vl_Depressao, [80, 90, 100])
        
        EstadoMental_baixo = fuzz.trimf(vl_EstadoMental, [0, 30, 45])
        EstadoMental_normal = fuzz.trimf(vl_EstadoMental, [35, 60, 85])
        EstadoMental_alto = fuzz.trimf(vl_EstadoMental, [80, 90, 100])

        saida_azul = fuzz.trimf(x_saida, [0, 7, 15])
        saida_verde = fuzz.trimf(x_saida, [15, 22, 29])
        saida_amarelo = fuzz.trimf(x_saida, [29, 36, 43])
        saida_vermelho = fuzz.trimf(x_saida, [43, 50, 60])
        #endregion

        #region .: Função de ativação para cada nivel definido anteriormente :.
        DadosVitaisAlterados_level_baixo = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_baixo, DadosVitaisAlterados)
        DadosVitaisAlterados_level_medio = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_normal, DadosVitaisAlterados)
        DadosVitaisAlterados_level_alto = fuzz.interp_membership(vl_DadosVitaisAlterados, DadosVitaisAlterados_alto, DadosVitaisAlterados)
        
        Agitacao_level_baixo = fuzz.interp_membership(vl_Agitacao, Agitacao_baixo, Agitacao)
        Agitacao_level_medio = fuzz.interp_membership(vl_Agitacao, Agitacao_normal, Agitacao)
        Agitacao_level_alto = fuzz.interp_membership(vl_Agitacao, Agitacao_alto, Agitacao)
        
        Depressao_level_baixo = fuzz.interp_membership(vl_Depressao, Depressao_baixo, Depressao)
        Depressao_level_medio = fuzz.interp_membership(vl_Depressao, Depressao_normal, Depressao)
        Depressao_level_alto = fuzz.interp_membership(vl_Depressao, Depressao_alto, Depressao)
        
        EstadoMental_level_baixo = fuzz.interp_membership(vl_EstadoMental, EstadoMental_baixo, EstadoMental)
        EstadoMental_level_medio = fuzz.interp_membership(vl_EstadoMental, EstadoMental_normal, EstadoMental)
        EstadoMental_level_alto = fuzz.interp_membership(vl_EstadoMental, EstadoMental_alto, EstadoMental)
        #endregion

        try:
            #region .: Definição das regras para o valor de saida :.
            saida_vermelho_regras = np.fmin(
                np.fmax(EstadoMental_level_alto,
                    np.fmax(Agitacao_level_alto, Depressao_level_alto)
                )
                , saida_vermelho)

            saida_amarelo_regras = np.fmin(
                np.fmax(
                    np.fmax(Depressao_level_medio, EstadoMental_level_medio),
                    np.fmax(Agitacao_level_medio, DadosVitaisAlterados_level_medio)
                )
                , saida_amarelo)
                    
            saida_verde_regras = np.fmin(
                np.fmax(DadosVitaisAlterados_level_baixo, Depressao_level_medio)
                , saida_verde)

            saida_azul_regras = np.fmin(
                np.fmax(EstadoMental_level_baixo,
                    np.fmax(DadosVitaisAlterados_level_baixo, Depressao_level_baixo)
                )
                , saida_azul)

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

            return resp_ok('Doença Psiquiatrica', MSG_SUCCESS, defuzz)
        except Exception as e:
            return resp_exception('Doença Psiquiatrica', description=e.__str__())