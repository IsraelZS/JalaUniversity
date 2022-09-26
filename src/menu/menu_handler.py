from questions.questions_processor import get_questions



def print_questions(questions):
    [  print(index, value, sep=". ") for index, value in questions.items()]

def validate_input(input):
    return not input in ["Quit", "Q", "q", "quit"]
  
def validate_question_number(input, keys):
    return input.isdigit() and int(input) in keys
  
def handle_questions_menu():
    questions = []
    for question in get_questions():
        questions.append(question['question'])

    # list to dictionary
    questions = dict(enumerate(questions, 1))

    print()
    print_questions(questions)

    # while user does not enter a valid question  number or Quit or Q to exit then keep asking, else return
    user_input = input("Type a number, or Quit or Q to exit")
    while validate_input(user_input) and not validate_question_number(user_input, questions.keys()):
        user_input = input("Type a number, or Quit or Q to exit")
    return user_input

        ## break if user enters a valid question number
        # if user_input == 1 or user_input == 2:
        # if user_input in range(1, len(question) + 1):
        # if user_input.isdigit() and int(user_input) in questions.keys():
        #     break

    

def handle_question_input_data(selected_question):
    data = {}
    if validate_input(selected_question):
        placeholders = get_questions()[int(selected_question)-1]['placeholders']
        for value in placeholders:
            name = value["name"]
            user_input = input(f"Type {name} value, or Quit or Q to exit program")
            if not validate_input(user_input):
                break 
            data[name] = user_input
        print(data)    
    return data



