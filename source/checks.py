# THIS FILE IS RAN FIRST
# Checks if all packages are working ensure the programs directory exsists
import os, sys


class files:
  base_dir = f'C:/Users/{os.getlogin()}/Program Files/test4py'
  question_set = f'{base_dir}/set.txt'
  log_file = f'{base_dir}/logs.txt'
  sesh_file = f'{base_dir}/session.txt'


def prerun():
  if not os.path.exists(files.base_dir):
    os.mkdir(base_dir)

