"""Waits for the database to become available.
   Then, creates the needed database. Finally, creates the appropriate tables and adds any needed information."""

import os
import time
import MySQLdb
import subprocess


# constants
ENVIRONMENT_VARS = ['DB_USER', 'DB_PASS', 'DB_HOST', 'DB_NAME']
MAX_WAIT = 120
STEP = 10



def build_basic_database_tables():
  subprocess.run('python manage.py makemigrations --noinput', shell=True, check=True)
  subprocess.run('python manage.py migrate --noinput', shell=True, check=True)


def wait_for_database(max_wait_seconds: int, step_seconds: int):
  """Waits for the database to become available. If successful, returns a database connection."""
  total_time = 0
  
  while total_time < max_wait_seconds:
    try:
      connection = MySQLdb.connect(host=os.environ['DB_HOST'], user=os.environ['DB_USER'], passwd=os.environ['DB_PASS'])
      return connection
    except MySQLdb._exceptions.OperationalError:
      pass
    time.sleep(step_seconds)
    total_time += step_seconds
    
  raise ConnectionError('Cannot connect to database')
   
   
def check_environment_vars(environment: list):
  """Makes sure that the necessary environment variables exist."""
  for env_var in environment:
    if not (env_var in os.environ):
      raise EnvironmentError('Cannot find environment variable "' + env_var + '"')


def main():
  """Wait for the database to become available. Then, create the needed database."""

  check_environment_vars(ENVIRONMENT_VARS)

  connection = wait_for_database(MAX_WAIT, STEP)
  
  cursor = connection.cursor()
  
  cursor.execute('CREATE DATABASE IF NOT EXISTS ' + os.environ['DB_NAME'])
  
  build_basic_database_tables()
  
  cursor.execute('USE ' + os.environ['DB_NAME'])
  
  # add users named 'test1' 'test2' and 'test3' with a password of 'password'
  try:
    cursor.execute('INSERT INTO auth_user (password, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, email) VALUES (%s, 0, "test1", 0, 1, "2020-08-27 19:57:47.074317", "", "", "")', ("pbkdf2_sha256$216000$5xnigJtvZWit$8ILPoEFUu/RWmsB4SRhx0K6Ku6gY+jwXoOR1T++GCj0=",))
  except MySQLdb._exceptions.IntegrityError:
    pass
  try:
    cursor.execute('INSERT INTO auth_user (password, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, email) VALUES (%s, 0, "test2", 0, 1, "2020-08-27 19:57:47.074317", "", "", "")', ("pbkdf2_sha256$216000$5xnigJtvZWit$8ILPoEFUu/RWmsB4SRhx0K6Ku6gY+jwXoOR1T++GCj0=",))
  except MySQLdb._exceptions.IntegrityError:
    pass
  try:
    cursor.execute('INSERT INTO auth_user (password, is_superuser, username, is_staff, is_active, date_joined, first_name, last_name, email) VALUES (%s, 0, "test3", 0, 1, "2020-08-27 19:57:47.074317", "", "", "")', ("pbkdf2_sha256$216000$5xnigJtvZWit$8ILPoEFUu/RWmsB4SRhx0K6Ku6gY+jwXoOR1T++GCj0=",))
  except MySQLdb._exceptions.IntegrityError:
    pass
    
  connection.commit()
  
  cursor.close()
  
  connection.close()
    

if __name__ == '__main__':
  main()
