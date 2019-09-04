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

class ListaEsperaModel(db.Document):
    '''
    Mapeamento de Wait List
    '''
    meta = {'collection': 'wait_list'}

    name = StringField()
    cpf = StringField()
    enter_date = DateTimeField()
    
class SintomaModal(EmbeddedDocument):
    '''
    Mapeamento de Sintoma dentro da triagem
    '''
    sympton_name = StringField()
    value = IntField()

class TriagemModel(db.Document):
    '''
    Mapeamento de Triagem
    '''
    meta = {'collection': 'triage'}

    cpf = StringField()
    doctor = StringField()
    crm = IntField()
    manchester_classification = IntField()
    main_complaint = StringField()
    attendance_date = DateTimeField()
    sympton = ListField(EmbeddedDocumentField(SintomaModal))
