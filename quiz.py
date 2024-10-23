import pgzrun

TITLE = "Quiz Time!"
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

pgzrun.go()