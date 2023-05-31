# THIS FILE IS RAN FIRST
# Checks if all packages are working and ensure the programs directory exsists
import os, sys


class files:
  base_dir = f'C:/Users/{os.getlogin()}/test4py'
  set_file = f'{base_dir}/set.txt'
  log_file = f'{base_dir}/logs.txt'
  sesh_file = f'{base_dir}/session.txt'


def prerun():
  if not os.path.exists(files.base_dir):
    os.mkdir(files.base_dir)
  if not os.path.exists(files.set_file):
    open(files.set_file, 'x')
  if not os.path.exists(files.log_file):
    open(files.log_file, 'x')
  if not os.path.exists(files.sesh_file):
    open(files.sesh_file, 'x')
  else:
    with open(files.log_file, 'a') as log:
      log.write('Passed [CHECKS] successfully.')