from app.models.util import *

class User (baseModel):
  username  = CharField(primary_key=True)
  is_admin  = BooleanField(default=False)
  firstname = CharField(max_length=100)
  lastname  = CharField(max_length=100)
  
  def __str__(self):
    return self.username

class UserQueries():
  def select_all(self):
    try:
      users = User.select().order_by(User.lastname)
      return users
    except Exception as e:
      return False
  
  def insert(self,username,is_admin,firstname,lastname):
    '''Purpose: An insert query to add a new user
    Args:
      username  (str):  The user's username
      is_admin (bool):  Admin status true or false
      firstname (str):  The user's firstname
      lastname  (str):  The user's lastname
    Return:
      status: True if successful, False if unsuccessful'''
    strings = [username,firstname,lastname]
    bools  = [is_admin]
    if checkStrings(strings) and checkBooleans(bools): 
      try:
        user = User(username=username, is_admin=is_admin, firstname=firstname, lastname=lastname)
        user.save(force_insert=True)
        return True
      except Exception as e:
        # Log Exception
        print e
    return False

  def select_single(self,username):
    strings=[username]
    if checkStrings(strings):
      try:
        user=User.get(User.username==username)
        return user
      except Exception as e:
        print e
        return False
    return False
    
  def select_admins(self):
    try:
      admins=User.select().where(User.is_admin==True)
      return admins
    except Exception as e:
      return False
  
  def select_non_admins(self):
    try:
      admins=User.select().where(User.is_admin==False)
      return admins
    except Exception as e:
      return False
      
  def change_admin_status(self,username, newStatus):
    strings=[username]
    if checkStrings(strings):
      try:
        user = self.select_single(username)
        user.is_admin = newStatus
        user.save()
        return user
      except Exception as e:
        print e
    return False
    
