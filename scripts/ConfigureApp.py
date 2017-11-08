import yaml
import os, sys, glob
from peewee import *
import inspect
import hashlib
# http://flask.pocoo.org/snippets/54/
from werkzeug.security import generate_password_hash

path = os.getcwd()
test_dir = os.path.join(path,'app/config/')
if os.path.isdir(test_dir):
    sys.path.insert(0,path)
else:
    new_path = os.path.dirname(path)
    sys.path.insert(0,new_path)

class ConfigureApp():
    def __init__(self):
        self.db_choice = None
        self.db_name = None
        self.host = None
        self.username = None
        self.password = None
        self.secret_key = None
        self.conf = self.load_config('config.yaml')
        self.login = None
    
    def get_abs_path(self,relaitivePath):
        filepath = os.path.join(sys.path[0],relaitivePath)
        return filepath
    
    def get_model_filenames(self):
            filenames = []
            model_dir = 'app/models'
            for file in glob.glob(model_dir + "/*.py"):
                ignore_list = ['__init__.py','util.py']
                if (os.path.basename(file) not in ignore_list):
                    print "File: {0}".format(file)
                    filenames.append(os.path.splitext(os.path.basename(file))[0])
            print filenames
            return filenames
        
    def import_peewee_tables(self):
        model_filenames = self.get_model_filenames()    
        models_list = []
        for model in model_filenames:
            package = "app.models"
            peewee_table = getattr(__import__(package,fromlist=[model]), model)
            models_list.append(peewee_table)
        print models_list
        return models_list
        
    def load_config(self,filename):
        rel_path = 'app/config/' + filename 
        file_abs_path = self.get_abs_path(rel_path)
        with open(file_abs_path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg
        
    def get_db_choice(self):
        print '[1]: SQLite\n[2]: MySQL'
        while True:
            user_input = raw_input('What kind of database are you using? ')
            if (user_input.lower() == 'sqlite') or (user_input == '1'):
                self.db_choice = 'sqlite'
                return 'sqlite'
            elif (user_input.lower() == 'mysql') or (user_input == '2'):
                self.db_choice = 'mysql'
                return 'mysql'
            else:
                print '\nERROR: Invaild Response\tPlease type either the name of the software of its corresponding number. eg(Sqlite or 1)'
                
    def get_secret_key(self):
        print '\nFlask Session Cookies are cryptographically signed, which basically'
        print 'means that in order for a user to modify a session cookie they would'
        print 'need a secret key, which is a functionality required by this application.\n'
        while True:
            secret_key0 = raw_input('Therefore, what would you like the secret key to be for your application? ')
            secret_key1 = raw_input('Please type the secret key again: ')
            if secret_key0 == secret_key1:
                print "Thank you the secret key has been saved inside of secret.yaml, and can be changed at anypoint through modifing that file."
                return secret_key0
            else:
                print 'The two secret keys did not match.'
    
    def get_db_name(self):
        print 'Please exclude any path or extention details, eg( "data/" or ".sqlite").'
        while True:
            #TODO: check for /data and .sqlite
            db_name0 = raw_input('What would you like to name your {0} database. '.format(self.db_choice))
            db_name1 = raw_input('Please type the name of your database again: ')
            if db_name0 == db_name1:
                print "Your database name ({0}) will now be created.".format(db_name0)
                return db_name0
            else:
                print "The two database names did not match."
                
    def get_mysql_variables(self):
        self.host = raw_input('What is your host? ')
        self.username = raw_input('What should be your root username for msql? ')
        self.password = raw_input('What should be your root passwod for mysql? ')
        print ('\nIf you have entered any of these variables incorrectly, they can be changed in secret.yaml.')
        
    def edit_secret_yaml(self):
        #values_list should be ordered:
        #  [db_name,host,username,password,secret_key]
        if self.db_choice == 'sqlite':
            secret_data = {"db":{"db_name":self.db_name, "db_choice":self.db_choice}, "secret_key":self.secret_key, "login":self.login}
        else:
            secret_data = {'db':{"db_name":self.db_name, "db_choice":self.db_choice, "host":self.host, "username":self.username, "password":self.password}, "secret_key":self.secret_key,"login":self.login}
        #TODO: Figure out how not to hard code this
        path = os.path.join(sys.path[0],'app/config/secret.yaml')
        with open(path,'w') as outfile:
            yaml.dump(secret_data, outfile, default_flow_style=False)
                
    def get_login_choice(self):
        print 'Note: Password is a feature that is built into this applicaiton.'
        print 'It is a standard password and email authentication system.\n'
        print '[1]: Shibboleth\n[2]: Password'
        while True:
            user_input = raw_input('What kind of login are you using? ')
            if (user_input.lower() == 'shibboleth') or (user_input == '1'):
                self.login = 'shibboleth'
                return 'shibboleth'
            elif (user_input.lower() == 'password') or (user_input == '2'):
                self.db_choice = 'password'
                return 'password'
            else:
                print '\nERROR: Invaild Response\tPlease type either the name of the login system or its corresponding number. eg(Shibboleth or 1)'
    
    def create_sqlite_database(self):
        db_abs_path = self.get_abs_path(self.db_name)
        print db_abs_path
        def remove_db():
            try:
                os.remove(self.db_name)
                print("\t...Removing {0}.".format(db_abs_path))
            except OSError:
                print OSError
                pass
        
        def no_db_file():
            if os.path.isfile(self.db_name):
                print ("WARNING: Database ({0}) already exists in the system.".format(self.db_name))
                cont = None
                while True:
                    print ('Continuing this setup will DELETE your current sqlite file')
                    user_input = raw_input('Would you like to continue? (y/n): ')
                    if (user_input.lower() == 'yes') or (user_input.lower() == 'y'):
                        remove_db()
                        return True
                    elif (user_input.lower() == 'no') or (user_input.lower() == 'n'):
                        return False
                    else:
                        print '\nERROR: Invaild Response\tPlease respond with either yes/y or no/n.'
            return True
        
        def add_sqlite_dummy_prompt():
            user_input = raw_input('Would you like to add some default testing data to your db? (Y/N) ')
            while True:
                if (user_input.lower() == 'y') or (user_input.lower() == 'yes'):
                    return True
                elif (user_input.lower() == 'n') or (user_input.lower()=='no'):
                    return False
                else:
                    print '\n ERROR: Invaild Response\tPlease respond with either yes/y or no/n.'
        
        def add_sqlite_dummy_data():
            model_filenames = self.get_model_filenames()
            for model in model_filenames:
                model_path = "app"
                name = 'models'
                query_type = model+'Queries'
                #TODO: this one might just be based off naming convention
                package = getattr(__import__(model_path,fromlist=[name]), query_type)
                if query_type == 'UserQueries':
                    user = package()
                    bad_pw_hash = generate_password_hash("BadPass")
                    print '\n This is bad pass: ({})\n'.format(bad_pw_hash)
                    user.insert('adminUser',True,'Grace','Hopper')
                    user.insert('normalUser',False,'Alan','Turning')
                    user.insert('normalUser1', False, 'Ada', 'Lovelace')
                    user.insert('normalUser2', False, 'Larry', 'Page')
                elif query_type == 'FormQueries':
                   form = package()
                   form.insert('3/23/17','4/25/17','In Progress','(555)867-5309','Computer Science','We are contacting previous alumni in order to start up a program','.pdf','This is a 140 character limited description of what you are asking for','Computer Science Alumni','filename.txt','Thanks for all the hard work you do','Could you sign it Computer Science Department','alumni_trustees,non_alumni_trustees,staff_seed,council_members','mail,visit,phone,deceased','fake_example_email@gmail.com',True,None)
                elif query_type == 'RequestorQueries':
                    requestor = package()
                    requestor.insert('normalUser',1)
                elif query_type == 'StaffAssignedQueries':
                    staffAssigned = package()
                    staffAssigned.insert('normalUser',1)
                elif query_type == 'StaffNotesQueries':
                    staffNotes = package()
                    staffNotes.insert('normalUser',1,'The man who broke the Enigma','5/3/17')
                else:
                    pass
        
        def create_file():
            print 'Creating empty SQLite file: {0}'.format(db_abs_path)
            open(db_abs_path, 'a').close()
            return True
        
        def create_sqlite_tables():
            mainDB = SqliteDatabase(db_abs_path)
            class baseModel(Model):
                class Meta:
                    database = mainDB
            models = self.import_peewee_tables()    
            mainDB.create_tables(models,safe=True)
            
        check = no_db_file()
        if check:
            create_file()
            create_sqlite_tables()
        else:
            print 'Creation of the SQLite database has stopped.'
        dummy_prompt = add_sqlite_dummy_prompt()
        if dummy_prompt:
            add_sqlite_dummy_data()
        
                    
    def main(self):
        self.login        = self.get_login_choice()
        self.db_choice    = self.get_db_choice()
        self.db_name      = self.get_db_name()
        if self.db_choice == 'sqlite':
            self.db_name = 'data/' + self.db_name + '.sqlite'
        else:
            self.get_mysql_variables()
        self.secret_key = self.get_secret_key()
        self.edit_secret_yaml()
        if self.db_choice == 'sqlite':
            self.create_sqlite_database()
       
        
            
if __name__ == '__main__':
    create = ConfigureApp()
    create.main()
    
#TODO: 
# Find a way to create the mySQL Database
# Find a way to add dummy data to the mysql database