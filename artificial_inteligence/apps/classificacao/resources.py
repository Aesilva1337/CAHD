# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import TriagemModel
from .models import ListaEsperaModel
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist
from .schemas import TriagemSchema
# Third
from flask_restful import Resource
import json
from collections import namedtuple

class Classificacao(Resource):
    def get(self):
        try:
            cpf = request.args.get('cpf')
            historicoPaciente = TriagemModel.objects(cpf=cpf)
            return resp_ok('Histórico do Paciente', MSG_SUCCESS, json.loads(historicoPaciente.to_json()))

        except Exception as e:
            return resp_exception('Histórico do Paciente', description=e.__str__())

    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        schema = TriagemSchema()

        if req_data is None:
            return resp_data_invalid('Triagem', [], msg=MSG_NO_DATA)

        data, errors = schema.load(req_data)
        
        if errors:
            return resp_data_invalid('Triagem', errors)

        try:
            triagem = TriagemModel(**data)
            triagem.save()
            ListaEsperaModel.objects.get(cpf=data['cpf']).delete()
            ListaEsperaModel.save()
            return resp_ok('Triagem', MSG_SUCCESS, {'valido': True})

        except Exception as e:
            return resp_exception('Triagem', description=e.__str__())