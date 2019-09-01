# Third
from mongoengine import (
    BooleanField,
    DateTimeField,
    DictField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField,
    IntField,
    ListField
)

from apps.db import db

class SintomaModel(EmbeddedDocument):
    '''
    Mapeamento de sintomas
    '''
    sympton_name = StringField()
    min_value = IntField()
    max_value = IntField()
    value = IntField()
    type_input = IntField()
    property_name = StringField()


class DiagnosticoModel(db.Document):
    '''
    Mapeamento de diagnostico
    '''
    meta = {'collection': 'diagnosis'}

    diagnosis_name = StringField()
    sympton = ListField(EmbeddedDocumentField(SintomaModel))