# THIS FILE IS RAN FIRST
# Checks if all packages are working and ensure the programs directory exsists
try: # Import all used dependencies to sniff out missing modules (should be installed by setup)
  import os, sys
  import signal
  import time
  import string
  import random
  import tkinter as tk
  from cryptography.fernet import Fernet
except Exception as e:
  print(f'ERROR: [CHECKS] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)


class files:
  base_dir = f'C:/Users/{os.getlogin()}/test4py'
  set_file = f'{base_dir}/set.txt'
  log_file = f'{base_dir}/logs.txt'
  sesh_file = f'{base_dir}/session.txt'


def prerun():
  if not os.path.exists(files.base_dir):
    os.mkdir(files.base_dir)
  if not os.path.exists(files.set_file):
    open(files.set_file, 'w')
  if not os.path.exists(files.log_file):
    open(files.log_file, 'w')
  if not os.path.exists(files.sesh_file):
    open(files.sesh_file, 'w')
  