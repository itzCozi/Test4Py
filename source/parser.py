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
    fcontent = content.splitlines()
    alphabet = string.ascii_uppercase

    questions = []

    answer_choice_count = -1
    incorrect_answers = []
    correct_answers = []
    allAnswers = []
    
    parsed_answers = []
    parsed_questions = []
    
    # This is a good start but it doesnt conslidate and parse question by question which it needs to 
    # in order to prevent overlaping answer choices and stuff.
    for Qline in content.splitlines():
      # fcontent: The contents of the file split by newlines
      if '::' in Qline:
        qStart = fcontent.index(Qline)
      if ';;' in Qline:
        qEnd = fcontent.index(Qline)
        questionOBJ = fcontent[qStart:qEnd]
        questions.append(questionOBJ)
    
    for item in questions: # For every question in the list
      ticker = -1 # Reset the ticker so the letters start from A
      for line in item: # For each newline in the choosen item
        # Index: Returns the index of the item in a given list
        # Find: Returns index of the word in a string/line
        if '??' in line:
          questionIndex = line.find('??')
          question = line[questionIndex:]
        if '__' in line:
          aStart = item.index(line)
        if '[' and ']' in line:
          if '[' in line:
            embedStart = line.find('[')
          if ']' in line:
            embedEnd = line.find(']')
          embedded_file = line[embedStart:embedEnd].replace('[', '').replace(']', '')
    
      for Aline in item[aStart:]: # For every line after the __ symbol
        if '!' in Aline:
          incorrect_answers.append(Aline.replace('!', ''))
          allAnswers.append(Aline.replace('!', ''))
        elif '*' in Aline:
          correct_answers.append(Aline.replace('*', ''))
          allAnswers.append(Aline.replace('*', ''))
        answer_choice_count += 1
      
      for ans in allAnswers: # Assign a uppercase letter to each choice
        ticker += 1
        letter = list(alphabet)[ticker]
        answer_choice = f'{letter}. {ans}'
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