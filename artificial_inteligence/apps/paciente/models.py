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

class PacienteModel(db.Document):
    '''
    Mapeamento de Pacient
    '''
    meta = {'collection': 'pacient'}

    name = StringField()
    cpf = StringField()
    born_date = DateTimeField()
    sex = StringField()
    address = StringField()
    zip_code = StringField()
    telephone = StringField()
    city = StringField()
    mother_name = StringField()

class ListaEsperaModel(db.Document):
    '''
    Mapeamento de Wait List
    '''
    meta = {'collection': 'wait_list'}

    name = StringField()
    cpf = StringField()
    enter_date = DateTimeField()