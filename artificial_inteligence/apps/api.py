# -*- coding: utf-8 -*-
# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.manchester.cefaleia import Cefaleia
from apps.manchester.convulsao_coma import ConsulsaoComa
from apps.manchester.diabetes import Diabetes
from apps.manchester.doenca_psiquiatrica import DoencaPsiquiatrica
from apps.manchester.dor_abdominal import DorAbdominal
from apps.manchester.dor_toracica import DorToracica
from apps.manchester.ferida import Ferida
from apps.diagnostico.resources import Diagnostico
from apps.paciente.resources import Paciente
from apps.paciente.resources import ListaEspera
from apps.classificacao.resources import Classificacao
from apps.usuario.resources import Login

# Criamos uma classe que extende de Resource
class Index(Resource):

    # Definimos a operação get do protocolo http
    def get(self):

        # retornamos um simples dicionário que será automáticamente
        # retornado em json pelo flask
        return {'hello': 'world by apps'}


# Instânciamos a API do FlaskRestful
api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/')

    # API para calculo da classficação de manchester a partir do diagnostico Cefaleia
    api.add_resource(Cefaleia, '/cefaleia')

    # API para calculo da classficação de manchester a partir do diagnostico Convulsão ou Coma
    api.add_resource(ConsulsaoComa, '/convulsao')

    # API para calculo da classficação de manchester a partir do diagnostico Diabetes
    api.add_resource(Diabetes, '/diabetes')

    # API para calculo da classficação de manchester a partir do diagnostico Doença Psiquiatrica
    api.add_resource(DoencaPsiquiatrica, '/doenca_psiquiatrica')

    # API para calculo da classficação de manchester a partir do diagnostico Dor Abdominal
    api.add_resource(DorAbdominal, '/dor_abdominal')

    # API para calculo da classficação de manchester a partir do diagnostico Dor Toracica
    api.add_resource(DorToracica, '/dor_toracica')

    # API para calculo da classficação de manchester a partir do diagnostico Ferida
    api.add_resource(Ferida, '/ferida')

    # API para listagem de diagnostico
    api.add_resource(Diagnostico, '/diagnostico')

    # API para listagem de diagnostico
    api.add_resource(ListaEspera, '/lista_espera')
    
    # API para listagem de diagnostico
    api.add_resource(Paciente, '/pacientes/<string:cpf>', '/pacientes')
    
    # API para listagem de classificação de manchester
    api.add_resource(Classificacao, '/classificacao_machester' )

    # API para listagem de classificação de manchester
    api.add_resource(Login, '/login' )

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)