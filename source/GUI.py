# Displays the tkinter GUI window with each containg the recived questions, embedded content and answer choices from createSet(file)
# All i have to do is parse the list and display each sub-list as its own window and the user can send inputs to change said window.
try:
  import os, sys
  import tkinter as tk
  from parser import createSet
except Exception as e:
  print(f'ERROR: [GUI] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)
# REFERENCE: https://github.com/itzCozi/0swald-AI, THEME: Dark(3E3E42/2D2D30/E4E6EB)