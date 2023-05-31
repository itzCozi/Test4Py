# This file guides the user through starting a new testing session which contains of creating a question set inputting the path of said set and asking if they would like to start a session
# In a session the set file is encrypted and then that file (key at the end) would be decrypted by their Test4Py program assuming they choose the 'join test' option and entered the set path
import os, sys
from checks import prerun
from helper import functions, crypto