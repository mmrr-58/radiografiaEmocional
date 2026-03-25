import sqlite3

con = sqlite3.connect("radiografiaEmocional.db")
cursor = con.cursor()

# Add new question to questions table
def createQuestion(question_category, question_frequency, question, type):
    cursor.execute("""INSERT INTO questions (
                   Question_category, 
                   Question_id, 
                   Question_frequency,
                   Question,
                   Answer_type)
                   VALUES (?,?,?,?,?);
                   """, (question_category, 
                         createQuestionID(question_category),  
                         question_frequency,
                         question,
                         type))
    con.commit()

def createQuestionID(category):
    cursor.execute("""SELECT Question_category FROM questions 
                   WHERE Question_category = ?;""", (category,) )
    items = cursor.fetchall()

    if len(items) > 0: 
        return category + str(len(items)+1)
    else:
        return category + '1'

# Send questions that need to be answered
def sendQuestions(frequency):
    cursor.execute("""SELECT Question_id, Question , Answer_type FROM questions
                   WHERE Question_frequency = ?;""", (frequency,))
    questions = cursor.fetchall()
    return questions


# Add responses to answers table
def recordAnswers(answers):
    rows = []
    response = getResponseNumber()
    for question_id, value in answers.items():
        rows.append((response, question_id, value))
    cursor.executemany("""INSERT INTO answers(
                Response,
                Question_id,
                Value)
                VALUES (?,?,?);""", (rows))
    con.commit()

def getResponseNumber():
    cursor.execute("""SELECT * FROM answers ORDER BY Response DESC LIMIT 1""")
    previous_response = cursor.fetchone()
    if previous_response is None:
        return 1
    else:
        return int(previous_response[0]) + 1 

# Create a table "questions" 
cursor.execute("""CREATE TABLE IF NOT EXISTS questions(
               Question_category TEXT NOT NULL,
               Question_id TEXT NOT NULL,
               Question_frequency TEXT NOT NULL,
               Question TEXT NOT NULL,
               Answer_type TEXT NOT NULL
               );""")

# Create a table "answers"
cursor.execute("""CREATE TABLE IF NOT EXISTS answers(
               Response INTEGER,
               Question_id TEXT,
               Value TEXT,
               Date DATETIME DEFAULT CURRENT_TIMESTAMP
               );""")