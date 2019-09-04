# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import PacienteModel
from .models import ListaEsperaModel
# Third
from flask_restful import Resource
import json


class Paciente(Resource):

    def get(self, cpf=''):
        try:
            if cpf != '' :
                pacienteList = PacienteModel.objects.get(cpf=cpf) 
                return {'data':json.loads(pacienteList.to_json())}
            else:
                pacienteList = PacienteModel.objects()
                return {'data':json.loads(pacienteList.to_json())}            
        except Exception as e:
            return {'erro': e.__str__()}

class ListaEspera(Resource):

    def get(self):
        try:
            waitList = ListaEsperaModel.objects()
            return {'data':json.loads(waitList.to_json())}
        except Exception as e:
            return {'erro': e.__str__()}