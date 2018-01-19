import glob,os,sys

path = os.getcwd()
test_dir = os.path.join(path,'app/config/')

if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

from app.models import *

def drop_tables():
    models = [Images, Forms, Galleries,Files,Users] 
    for model in models:
        model.drop_table()

def create_tables():
    models = [Users, Files,Galleries,Forms,Images] 
    for model in models:
        model.create_table()

def dummy_data():
    drop_tables()
    create_tables()
    load_user_data()
    load_files_data()
    load_galleries_data()
    load_forms_data()
    load_images_data()

def load_user_data():
    Users(uid=1, username="adminUser").save(force_insert=True)

def load_files_data():
    Files(fid=1, filetype="pdf", form=1, filename="Seth's CV", filepath="applications/gallery_1/seth@seth.com/").save(force_insert=True)


def load_forms_data():
    Forms(fid=1, first_name="seth", last_name="roger", street_address="101 Seth Roger Road", city="Blueburge", state="KY", email="seth@seth.com",phone_number="1234567890", website="seth.com", gallery=1, cv=1,personal_statement=1).save(force_insert=True)

def load_images_data():
    Images(iid=1, form=1, fullsize=1, thumbnail=1).save(force_insert=True)



if __name__ == "__main__":
    dummy_data()


