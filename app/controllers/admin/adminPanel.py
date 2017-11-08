from app.allImports import *
from app.logic.validation import *
from app.logic.data_validation import *


@app.route("/addAdmin", methods=["POST", "GET"])
def addAdmin():
    # Require Login
    user = require_login()
    if user.is_admin == False:
        abort(403)
    try: 
        # Create User Class object
        user_obj = UserQueries()
        # Get the form
        data = request.form
        
        newAdmin =  data['newAdmin']
        print "New admine here" + newAdmin
      
        admin = user_obj.change_admin_status(newAdmin, True)
        flash( admin.firstname + " " + admin.lastname + " is now an administrator.")
      
      
    except Exception as e:
        print e
        flash("An error has occured")    
    
    return(redirect("/adminPanel"))

@app.route("/removeAdmin", methods=["POST", "GET"])
def removeAdmin():
    # Require Login
    user = require_login()
    
    user_obj = UserQueries()
    url = "/adminPanel"
    if user.is_admin == False:
        abort(403)
   
    try: 
        # # Create User Class object
        user_obj = UserQueries()
        # # Get the form
        data = request.form
        
      
        removeAdmin =  data['removeAdmin']
        admin = user_obj.change_admin_status(removeAdmin, False)
        flash( admin.firstname + " " + admin.lastname + " has been removed as an administrator.")
            
    except Exception as e:
        print e
        flash("An error has occured")  
    if user.username == removeAdmin:
        url = "/"
    else: 
        url = "/adminPanel"
        
    return(redirect(url))


@app.route('/adminPanel', methods=["GET","POST"])
def adminPanel ():
    # require login
    user = require_login()
    
    # Create A Class Object
    user_obj = UserQueries()
    
    if user.is_admin == False:
        abort(403)
        
        
    non_admins = user_obj.select_non_admins()
    admins = user_obj.select_admins()

    return render_template('views/adminPanel.html', 
                            user = user,
                            admins = admins,
                            non_admins = non_admins,
                            cfg=cfg
                            )
  
    