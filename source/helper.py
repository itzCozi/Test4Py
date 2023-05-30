# OS: Windows10
# PY-VERSION: 3.11+
# GITHUB: https://github.com/itzCozi/Helper

try:
  import os, sys
  import signal
  import time
  import string
  import random
  from sys import platform
  from cryptography.fernet import Fernet
except ModuleNotFoundError:
  print('ERROR: [PACKAGES] An unknown package could not be imported.')
  sys.exit(1)
  

class functions:
  
  def genID():
    # Creates a unique ID
    lenght = 8
    buffer = random.randint(3, 6)
    alphabet = list(string.ascii_letters+string.digits+string.digits)
    ID = []

    for i in range(buffer):
      random.shuffle(alphabet)
    
    for num in range(lenght):
      char = random.choice(alphabet)
      ID.append(char)
    
    return ''.join(ID)

  def clear():
    # Clears the working console
    if 'win' in sys.platform:
      return os.system('cls')
    else:
      return os.system('clear')

  def processPath(process):
    # Returns the running processes path
    if '.exe' in process:
      process = process[:-4]
    try:
      out = os.popen(f'powershell (Get-Process {process}).Path').read()
      for line in out.splitlines():
        if os.path.exists(line):
          return line
    except Exception as e:
      print(f'ERROR: An unknown error was encountered. \n{e}\n')
      sys.exit(1)

  def getProcesses():
    # Outputs all running processes
    try:
      iterated = set()
      retlist = []
      output = os.popen('wmic process get description, processid').read()

      for line in output.splitlines():
        if '.exe' in line:
          index = line.find('.exe')
          item = line[index + 5:].replace(' ', '')
          itemobj = functions.getNAME(item)
          if itemobj and itemobj not in iterated:
            retlist.append(itemobj)
            iterated.add(itemobj)

      return retlist
    except Exception as e:
      print(f'ERROR: An unknown error was encountered. \n{e}\n')
      sys.exit(1)

  def getNAME(PID):
    # Gets a process name from PID
    output = os.popen(f'tasklist /svc /FI "PID eq {PID}"').read()
    for line in str(output).splitlines():
      if '.exe' in line:
        index = line.find('.exe')
        diffrence = line[0:index]
        retvalue = f'{diffrence}.exe'
        return retvalue

  def getPID(process):
    # Returns a process PID from name
    if '.exe' in process:
      process = process.replace('.exe', '')
    try:
      retlist = []
      output = os.popen(f'powershell Get-Process -Name {process}').read()
      for line in output.splitlines():
        if '  SI ' in line:
          index = line.find('  SI ')
        if '.' in line:
          diffrence = line[:index]
          proc_info = diffrence.split()[-1].replace(' ', '')
          retlist.append(proc_info)
      return retlist
    except Exception:
        print(f'ERROR: Cannot find process {process}.')
        sys.exit(1)

  def removeRunning(process):
    # Kills a running process and then deletes it
    if not '.exe' in process:
      process = f'{process}.exe'
    proc_path = functions.processPath(process)

    try:
      try:
        functions.killProcess(process)
      except:
        pass
      time.sleep(0.5)
      os.remove(proc_path)
    except Exception as e:
      print(f'ERROR: An unknown error was encountered. \n{e}\n')
      sys.exit(1)

  def getRunning():
    # Get all running processes
    try:
      iterated = set()
      retlist = []
      output = os.popen('wmic process get description, processid').read()
      for line in output.splitlines():
        if '.exe' in line:
          index = line.find('.exe')
          item = line[index + 5:].replace(' ', '')
          itemobj = functions.getNAME(item)
          if not itemobj in iterated:
            retlist.append(itemobj)
          else:
            continue
          iterated.add(itemobj)
        else:
          output = output.replace(line, '')

      for item in retlist:
        if item == None:
          retlist.remove(item)
        else:
          with open(vars.processdump, 'a') as out:
            out.write(f'{item}\n')
          out.close()

    except Exception as e:
      print(f'ERROR: An unknown error was encountered. \n{e}\n')
      sys.exit(1)

  def killProcess(name):
    # Ends given process
    if name.endswith('.exe'):
      name = name.replace('.exe', '')
    PIDlist = functions.getPID(name)
    if PIDlist == None:
      print('ERROR: Process/Child-processes cannot be located.')
      sys.exit(1)
    for PID in PIDlist:
      try:
        os.kill(int(PID), signal.SIGTERM)
      except Exception as e:
        print(f'ERROR: Process {name} cannot be located.')
        sys.exit(1)
        
  def getTime():
    out = os.popen('time /t').read()
    if 'PM' in out:
      index = out.find('PM')
    else:
      index = out.find('AM')
    time = out[:index]
    return time

  def easyLog(type, message, file):
    # TYPE: What type of log, example: [PACKAGES] Failed import of ...
    # MESSAGE: The desired message to display with the log.
    # FILE: A optional way to output logs to a file.
    time = functions.getTime()
    
    if not os.path.exists(file):
      print(f'ERROR: Could not find {file}.')
      sys.exit(1)

    try:
      with open(file, 'a') as log_file:
        log_file.write(f"\n[{type}] {message} - {time}\n")
        log_file.close()
    except Exception as e:
      print(f'ERROR: Could not open {file}.')
      sys.exit(1)
        

  def filterFile(file, word):
    # Search a file for given word and remove it
    if not os.path.exists(file):
      print(f'ERROR: Given file {file} cannot be found.')
      sys.exit(1)
    try:
      with open(file, 'r+') as Fin:
        content = Fin.read()
      if word in content:
        with open(file, 'w+') as Fout:
          write_item = content.replace(word, '')
          Fout.write(write_item)
      else:
        print(f'ERROR: {word} cannot be found in {file}.')
        sys.exit(1)
    except Exception as e:
      print(f'ERROR: An unknown error was encountered. \n{e}\n')
      sys.exit(1)


