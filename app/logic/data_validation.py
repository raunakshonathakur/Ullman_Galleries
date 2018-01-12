from app.models import *
from email_validator import validate_email, EmailNotValidError
from app.allImports import *

class DataValidation():
    def check_empty_list(self,the_list):
        if the_list == []:
            return None
        else:
            return the_list

    def check_empty_str(self,the_string):
        if the_string == '':
            return None
        else:
            return the_string

    def list_to_csv_str(self,the_list):
        check = self.check_empty_list(the_list)
        if not (check is None):
            csv_str = ",".join(the_list)
            return csv_str
        return None

    def csv_str_to_list(self,the_string):
        check = self.check_empty_str(the_string)
        if not (check is None):
            new_list = the_string.split(",")
            return new_list
        return None

    def create_staff_assigned_dict(self, forms, staff_assigned_obj):
        staff_assigned_dict = dict()
        for form in forms:
            staff=staff_assigned_obj.find_staff(form.FID)
            if staff == None:
                staff_assigned_dict[form.FID] = 'Unassigned'
            else:
                staff_assigned_dict[form.FID] = str(staff.username.firstname) + ' ' + str(staff.username.lastname)
        return staff_assigned_dict

    def create_requestors_dict(self,forms,requestor_obj):
        requestor_dict = dict()
        for form in forms:
            requestors=requestor_obj.select_users(form.FID)
            user_list = []
            for requestor in requestors:
                requestor_format = str(requestor.username.firstname) + ' ' + str(requestor.username.lastname)
                user_list.append(requestor_format)
            requestor_dict[form.FID] = user_list
        return requestor_dict

    def create_user_dict(self,forms,requestor_obj, username):
        requestor_dict = dict()
        for form in forms:
            requestors=requestor_obj.select_users(form.FID)
            user_list = []
            for requestor in requestors:
                if requestor.username.username == username:
                    requestor_format = str(requestor.username.firstname) + ' ' + str(requestor.username.lastname)
                    user_list.append(requestor_format)
                    requestor_dict[form.FID] = user_list
        return requestor_dict

    def create_filename_csv(self,current_csv,new_filename):
        filename_list = self.csv_str_to_list(str(current_csv))
        filename_list.append(new_filename)
        filename_csv_str = self.list_to_csv_str(filename_list)
        return filename_csv_str

    def validateEmail(self, email):
        try:
            v = validate_email(email)
            email = v["email"]
            print(email)
        except EmailNotValidError as e:
            print((str(e)))


