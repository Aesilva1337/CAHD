# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import PacienteModel
from .models import ListaEsperaModel
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist
from .schemas import PacientSchema
# Third
from flask_restful import Resource
import json
from mongoengine.errors import DoesNotExist
from datetime import datetime


class Paciente(Resource):

    def get(self, cpf=''):
        try:
            if cpf != '' :
                pacienteList = PacienteModel.objects.get(cpf=cpf) 
                return resp_ok('Paciente', MSG_SUCCESS, json.loads(pacienteList.to_json()))
            else:
                pacienteList = PacienteModel.objects()
                return resp_ok('Paciente', MSG_SUCCESS, json.loads(pacienteList.to_json()))           
        except Exception as e:
            return resp_exception('Paciente', description=e.__str__())

    def post(self):
        req_data = request.get_json() or None
        schema = PacientSchema()

        if req_data is None:
            return resp_data_invalid('Cadastro de Paciente', [], msg=MSG_NO_DATA)

        data, errors = schema.load(req_data)

        if errors:
            return resp_data_invalid('Cadastro de Paciente', errors)

        try:
            pacient = PacienteModel(**data)
            pacient.save()
            return resp_ok('Cadastro de Paciente', MSG_SUCCESS, json.loads(pacient.to_json()))    
        except Exception as e:
            return resp_exception('Cadastro de Paciente', description=e.__str__())
        

class ListaEspera(Resource):

    def get(self):
        try:
            waitList = ListaEsperaModel.objects()
            return resp_ok('Lista de Espera', MSG_SUCCESS, json.loads(waitList.to_json()))
        except Exception as e:
            return resp_exception('Lista de Espera', description=e.__str__())

    def post(self):
        try:
            req_data = request.get_json() or None
            pacient = PacienteModel.objects.get(cpf=req_data['cpf'])
            wait_list = ListaEsperaModel()
            wait_list.name = pacient.name
            wait_list.cpf = pacient.cpf
            wait_list.enter_date = datetime.now()
            wait_list.save()
            return resp_ok('Lista de Espera', MSG_SUCCESS, json.loads(wait_list.to_json()))
        except Exception as e:
            return resp_exception('Lista de Espera', description=e.__str__())
            