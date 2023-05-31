# Used to parse the question set to create a session set
import os, sys
import string

class set:
  # :: - Begin a new question
  # ;; - End current question
  # ?? - Writen before the question
  # [] - Embed a file in the question
  # ! - Symbolize incorrect answer
  # * - Correct answer choice
  # __ - Begin answer choice section

  def parseSet(file):
    # Makes the question set into a list
    if not os.path.exists(file):
      print(f'ERROR: Could not find {file}.')
      sys.exit(1)
    
    with open(file, 'r') as f:
      content = f.read()
    alphabet = string.ascii_uppercase
    answer_choice_count = -1
    incorrect_answers = []
    correct_answers = []
    allAnswers = []
    ticker = -1
    
    parsed_answers = []
    
    # This is a good start but it doesnt conslidate and parse question by question which it needs to 
    # in order to prevent overlaping answer choices and stuff.
    for Qline in content.splitlines():
      if '::' in Qline:
        qStart = content.find(Qline)
      if ';;' in Qline:
        qEnd = content.find(Qline)
    
    for line in content[qStart:qEnd].splitlines():
      if '??' in line:
        questionIndex = line.find('??')
        question = line[questionIndex:]
      if '__' in line:
        aStart = content.find(line)
      if '[' and ']' in line:
        if '[' in line:
          embedStart = line.find('[')
        if ']' in line:
          embedEnd = line.find(']')
        embedded_file = line[embedStart:embedEnd].replace('[', '').replace(']', '')
    
    for line in content[qStart:qEnd].splitlines():
      if '!' in line:
        incorrect_answers.append(line.replace('!', ''))
        allAnswers.append(line.replace('!', ''))
      elif '*' in line:
        correct_answers.append(line.replace('*', ''))
        allAnswers.append(line.replace('*', ''))
      answer_choice_count += 1
      
    for item in allAnswers:
      ticker += 1
      letter = list(alphabet)[ticker]
      answer_choice = f'{letter}. {item}'
      parsed_answers.append(answer_choice)
    
    #if '[' and ']' in content[qStart:questionIndex]:
    #  print('yea')

  def createSet():
    # Creates complete question set and returns it
    pass

  def jumbleSet():
    # Encrypts and shuffles the question set
    pass

set.parseSet('set.txt')