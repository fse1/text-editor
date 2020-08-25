"""Waits for the database to become available.
   Then, creates the needed database. Finally, creates the appropriate tables and adds any needed information."""

import sys


# constants
ENVIRONMENT_VARS = ['DB_USER', 'DB_PASS', 'DB_HOST', 'DB_NAME']
MAX_WAIT = 
STEP = 


def wait_for_database(max_wait_seconds: int, step_seconds: int):
  """Waits for the database to become available."""
  total_time = 0
  
  while total_time < max_wait_seconds:
    
    total_time += step_seconds
   
   
def check_environment_vars(environment: list):
  """Makes sure that the necessary environment variables exist."""
  for env_var in environment:
    if not (env_var in os.environ):
      raise ValueError('Cannot find environment variable "' + env_var + '"')


def main():
  """Wait for the database to become available. Then, create the needed database table."""

  check_environment_vars(ENVIRONMENT_VARS)

  wait_for_database(MAX_WAIT, STEP)
    
    

if __name__ == '__main__':
  main()
