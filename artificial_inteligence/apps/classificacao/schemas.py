# -*- coding: utf-8 -*-


from marshmallow import Schema
from marshmallow.fields import Email, Str, Boolean, Nested, Int, List

from apps.messages import MSG_FIELD_REQUIRED


class SymptonSchema(Schema):
    sympton_name = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    ) 
    value = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    ) 

class TriagemSchema(Schema):
    cpf = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    doctor = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    main_complaint = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    attendance_date = Str(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    crm = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    manchester_classification = Int(
        required=True, error_messages={'required': MSG_FIELD_REQUIRED}
    )
    sympton = List(Nested(SymptonSchema))