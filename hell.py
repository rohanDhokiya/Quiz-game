import json 
import random


def data():
  return{ "normal":[{"Question":"who is the pm of india ?",
                    "Options":["(A)Narendra modi","(B)Asit kumar modi","(C)M.P.Shah","(D)dropadi murmur"],
                    "Answer":"A" },


                    {"Question":"Where is the capital of India?",
                    "Options": ["(A)Mumbai", "(B)Delhi", "(C)Chennai", "(D)Kolkata"],
                    "Answer": "B"},


                    {"Question":"who is the richest person of india ?",
                    "Options":["(A)vijay maliya","(B)Anand mahindra","(C)ratan tata","(D)mukesh ambani"],
                    "Answer":"D"}],
        
        
          "medium": [ {"Question": "Which is the largest state in India by area?",
                       "Options": ["(A) Maharashtra", "(B) Madhya Pradesh", "(C) Rajasthan", "(D) Uttar Pradesh"],
                       "Answer": "C"},
    
    
                      { "Question": "Who wrote the National Anthem of India?",
                       "Options": ["(A) Bankim Chandra Chatterjee", "(B) Rabindranath Tagore", "(C) Subhash Chandra Bose", "(D) Sarojini Naidu"],
                       "Answer": "B"},
    
    
                       {"Question": "Which is the hardest natural substance on Earth?",
                       "Options": ["(A) Gold", "(B) Iron", "(C) Diamond", "(D) Platinum"],
                       "Answer": "C"}],
          "hard":   [{"Question": "Who was the first Indian woman to become President of the UN General Assembly?",
                      "Options": ["(A) Sarojini Naidu", "(B) Vijaya Lakshmi Pandit", "(C) Indira Gandhi", "(D) Sucheta Kripalani"],
                      "Answer": "B"},


                     {"Question": "Which acid is naturally produced in the human stomach to help digestion?",
                      "Options": ["(A) Sulfuric Acid", "(B) Nitric Acid", "(C) Hydrochloric Acid", "(D) Acetic Acid"],
                      "Answer": "C"},


                     { "Question": "In which year was 'Project Tiger' launched in India to save tigers?",
                       "Options": ["(A) 1973", "(B) 1982", "(C) 1990", "(D) 1965"],
                       "Answer": "A"}]           
                       
        } 

quiz_data=data()


with open("data.json","w") as f:
       json.dump(quiz_data, f)

with open("data.json","r") as f:
       loaded_data =json.load(f)

Level = input("Choose Level (normal/medium/hard): ")
questions =  loaded_data[Level]
random.shuffle(questions)

score = 0
     
Lifeline =True

for q in questions:
     print(q["Question"])
     for option in q["Options"]:
       print(option) 
                    
     if q["Answer"]== h:
              print("True")
              score+=4
     elif user_choise:
          print(user_choise) 

     else:
              print(f"Wrong! The correct answer was{q['Answer']}")
              print("False")
              score-=1

     user_choise = input(" Type 'h' for enter  your answer or type'L' for Life line").upper()
     if user_choise == "L":
        if Lifeline:
         choise=int(input("enter 1 for 50-50 And 2 for skip the question"))
         if choise == 1:
            correct_letter = q["Answer"]
            wrong_options = [opt for opt in q["Options"] if not opt.startswith(f"({correct_letter})")]
            random_wrong = random.choice(wrong_options)
                
        
            for opt in q["Options"]:
                    if opt.startswith(f"({correct_letter})") or opt == random_wrong:
                        print(opt)
            h=(input("Enter your answer: ")).upper() 
            if q["Answer"]== h:
                print("True")
                score+=4 
            else:
                 print(f"Wrong! The correct answer was{q['Answer']}")
                 print("False")
                 score-=1

         elif choise ==2:
                 Lifeline = False
                 continue    
         Lifeline=False 
        else:
             print("Life line already used!")
             h=(input("Enter your answer: ")).upper()  
     else:
             h= user_choise        
             
if q["Answer"]== h:
              print("True")
              score+=4
else:
              print(f"Wrong! The correct answer was{q['Answer']}")
              print("False")
              score-=1


print(f"Your final score is {score}")



