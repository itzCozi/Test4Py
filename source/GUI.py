# Displays the tkinter GUI window with each containg the recived questions, embedded content and answer choices from createSet(file)
# All i have to do is parse the list and display each sub-list as its own window and the user can send inputs to change said window.
try:
  import os, sys
  import tkinter as tk
  from parser import createSet  # Convert file to parsed set [createSet(file)]
  from helper import crypto     # Decoding&Encoding the set [decode(file),encode(file)]
except Exception as e:
  print(f'ERROR: [GUI] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)
  
window = tk.Tk()
window.title('Test4Py')
window.geometry('850x650')
window.resizable(width=False, height=False)
# Disables window resizing (re-enable during test_loop)  


class utility:
  def resetAll():
    # Reset everything
    for widget in window.winfo_children():
      widget.destroy()

  def openNewWindow(x, y, title):
    if not isinstance(x, int) or isinstance(y, int):
      print('ERROR: Both x and y need to be integers.')
      sys.exit(1)
    newWindow = tk.Toplevel(window)
    newWindow.title(title)
    newWindow.geometry(f'{x}x{y}')

def menu():
  utility.resetAll()
  # Declare widgets
  header = tk.Label(window, height=4, width=5, text='Test4Py', bg='#2D2D30', fg='#E4E6EB')
  btn1 = tk.Button(window, height=1, width=5, text='Join A Testing Session', command=join_session, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  btn2 = tk.Button(window, height=1, width=5, text='Start New Testing Session', command=new_session, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  btn3 = tk.Button(window, height=1, width=5, text='Exit Program', command=window.destroy, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  blank = tk.Label(window, height=20, width=5, bg='#2D2D30')
  
  # Config widgets
  header.config(font=('monospace', 26))
  btn1.config(font=('monospace', 16))
  btn2.config(font=('monospace', 16))
  btn3.config(font=('monospace', 16))
  blank.config(font=('monospace', 26))
  
  # Pack widgets
  header.pack(anchor=tk.CENTER,fill=tk.X)
  btn1.pack(anchor=tk.CENTER,fill=tk.X)
  btn2.pack(anchor=tk.CENTER,fill=tk.X)
  btn3.pack(anchor=tk.CENTER,fill=tk.X)
  # Spawn a blank box below the buttons
  blank.pack(anchor=tk.S, fill=tk.X)
  
  tk.mainloop()

def error_page():
  utility.resetAll()
  # Config widgets
  header = tk.Label(window, height=5, text ='Whoops...', bg='#2D2D30', fg='#E4E6EB')
  blurb = tk.Text(window, bg='#2D2D30', fg='#E4E6EB' )
  
  # Insertion/config widgets
  header.config(font=('monospace', 20))
  blurb.config(font=('monospace', 16))
  blurb.insert(tk.END, 'An unknown error was encountered, You can exit the application and try again in a little.')
  blurb.config(state='disabled')
  
  # Pack widgets
  header.pack(anchor=tk.CENTER,fill=tk.X)
  blurb.pack(anchor=tk.CENTER,fill=tk.Y)
  
  tk.mainloop()

def new_session():
  # Takes in a set file and encodes it from bytes to string
  utility.resetAll()
  def copyHash():
    btn_content = hashed.cget('text')
    if btn_content != '':
      window.clipboard_clear()
      window.clipboard_append(btn_content)
      hashed.config(text='Test Code Copied To Clipboard', state='disabled')
      button.config(text='Home', command=menu)
  
  def getSet():
    inp = inputTXT.get(1.0, 'end-1c')
    if os.path.exists(inp):
      hash = crypto.encode(inp)
      hashed.config(text=hash, state='normal')
    return inp

  inputPROMPT = tk.Label(window, text="Enter the set's path", bg='#2D2D30', fg='#E4E6EB')
  inputTXT = tk.Text(window, height=2, width=6, bg='#2D2D30', fg='#E4E6EB')
  hashed = tk.Button(window, height=4, width=6, command=copyHash, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  button = tk.Button(window, height=1, width=2, text='Submit', command=getSet, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  blank = tk.Label(window, height=20, width=50, bg='#2D2D30')
  
  button.config(font=('monospace', 14))
  inputTXT.config(font=('monospace', 16))
  hashed.config(font=('monospace', 16), state='disabled')
  inputPROMPT.config(font=('monospace', 12), state='disabled')
  blank.config(font=('monospace', 26), state='disabled')

  inputPROMPT.pack(anchor=tk.W,fill=tk.X)
  inputTXT.pack(anchor=tk.CENTER,fill=tk.X)
  hashed.pack(anchor=tk.CENTER,fill=tk.X)
  button.pack(anchor=tk.CENTER,fill=tk.X)
  blank.pack(anchor=tk.S, fill=tk.X)
  
  tk.mainloop() # So now to join a session enter the copied string in join_session!

def join_session():
  # Decodes given string to bytes and write to set file/Start test
  utility.resetAll()
  pass

def test_loop(set):
  # Takes in question set and parses the question, embeds and answer choices with each 
  # answer choice printed as a button for each item in the last item of the question list
  """ EXAMPLE QUESTION LIST
  [['Which choice accurately summarizes the text. ', 'THIS IS AN EMBEDDED \nFILE WITH TWO LINES ', ['A. The authour writes about their favorite food', 'B. *Our protagonist finds her husband in a mall', 'C. Liz invites a freind over for dinner', 'D. The narrator has a nice day in the park']]]
  """
  utility.resetAll()
  pass

# REFERENCE: https://github.com/itzCozi/0swald-AI, THEME: Dark(3E3E42/2D2D30/E4E6EB)