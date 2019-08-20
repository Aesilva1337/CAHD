# Importamos as classes API e Resource
from flask_restful import Api, Resource
from apps.manchester.cefaleia import Cefaleia
from apps.manchester.convulsao_coma import ConsulsaoComa
from apps.manchester.diabetes import Diabetes

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
    api.add_resource(ConsulsaoComa, '/convulsao_coma')

    # API para calculo da classficação de manchester a partir do diagnostico Diabetes
    api.add_resource(Diabetes, '/diabetes')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)