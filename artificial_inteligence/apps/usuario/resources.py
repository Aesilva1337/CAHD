# -*- coding: utf-8 -*-

# Flask
from flask import request
# Local
from .models import UsuarioModel
from apps.responses import resp_ok, resp_exception, resp_data_invalid, resp_already_exists
from apps.responses import resp_notallowed_user, resp_does_not_exist
from apps.messages import MSG_NO_DATA, MSG_PASSWORD_OR_CPF_NOT_SEND, MSG_SUCCESS, MSG_PASSWORD_OR_CPF_INVALID
from .schemas import UserSchema
# Third
from flask_restful import Resource
import json
from mongoengine.errors import DoesNotExist


class Login(Resource):

    def post(self):
        req_data = request.get_json() or None
        schema = UserSchema()

        if req_data is None:
            return resp_data_invalid('Login', [], msg=MSG_NO_DATA)

        data, errors = schema.load(req_data)

        if errors:
            return resp_data_invalid('Login', errors)

        try:
            usuarioList = UsuarioModel.objects.get(cpf=data['cpf'], password=data['password'])
            return resp_ok('Login', MSG_SUCCESS, json.loads(usuarioList.to_json()))
        except DoesNotExist:
            return resp_does_not_exist('Login', MSG_PASSWORD_OR_CPF_INVALID)      
        except Exception as e:
            return resp_exception('Login', description=e.__str__())