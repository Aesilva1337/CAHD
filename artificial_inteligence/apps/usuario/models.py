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

class UsuarioModel(db.Document):
    '''
    Mapeamento de User
    '''
    meta = {'collection': 'user'}

    name = StringField()
    cpf = StringField()
    password = StringField()