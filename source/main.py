# AFTER COMPILED THIS FILE LAUNCHS IN WINDOW VERSION MEANING IT IS NOT ABLE TO BE SEEN BY THE USER
try:
  import os, sys
  from checks import prerun
  from GUI import menu, error_page
  from helper import functions, crypto, sesh
except Exception as e:
  print(f'ERROR: [MAIN] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)


class files:
  base_dir = f'C:/Users/{os.getlogin()}/test4py'
  set_file = f'{base_dir}/set.txt'
  log_file = f'{base_dir}/logs.txt'
  sesh_file = f'{base_dir}/session.txt'


if __name__ == '__main__':
  try:
    prerun()
    menu()
  except Exception as e:
    errorMSG = f'\nERROR: Unkown error encountered - {functions.getTime()}\n{e}\n'
    with open(files.log_file, 'a') as log:
      log.write(errorMSG)
      log.close()
    print(errorMSG)
    error_page()
