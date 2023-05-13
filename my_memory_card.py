#создай приложение для запоминания информ
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup 

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600,400)

lbl = QLabel('Какой национальности не существует?')
btv_otv = QPushButton('Ответить')
box = QGroupBox('Варианты ответа')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')
vlbox = QVBoxLayout()
hlbox1 = QHBoxLayout()
hlbox2 = QHBoxLayout()
hlbox1.addWidget(btn1)
hlbox1.addWidget(btn2)
hlbox2.addWidget(btn3)
hlbox2.addWidget(btn4)
vlbox.addLayout(hlbox1)
vlbox.addLayout(hlbox2)
box.setLayout(vlbox)
vlbox.addWidget(lbl)
vlbox.addWidget(btv_otv)
vlbox.addWidget(box)
vl = QVBoxLayout()#главная вертикальная линия
vl.addWidget(lbl)
vl.addWidget(box)


box2 = QGroupBox('Результаты теста')
lbl2 = QLabel('Правильный ответ')
lbl1 = QLabel('Правильно/Неправильно')
vl2 = QVBoxLayout()
box2.setLayout(vl2)
vl2.addWidget(lbl2)
vl2.addWidget(lbl1)

vl.addWidget(box2)
box2.hide()

vl.addWidget(btv_otv)
main_win.setLayout(vl)

rg = QButtonGroup()
rg.addButton(btn1)
rg.addButton(btn2)
rg.addButton(btn3)
rg.addButton(btn4)


def show_result():
    box.hide()
    box2.show()
    btv_otv.setText('Следующий вопрос')
def show_question():
    box2.hide()
    box.show()
    btv_otv.setText('Ответить')
    rg.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    rg.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]
def ask(q: Question):
    shuffle(answers)
    lbl.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl2.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1  
        print('Статистика')
        print('Всего вопросов -', main_win.total)
        print('Правильных ответов -', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')
    else:
        show_correct('Неверно!')
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')

def show_correct(res):
    lbl1.setText(res)
    show_result()

question_list = []
question_list.append(
Question('Государстеный язык Португалии',
'Португальский', 'Английский', 'Испанский', 'Русский'))
question_list.append(
Question('Какая легендарка лучше?',
'леон', 'ворон', 'сенди', 'амбер'))
question_list.append(
Question('Какая лучшая игра 2022?',
'Stray', 'Genshin impact', 'God of war', 'sonik'))
question_list.append(
Question('Сколько сейчас времени?',
'время обеда', '18:27', '12:54','17:48'))
question_list.append(
Question('Какая лучшая карточная игра?',
'Дурак', '11', 'Пасьянс', 'Косынка'))


main_win.cur_question = -1
def next_question():
    #q = question_list[main_win.cur_question]
    #main_win.cur_question += 1
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    #if main_win.cur_question >= len(question_list):
        #main_win.cur_question = 0
    #q = question_list[main_win.cur_question]

    print('Статистика')
    print('Всего вопросов -', main_win.total)
    print('Правильных ответов-', main_win.score)
    ask(q)
def click_OK():
    if btv_otv.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()
btv_otv.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0

next_question()




#ask('Государственный язык Бразилии', 'Бразильский', 'Португальский', 'Испанский', 'Итальянский')
#q = Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Русский')
#ask(q)
#btv_otv.clicked.connect(check_answer)



main_win.show()
app.exec_()

