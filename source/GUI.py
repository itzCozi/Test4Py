# Displays the tkinter GUI window with each containg the recived questions, embedded content and answer choices from createSet(file)
# All i have to do is parse the list and display each sub-list as its own window and the user can send inputs to change said window.
try:
  import os, sys
  import tkinter as tk
except Exception as e:
  print(f'ERROR: [GUI] An error occurred when importing dependencies. \n{e}\n')
  sys.exit(1)
  
window = tk.Tk()
window.title('Test4Py')
window.geometry('850x650')
  

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
  # Declare widgets
  header = tk.Label(window, height=5, text ='Test4Py', bg='#2D2D30', fg='#E4E6EB')
  btn1 = tk.Button(window, text ='Join A Testing Session', command = join_session(), bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB')
  btn2 = tk.Button(window, text ='Start New Testing Session', command = new_session(), bg='#2D2D30', activebackground='#3E3E42', fg='#E4E6EB')
  blank = tk.Label(window, width=45, bg='#2D2D30')
  
  # Config widgets
  header.config(font=('monospace', 26))
  btn1.config(font=('monospace', 16))
  btn2.config(font=('monospace', 16))
  blank.config(font=('monospace', 26))
  
  # Pack widgets
  header.pack(anchor=tk.CENTER,fill=tk.X)
  btn1.pack(anchor=tk.CENTER,fill=tk.X)
  btn2.pack(anchor=tk.CENTER,fill=tk.X)
  # Spawn a blank box below the buttons
  blank.pack(anchor=tk.S, fill=tk.X)
  
  tk.mainloop()

def error_page():
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
  pass
def join_session():
  pass

#menu()
# REFERENCE: https://github.com/itzCozi/0swald-AI, THEME: Dark(3E3E42/2D2D30/E4E6EB)