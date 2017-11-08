from app.models.util import *
from app.models.User import User
from app.models.Form import Form


class Requestor (baseModel):
  GID      = PrimaryKeyField()
  username = ForeignKeyField(User)
  FID      = ForeignKeyField(Form)
  
  def __str__(self):
    return str(self.GID)
  
class RequestorQueries():
  def select_all(self):
    try:
      requestors = Requestor.select()
      return True
    except Exception as e:
      return False
  
  def select_users(self,FID):
    try:
      requestors = Requestor.select().where(Requestor.FID == FID)
      return requestors
    except Exception as e:
      return False
  
  def insert(self,username,FID):
    strings=[username]
    if checkStrings(strings):
      try:
        requestor = Requestor(username=username,FID=FID)
        requestor.save()
        return True
      except Exception as e:
        print e
    return False
    
  
  