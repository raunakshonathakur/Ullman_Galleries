from app.models.util import *
from app.models.User import User
from app.models.Form import Form

class StaffAssigned (baseModel):
  SID      =   PrimaryKeyField()
  username =   ForeignKeyField(User)
  FID      =   ForeignKeyField(Form)
  
  def __str__(self):
    return str(self.SID)
    
class StaffAssignedQueries():
  def select_all(self):
    try:
      staffAssigned = StaffAssigned.select()
      return staffAssigned
    except Exception as e:
      print e
    return False
    
  def update_username(self,username,FID):
    try:
      staff_assigned          = StaffAssigned.get(StaffAssigned.FID == FID)
      if username: #if username is not empty string 
        staff_assigned.username = username
      else: #if username is empty i.e unassigned
        staff_assigned.delete_instance()  #delete the whole FID row from database
      staff_assigned.save()
      return True
    except Exception as e:
      return False
    
  def insert(self,username,FID):
    strings=[username]
    if checkStrings(strings):
      try:
        staffAssigned = StaffAssigned(username=username,FID=FID)
        staffAssigned.save()
        return True
      except Exception as e:
        print e
    return False
    
  def find_staff(self,FID):
    try: 
      SID = StaffAssigned.get(StaffAssigned.FID==FID)
      return SID
    except Exception as e:
      return None
