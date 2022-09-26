import json
"""
Reads a file with questions and builds and returns in-memory questions object
"""

def get_questions():
    f = open ("C:/Users/israe/Documents/JalaUniversity/PythonTraining/week3_day1/week3_day1/teams_attendance_app/src/questions/questions.json")
    my_data = json.load(f)
    f.close
    return my_data

