from app.models.util import *
from app.models.User import User
from email_validator import validate_email, EmailNotValidError

class Form (baseModel):
  FID               = PrimaryKeyField()
  submit_date       = CharField()
  date_needed       = CharField()
  status            = CharField(max_length=100)
  phone             = CharField(max_length=11)
  department        = CharField(max_length=100)
  purpose           = CharField(max_length=500)
  format_type       = CharField(max_length=100)
  output            = CharField(max_length=200)
  selection         = CharField(max_length=200)
  attachments       = CharField(max_length=100,null=True)
  comments          = CharField(max_length=200,null=True)
  signature         = CharField(max_length=100)
  extra_groups      = CharField(max_length=100,null=True)
  excluded_groups   = CharField(max_length=100,null=True)
  email             = CharField(max_length=100)
  banner            = BooleanField()
  dateDone          = CharField(max_length=10, null=True)
  
  def __str__(self):
    return str(self.FID)

class FormQueries():
  def select_all(self):
    try:
      forms = Form.select()
      return forms
    except Exception as e:
      return False
      
  def select_single(self, FID):
    try:
      form = Form.get(Form.FID == FID)
      return form
    except Exception as e:
      print e 
      return False
      
  def select_from_list(self, listFID):
    try:
      form = Form.select().where(Form.FID << listFID)
      return form
    except Exception as e:
      print e 
      return False
     
  def select_all_incomplete(self):
    try:
      forms = Form.select().where((Form.status != 'Completed') & (Form.status != 'Cancelled'))
      return forms
    except Exception as e:
      return False
 
  def select_all_complete(self):
    try:
      forms = Form.select().where((Form.status != 'New') & (Form.status != 'In Progress'))
      return forms
    except Exception as e:
      return False
      
  def insert(self,submit_date,date_needed,status,phone,department,purpose,format_type,output,selection,attachments,comments,signature,extra_groups,excluded_groups,email ,banner,dateDone):
    # strings=[submit_date,date_needed,status,phone,department,purpose,format_type,output,selection,attachments,comments,signature,extra_groups,excluded_groups,email,dateDone]
    # if checkStrings(strings) & self.validateEmail(email):
    try:
      form = Form(submit_date=submit_date,date_needed=date_needed,status=status,phone=phone,department=department,purpose=purpose,format_type=format_type,output=output,selection=selection,attachments=attachments,comments=comments,signature=signature,extra_groups=extra_groups,excluded_groups=excluded_groups,email=email,banner=banner,dateDone=dateDone)
      form.save()
      return form
    except Exception as e:
      return e
    return False
     
  def insert_attachments_files(self,FID,filename):
    try: 
      form = Form.get(Form.FID == FID)
      form.attachments = filename
      form.save()
      return form
    except Exception as e:
      print e
      return False
      
  def update_status (self, updated_status, FID):
    try:
      form = Form.get(Form.FID == FID)
      form.status = updated_status
      form.save()
    except Exception as e:
      print e
      return False
  
  