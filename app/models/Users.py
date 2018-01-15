from app.models.util import *

class Users (baseModel):
  uid               = IntegerField(primary_key=True)
  username          = TextField()

