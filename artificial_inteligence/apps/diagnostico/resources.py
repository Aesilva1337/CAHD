# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import DiagnosticoModel
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist
# Third
from flask_restful import Resource
import json


class Diagnostico(Resource):

    def get(self):

        try:
            diagnosticoList = DiagnosticoModel.objects()
            return resp_ok('Diagnostico', MSG_SUCCESS, json.loads(diagnosticoList.to_json()))
        except Exception as e:
            return resp_exception('Diagnostico', description=e.__str__())
