# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean, Nested, DateTime

from apps.messages import MSG_FIELD_REQUIRED


class PacientSchema(Schema):
    name = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    cpf = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    born_date = DateTime(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    sex = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    address = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    zip_code = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    telephone = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    city = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    mother_name = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )