from tkinter import *
from random import randint

# при нажатии мышкой на кнопку
def pressLetter(n):
    print(f"{chr(st + n)}")

#создание окна
root = Tk()
# параметр изменяемости окна
root.resizable(False, False)
# заголовок окна
root.title("Угадай слово")
# настройка геометрии окна
WIDTH  = 810
HEIGHT = 320
# ширина и высота монитора в пикселях с учётом плотности
SCR_WIDTH  = root.winfo_screenwidth()
SCR_HEIGHT = root.winfo_screenheight()
# определяем координаты окна
POS_X = SCR_WIDTH // 2 - WIDTH // 2
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2
# задаём параметры окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
# метка для вывода слова, которое человек угадывает в текущем раунде
# запятая в параметре font означает "применить системный шрифт"
wordLabel = Label(font=", 35")
# метка для отображения текущих очков
scoreLabel = Label(font=", 12")
# метка для отображения рекордных очков
topScoreLabel = Label(font=", 12")
# метка для оставшихся попыток
userTryLabel = Label(font=", 12")
# устанавливаем метки в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)
# текущие очки
score = 0
# рекорд игры
topScore = 1000
# попытки
userTry = 10
# определяем позиции кнопок с буквами
st = ord('А')
btn = []

for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font="consolas 15"))
    btn[i].place(x=215 + (i % 11) * 46, y=150 + i // 11 * 42)
    btn[i]["command"] = lambda x=i: pressLetter(x)

# определяем глобально: "загаданное слово"
wordComp = ""
# определяем глобально: "слово в звёздочках"
wordStar = ""

# запускаем окно
root.mainloop()
