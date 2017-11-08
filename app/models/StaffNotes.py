from app.models.util import *
from app.models.Form import Form
from app.models.User import User

class StaffNotes (baseModel):
  SNID       = PrimaryKeyField()
  username   = ForeignKeyField(User)
  FID        = ForeignKeyField(Form)
  notes      = CharField(max_length = 200)
  date       = CharField()
  
  def __str__(self):
    return str(self.SNID)
    
class StaffNotesQueries():
  def select_all(self):
    try:
      staffNotes = StaffNotes.select()
      return staffNotes
    except Exception as e:
      print e
    return False
    
  def insert(self,username,FID,notes,date):
    strings = [notes,date,username]
    if checkStrings(strings):
      try:
        staffNotes = StaffNotes(username=username,FID=FID,notes=notes,date=date)
        staffNotes.save()
        return True
      except Exception as e:
        print e
    return False
    
  def find_notes(self,FID):
    try:
      staff_notes = StaffNotes.select().where(StaffNotes.FID == FID)
      if staff_notes.exists():
        return staff_notes
      return False
    except Exception as e:
      print e
      return False
  
  def delete_note(self,SNID):
    try:
      staff_notes = StaffNotes.select().where(StaffNotes.SNID == SNID)
      if staff_notes.exists():
          staff_notes = StaffNotes.delete().where(StaffNotes.SNID == SNID)
          staff_notes.execute()
      return True
    except Exception as e:
      print e
      return False
  
  def update_note(self,SNID, newNote):
    try:
      staff_notes = StaffNotes.select().where(StaffNotes.SNID == SNID)
      if staff_notes.exists():
          staff_notes = StaffNotes.update(notes = newNote).where(StaffNotes.SNID == SNID)
          staff_notes.execute()
      return True
    except Exception as e:
      print e
      return False
 
    
   
    

    
    