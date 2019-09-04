# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean, Nested

from apps.messages import MSG_FIELD_REQUIRED


class UserSchema(Schema):
    cpf = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    password = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )