import pathlib
import textwrap 

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=('AIzaSyCooKkQNIDffGOoHTCsImnJw4kogi_ULlU')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
def getquestions(sub, grade): 
  



  subject  = sub
  level = grade


  ask = "Give a ", (subject), "question of grade level ", (level), "that has a definite answer. Do not include the answer. Make sure it is different from the previouse question(s)"
  response = model.generate_content(ask)



  questions = (response.text)

  list_of_questions = questions.split('\n')



  # if '' in list_of_questions:
  #   list(filter(lambda a: a != '', list_of_questions))

  
  # for i in range (0, len(list_of_questions)):
  #   temp = list_of_questions[i]
  #   new_question = temp[3:len(temp)]
  #   #print(temp)
  #   list_of_questions[i] = new_question
  

  return (response.text)

def isright(q, answer):
    
  ask = "If a question on a test was '"  + q + "', and I answered '" + answer + "', would I be right? Yes or No"
  response = model.generate_content(ask)
  yayornay = (response.text)
  return yayornay


