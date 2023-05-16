
from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QListWidget, QGroupBox, QButtonGroup)

class Vopros():
    def __init__(self, qust, r_answer, answ1, answ2, ansv3):
        self.qust = qust
        self.r_answer = r_answer
        self.wrong1 = answ1
        self.wrong2 = answ2
        self.wrong3 = ansv3

def showquestion():
    RadioGroupBox.show()
    AnswGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    otvet1.setChecked(False)
    otvet2.setChecked(False)
    otvet3.setChecked(False)
    otvet4.setChecked(False)
    RadioGroup.setExclusive(True)

    
def showresult():
    RadioGroupBox.hide()
    AnswGroupBox.show()
    button.setText('Следующий вопрос')

def clicc_OK():
    if button.text() == 'Ответить':
        chec_answer()
    else:
        next_question()
def show_correct(res):
    lb_Quest1.setText(res)
    showresult()
def chec_answer():
    global score
    global lose
    if spisok[0].isChecked():
        show_correct('Правильно')
        score += 1
    else:
        if spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
            show_correct('WRONG')
        lose += 1
    if len(question_list) == 0:
        print('Правильных ответоов:', score)
        print('Неправильных ответов:', lose)

def next_question():
    global d
    d = randint(0, len(question_list) - 1)
    q = question_list[d]
    ask(q)
    question_list.remove(question_list[d])
    
        
    



app  = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
RadioGroupBox = QGroupBox('Варианты ответов')
question = QLabel('вопрос')
button = QPushButton('Ответить')
otvet1 = QRadioButton('ответ1')
otvet2 = QRadioButton('ответ2')
otvet3 = QRadioButton('ответ3')
otvet4 = QRadioButton('ответ4')

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

spisok = [otvet1, otvet2, otvet3, otvet4]
def ask(q: Vopros):
    shuffle(spisok)
    spisok[0].setText(q.r_answer)
    spisok[1].setText(q.wrong1)
    spisok[2].setText(q.wrong2)
    spisok[3].setText(q.wrong3)
    question.setText(q.qust)
    lb_Quest2.setText(q.r_answer)
    showquestion()


layout_ans2.addWidget(otvet1)
layout_ans2.addWidget(otvet2)
layout_ans3.addWidget(otvet3)
layout_ans3.addWidget(otvet4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

AnswGroupBox = QGroupBox('результаты')
lb_Quest1 = QLabel('правильно/ неправильно')
lb_Quest2 = QLabel('правильноый ответ')
v_line = QVBoxLayout()
v_line.addWidget(lb_Quest1)
v_line.addWidget(lb_Quest2)

RadioGroupBox.setLayout(layout_ans1)
AnswGroupBox.hide()
AnswGroupBox.setLayout(v_line)

aaa = QVBoxLayout()
aaa.addWidget(question)
aaa.addWidget(RadioGroupBox)
aaa.addWidget(AnswGroupBox)
aaa.addWidget(button)

RadioGroup = QButtonGroup()
RadioGroup.addButton(otvet1)
RadioGroup.addButton(otvet2)
RadioGroup.addButton(otvet3)
RadioGroup.addButton(otvet4)

RadioGroup.setExclusive(False)
otvet1.setChecked(False)
otvet2.setChecked(False)
otvet3.setChecked(False)
otvet4.setChecked(False)
RadioGroup.setExclusive(True)



question_list = []
q1 = Vopros('Кто самый лучший герой в доте?', 'Phantom Assassin', 'Shadow Fiend', 'Ursa', 'Riki')
question_list.append(q1)
q2 = Vopros('Как меня зовут?', "Артур", 'Тимур', 'Антон', 'Паша')
question_list.append(q2)
q3 = Vopros('Как называется самое милое животное в мире?', 'Капибара', 'Крокодил', 'Бабуин', 'Лев')
question_list.append(q3)
q4 = ('Какое животное самое крупное на Земле?', 'Синий кит', 'Бегемот', 'Жираф', 'Анаконда')
question_list.append(q4)
q5 = Vopros('Ответ 2? (или нет)', 'Да', 'Нет', 'Не знаю', 'Возможно')
question_list.append(q5)
q6 = Vopros('Как называется животное, которое употребляет в пищу растения и мясо?', 'Всеядное животное', 'Травоядное', 'Плотоядное', 'не придумал')
question_list.append(q6)
q7 = Vopros('Какое сейчас время года?', 'Весна', 'Зима', 'Лето', 'Осень')
question_list.append(q7)
q8 = Vopros('Как отличить насекомое от паука?', 'Все вышеперечисленные факты', 'Он выглядит как паук', 'У насекомых могут быть крылья, у пауков они отсутствуют', 'У насекомых три части тела, у пауков – две')
question_list.append(q8)
q9 = Vopros('Чем утконос отличается от других млекопитающих?', 'Смешно ходит', 'Крякает, как утка', 'Откладывает яйца', 'Строит гнезда')
question_list.append(q9)
q10 = Vopros('Отгадай число', '4', '2', '1', '3')
question_list.append(q10)

main_win.cur_question = -1
d = 0
score = 0
lose = 0

button.clicked.connect(clicc_OK)
next_question()
main_win.setLayout(aaa)
main_win.show()
app.exec_()