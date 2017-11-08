# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from app.models import *
from app.config import * #This import is for testing
from app.logic.absolute_path import *
from functools import wraps
from flask import request, redirect, url_for, flash, abort
import os, re

def getUsernameFromEnv():
  #TODO: Delete dummy circumstance before production
  env = request.environ
  envK = "eppn"
  if envK in env:
    username = env[envK].split("@")[0].split('/')[-1].lower()
    add_user(env, username)
    return username  
  else:
    cfg = get_cfg()
    return cfg['user']['tmp']
  
def doesUserHaveRole(role):
  #TODO: Delete dummy circumstance before production
  username = getUsernameFromEnv()
  try:
    user = UserQueries()
    user.select_single(username)
    if user:
      if role=='admin':
        if user.is_admin:
          return True
        else:
          return False
      else:
        return True
    else:
      return False
  except Exception as e:
    print e
    return False
    
def switchRoles(Role):
  userName = getUsernameFromEnv()
  query    = User.update(role=Role).where(User.username==userName)
  query.execute()
  return True
  
      
# https://realpython.com/blog/python/primer-on-python-decorators/

def require_login ():
  username = getUsernameFromEnv()
  user = UserQueries()
  user = user.select_single(username)
  return user

      

def require_role (requiredRole):
  def decorator (fun):
    @wraps(fun)
    def decorated_fun (*args, **kwargs):
      if type(requiredRole) is tuple:
        for role in requiredRole:
          print(requiredRole)
          if doesUserHaveRole(role):
            print ("User has role: " + role)
            return fun(*args, **kwargs)
        abort(403)
      else:
        if doesUserHaveRole(requiredRole):
          print ('User has role: '+ requiredRole)
          return fun(*args, **kwargs)
        else:
          print ('User does not have role: ' + requiredRole)
          abort(403)
    return decorated_fun
  return decorator

def add_user(env,username):
  user = UserQueries()
  is_user = user.select_single(username)
  print is_user
  if is_user == False:
    description = request.environ['description'].lower()
    if description != 'student':
      try:
        newUser= user.insert(username, False, env['givenName'], env['sn'])
        return newUser
      except Exception as e:
        print e 
        abort(403)
    else:
      abort(404)


