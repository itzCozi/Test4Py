# Displays the tkinter GUI window
try:
  import os, sys
  import tkinter as tk
  from parser import set, createSet  # Convert file to parsed set [createSet(file)]
  from helper import crypto, sesh    # Decoding&Encoding the set [decode(file),encode(file)]
except Exception as e:
  print(f'ERROR: [GUI] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)

window = tk.Tk(className='Test4Py')
window.title('Test4Py')
window.geometry('850x650')
window.configure(bg='#2D2D30')
window.resizable(width=False, height=False)
# Disables window resizing (re-enable during test_loop)


class utility:

  def resetAll():
    for widget in window.winfo_children():
      widget.destroy()

  def openNewWindow(x, y, title):
    if not isinstance(x, int) or isinstance(y, int):
      print('ERROR: Both x and y need to be integers.')
      sys.exit(1)
    newWindow = tk.Toplevel(window)
    newWindow.title(title)
    newWindow.geometry(f'{x}x{y}')

class ScrollableFrame(tk.Frame):  # Must make the window spanwed here BIGGER
  # To make the test_loop scrollable for ease of use thanks to this guy
  # https://blog.teclado.com/tkinter-scrollable-frames/

  def __init__(self, container, *args, **kwargs):
    super().__init__(container, *args, **kwargs)
    canvas = tk.Canvas(self)
    scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
    self.scrollable_frame = tk.Frame(canvas)

    self.scrollable_frame.bind(
      '<Configure>',
      lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    canvas.create_window((0, 0), window=self.scrollable_frame, anchor=tk.CENTER)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def menu():
  utility.resetAll()
  # Declare widgets
  header = tk.Label(window, height=4, width=5, text='Test4Py', bg='#2D2D30', fg='#E4E6EB')
  btn1 = tk.Button(window, height=1, width=5, text='Join A Testing Session', command=join_session, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  btn2 = tk.Button(window, height=1, width=5, text='Start New Testing Session', command=new_session, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  btn3 = tk.Button(window, height=1, width=5, text='Exit Program', command=window.destroy, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')

  # Config widgets
  header.config(font=('monospace', 26))
  btn1.config(font=('monospace', 16))
  btn2.config(font=('monospace', 16))
  btn3.config(font=('monospace', 16))

  # Pack widgets
  header.pack(anchor=tk.CENTER, fill=tk.X)
  btn1.pack(anchor=tk.CENTER, fill=tk.X)
  btn2.pack(anchor=tk.CENTER, fill=tk.X)
  btn3.pack(anchor=tk.CENTER, fill=tk.X)

  tk.mainloop()


def error_page():
  utility.resetAll()
  # Config widgets
  header = tk.Label(window, height=5, text='Whoops...', bg='#2D2D30', fg='#E4E6EB')
  blurb = tk.Text(window, bg='#2D2D30', fg='#E4E6EB')

  # Insertion/config widgets
  header.config(font=('monospace', 20))
  blurb.config(font=('monospace', 16))
  blurb.insert(tk.END,'An unknown error was encountered, You can exit the application and try again in a little.')
  blurb.config(state='disabled')

  # Pack widgets
  header.pack(anchor=tk.CENTER, fill=tk.X)
  blurb.pack(anchor=tk.CENTER, fill=tk.Y)

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
      button.config(text='Join Session', command=join_session)

  def getSet():
    inp = inputTXT.get(1.0, 'end-1c')
    print(inp)
    if os.path.exists(inp):
      hash = crypto.encodeFile(inp)
      hashed.config(text=hash, state='normal')

  # Declare widgets
  inputPROMPT = tk.Label(window, text="Enter the set's path", bg='#2D2D30', fg='#E4E6EB')
  inputTXT = tk.Text(window, height=2, width=6, bg='#2D2D30', fg='#E4E6EB')
  hashed = tk.Button(window, height=4, width=6, command=copyHash, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  homeBTN = tk.Button(window, height=1, width=2, text='Back', command=menu, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  button = tk.Button(window, height=1, width=2, text='Submit', command=getSet, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')

  # Config widgets
  homeBTN.config(font=('monospace', 14))
  button.config(font=('monospace', 14))
  inputTXT.config(font=('monospace', 16))
  hashed.config(font=('monospace', 16), state='disabled')
  inputPROMPT.config(font=('monospace', 12), state='disabled')

  # Pack widgets
  inputPROMPT.pack(anchor=tk.W, fill=tk.X)
  inputTXT.pack(anchor=tk.CENTER, fill=tk.X)
  hashed.pack(anchor=tk.CENTER, fill=tk.X)
  button.pack(anchor=tk.CENTER, fill=tk.X)
  homeBTN.pack(anchor=tk.S, fill=tk.X)

  tk.mainloop()  # So now to join a session enter the copied string in join_session!


def join_session():
  # Decodes given string to bytes and write to set file/Start test
  utility.resetAll()
  
  def getCode():
    # Gets the b64 code and writes to set.txt
    inp = inputTXT.get(1.0, 'end-1c')
    print(inp)
    decoded_set = crypto.decode(inp)
    set.writeSet(decoded_set.encode('utf-8'))
    startBTN.config(text='Start', command=test_loop, height=2)
  
  # Declare widgets
  inputPROMPT = tk.Label(window, text='Enter the test code', bg='#2D2D30', fg='#E4E6EB')
  inputTXT = tk.Text(window, height=2, width=6, bg='#2D2D30', fg='#E4E6EB')
  homeBTN = tk.Button(window, height=1, width=2, text='Back', command=menu, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
  startBTN = tk.Button(window, height=1, width=2, text='Submit', command=getCode, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')

  # Config widgets
  inputTXT.config(font=('monospace', 16))
  homeBTN.config(font=('monospace', 14))
  startBTN.config(font=('monospace', 14))
  inputPROMPT.config(font=('monospace', 12), state='disabled')
  
  # Pack widgets
  inputPROMPT.pack(anchor=tk.W, fill=tk.X)
  inputTXT.pack(anchor=tk.CENTER, fill=tk.X)
  startBTN.pack(anchor=tk.CENTER, fill=tk.X)
  homeBTN.pack(anchor=tk.S, fill=tk.X)
  
  tk.mainloop()
  
  
def test_loop():  # This is going to suck to code...
  # Parses the set.txt file with createSet command then outputs the prompt, embed(if any)
  # and answer choices printed as a button for each item in the last item of the question list
  window.resizable(width=True, height=True)
  
  utility.resetAll()
  sesh.startSession()
  qSet = createSet()
  frame = ScrollableFrame(window)
  
  for question in qSet:
    def setAnswer(ans1):
      # Make this append to the sessions answers section and 
      # add a unclick feature by checking clicked buttons
      content = ans1.cget('text')
      answers.append(content[0])
      ans1.config(bg='#4ABA68')
      print(answers)
    
    sesh.updateQuestion()  # Update sesh file's question log
    answers = []                  # List of choosen answers (LETTERS)
    prompt = question[0]          # The inital question (displayed first)
    embed = question[1]           # Is equal to '' if no embed
    answer_choices = question[2]  # A list of answers
    
    question_prompt = tk.Label(frame.scrollable_frame, text=prompt, bg='#2D2D30', fg='#E4E6EB')
    if embed != '':  # I am pretty sure this will work
      embed_section = tk.Text(frame.scrollable_frame, bg='#2D2D30', fg='#E4E6EB')
      embed_section.insert(tk.END,embed)
      embed_section.config(font=('monospace', 14), state='disabled')
      
    question_prompt.config(font=('monospace', 14))
    question_prompt.pack(anchor=tk.N, fill=tk.X)
    if embed != '':
      embed_section.pack(anchor=tk.CENTER, fill=tk.X)
    
    for answer_choice in answer_choices:
      ans = tk.Button(frame.scrollable_frame, height=1, width=5, text=answer_choice, bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB') 
      ans.config(font=('monospace', 14), command=lambda m=ans: setAnswer(m))  # Lost 3hrs of my life here thanks (https://www.geeksforgeeks.org/how-to-check-which-button-was-clicked-in-tkinter/#)
      ans.pack(anchor=tk.CENTER, fill=tk.X)
    
    exitBTN = tk.Button(frame.scrollable_frame, height=1, width=4, text='EXIT', bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB', activeforeground='#E4E6EB')
    exitBTN.config(font=('monospace', 14), command=menu)
  
  frame.pack()


# REFERENCE: https://github.com/itzCozi/0swald-AI, THEME: Dark(3E3E42/2D2D30/E4E6EB)