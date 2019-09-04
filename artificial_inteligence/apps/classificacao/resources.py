# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import TriagemModel
from .models import ListaEsperaModel
# Third
from flask_restful import Resource
import json
from collections import namedtuple

class Classificacao(Resource):
    def get(self):
        try:
            cpf = request.args.get('cpf')
            historicoPaciente = TriagemModel.objects(cpf=cpf)
            return {'data':json.loads(historicoPaciente.to_json())}

        except Exception as e:
            return {'erro': e.__str__()}

    def post(self, *args, **kwargs):
        req_data = request.get_json() or None

        if req_data is None:
            return {'erro': 'Nenhuma classificação encontrada para inserir!'}

        cpf = req_data.get('cpf', None)

        try:
            triagem = TriagemModel(**req_data)
            triagem.save()
            ListaEsperaModel.objects.get(cpf=cpf).delete()
            return {'valido': True, 'mensagem': 'Sucesso ao inserir a triagem realizada.'}

        except Exception as e:
            return {'erro': e.__str__()}