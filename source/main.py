# AFTER COMPILED THIS FILE LAUNCHS IN WINDOW VERSION MEANING IT IS NOT ABLE TO BE SEEN BY THE USER

# This file guides the user through starting a new testing session which contains of creating a question set inputting the path of said set and asking if they would like to start a session
# In a session the set file is encoded and then that file (key at the end) would be decrypted by their Test4Py program assuming they choose the 'join test' option and entered the set path
try:
  import os, sys
  from checks import prerun
  from GUI import menu, error_page
  from helper import functions, crypto
except Exception as e:
  print(f'ERROR: [MAIN] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)