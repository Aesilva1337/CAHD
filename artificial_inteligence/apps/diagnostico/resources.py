# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import DiagnosticoModel
# Third
from flask_restful import Resource
import json


class Diagnostico(Resource):

    def get(self):

        try:
            diagnosticoList = DiagnosticoModel.objects()
            return {'data':json.loads(diagnosticoList.to_json())}
        except Exception as e:
            return {'erro': e.__str__()}
