import pgzrun

TITLE = "Quiz Guessr!"
WIDTH = 870
HEIGHT = 650

marque_box = Rect(0,10,880,80)
question_box = Rect(20,100,650,150)
timer_box = Rect(700,100,150,150)
skip_box = Rect(700,270,150,330)
answer_box1 = Rect(20,270,300,150)
answer_box2 = Rect(370,270,300,150)
answer_box3 = Rect(20,450,300,150)
answer_box4 = Rect(370,450,300,150)

score = 0
time_left = 10
question_file = "questions.txt"
is_game_over = False
is_game_complete = False
marque_message = ""

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
questions = []
question_count = 0
question_index = 0


def draw():
    global marque_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marque_box, "red")
    screen.draw.filled_rect(question_box, "blue")
    screen.draw.filled_rect(timer_box, "green")
    screen.draw.filled_rect(skip_box, "purple")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "orange")
        #Part 2
        
    marque_message = "Welcome to Quiz Guessr..."+f"Q: {question_count} of 11" 
    screen.draw.textbox(marque_message, marque_box, color = "black")
    screen.draw.textbox(str(time_left), timer_box, color = "brown", shadow = (0.5, 0.5), scolor = "grey")
    screen.draw.textbox("Skip", skip_box, color = "orange", angle = -90)
    
    screen.draw.textbox(question[0].strip(), question_box, color = "red")
    for answer in answer_boxes:
        screen.draw.textbox(question[index], color = "purple")
        index = index + 1

        #Part 3
def move_marque():
    marque.x = marque.x -2
    if marque_box.right < 0:
        marque_box.left = WIDTH

def update():
    move_marque()

def read_question_file():
    global questions, question_count
    q_file = open(question_file, "r")
    for question in q_file:
        questions.append(question)
        question_count = question_count +1
        q_file.close()

def read_next_question():
    global question_index
    question_index = question_index +1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
    if skip_box.collidepoint(pos):
        skip()

def correct_answer():
    global score, question, time_left, questions
    score = score +1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over
    message = f"Game Over!\n You Got {score} Questions Correct!"
    question = [message, "-","-","-","-",5]
    time_left = 0
    is_game_over = True

def skip():
    global question, time_left
    if question and not is_game_over:
        question = read_next_question
    else:
        game_over()

read_next_question()
question = read_next_question()

clock.schedule_interval(update_time_left,1)

def update_time_left():
    global time_left
    if time_left:
        time_left - 1
    else:
        game_over()



pgzrun.go()
