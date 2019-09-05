# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import PacienteModel
from .models import ListaEsperaModel
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist
# Third
from flask_restful import Resource
import json


class Paciente(Resource):

    def get(self, cpf=''):
        try:
            if cpf != '' :
                pacienteList = PacienteModel.objects.get(cpf=cpf) 
                return resp_ok('Login', MSG_SUCCESS, json.loads(pacienteList.to_json()))
            else:
                pacienteList = PacienteModel.objects()
                return resp_ok('Login', MSG_SUCCESS, json.loads(pacienteList.to_json()))           
        except Exception as e:
            return resp_exception('Paciente', description=e.__str__())

class ListaEspera(Resource):

    def get(self):
        try:
            waitList = ListaEsperaModel.objects()
            return resp_ok('Login', MSG_SUCCESS, json.loads(waitList.to_json()))
        except Exception as e:
            return resp_exception('Lista de Espera', description=e.__str__())