# Used to parse the question set file to create a usable list for the GUI
import os, sys
import random
import string


def searchList(INlist, target): 
  # Searches a list for a character or sequence
  if not isinstance(INlist, list):
    print('ERROR: INlist must be a list type variable.')
    sys.exit(1)
  
  for item in INlist:
    if target in item:
      index = INlist.index(item)
      return int(index)


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
    retlist = []

    for Qline in fcontent:
      if '::' in Qline:
        qStart = fcontent.index(Qline)
        fcontent.remove(Qline)
      if ';;' in Qline:
        qEnd = fcontent.index(Qline)
        fcontent.remove(Qline)

        questionOBJ = fcontent[qStart:qEnd]
        if questionOBJ not in questions:
          questions.append(questionOBJ)

    for item in questions:  # For every question in the list
      ticker = -1               # Counts up to 24 for each letter
      incorrect_answers = []    # A list of incorrect answers
      correct_answers = []
      allAnswers = []
      parsed_answers = []
      embedded = None
      for line in item:  # For each newline in the choosen item
        # Index: Returns the index of the item in a given list
        # Find: Returns index of the word in a string/line
        if '??' in line:
          questionIndex = line.find('??')
          question = line[questionIndex:].replace('??', '')
        if '__' in line:
          aStart = item.index(line)
        if '[' and ']' in line:
          embedded = True

          embedStart = line.find('[')
          embedEnd = line.find(']')
          embedded_path = line[embedStart:embedEnd] + ']'

      for Aline in item[aStart:]:  # For every line after the __ symbol
        if '!' == Aline[0]:
          incorrect_answers.append(Aline.replace('!', ''))
          allAnswers.append(Aline.replace('!', ''))
        elif '*' == Aline[0]:
          # We dont replace the asterisk because we need to 
          # idetify the correct answer later on
          correct_answers.append(Aline.replace('*', ''))
          allAnswers.append(Aline)

      for ans in allAnswers:  # Assign a uppercase letter to each choice
        ticker += 1
        letter = list(alphabet)[ticker]
        answer_choice = f'{letter}. {ans}'
        parsed_answers.append(answer_choice)

      split_answers = '\n'.join(parsed_answers)  # Cannot use \n in f-strings
      if embedded == True:  # If there is an embed in this question
        embedded_path = embedded_path.replace('[', '').replace(']', '')
        with open(embedded_path, 'r') as ef:
          embedded_content = ef.read()
          ef.close()
        parsed_question = f'{question} \
        \n{embedded_content} \
        \n{split_answers}'

      else:  # If there is not an embed
        parsed_question = f'{question} \
        \n{split_answers}'

      retlist.append(parsed_question.replace('  ', ''))
    return retlist
      
  def jumbleSet(set):
    # Shuffles the question set
    randnum = random.randint(2, 6)
    for i in range(randnum):
      random.shuffle(set)
    return set
  

def createSet(file):
  # Creates complete question set and returns it (self-explanitory)
  package = []
  for question in set.parseSet(file):
    qlist = question.splitlines()
    ans_index = int(searchList(qlist, 'A. '))
    
    prompt = qlist[0]
    embedded = qlist[1:ans_index]
    answer_choices = qlist[ans_index:]
    
    embedded = '\n'.join(embedded)
    
    bundle = [prompt, embedded, answer_choices]
    package.append(bundle)
  return package