class crypto:

  def encrypt(file):
    # Encrypt the given file and return a key
    if not os.path.exists(file):
      print(f'ERROR: Could not find {file}.')
      sys.exit(1)

    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      original = Fin.read()
      Fin.close()
    encrypted = fernet.encrypt(original)

    with open(file, 'wb') as Fout:
      Fout.write(encrypted)
      Fout.close()
    return key

  def decrypt(file, key):
    # Decrypt an encrypted file with a key
    if not os.path.exists(file):
      print(f'ERROR: Could not find {file}.')
      sys.exit(1)

    fernet = Fernet(key)

    with open(file, 'rb') as Fin:
      encrypted = Fin.read()
      Fin.close()
    decrypted = fernet.decrypt(encrypted)

    with open(file, 'wb') as Fout:
      Fout.write(decrypted)
      Fout.close()


if __name__ == '__main__': # Sorry this looks ugly (looks like JS TBH)
  file_name = os.path.basename(__file__).split('/')[-1]
  file_name = file_name[:file_name.find('.')]
  print(f"\n------------------------------------------------------ \
  \nYOU MUST IMPORT THE '{functions.__name__}' CLASS FROM '{file_name}'. \
  \nEXAMPLE: from {file_name} import functions as lib \
  \n------------------------------------------------------\n")
  sys.exit(1)
  
if 'linux' in sys.platform:
  print(f"\n------------------------------------------------ \
  \nTHIS PROGRAM IS ONLY COMPATIBLE WITH WINDOWS. \
  \nSOME ISSUES MAY BE ENCOUNTERED, CONTINUE? \
  \n------------------------------------------------")
  user_input = input('(y/n)> ')
  if 'y' in user_input.lower():
    print('\nYIELDING...')
    sys.platform = 'yielded'
  if 'n' in user_input.lower():
    print('\nQUITTING...')
    sys.exit(1)