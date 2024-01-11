from tkinter import *
from random import randint
from tkinter import messagebox

def updateInfo():
    """
    This function updates the information displayed on the screen, including the
    current score, the top score, and the remaining attempts.

    Parameters:
        None

    Returns:
        None
    """
    scoreLabel["text"] = f"Ваши очки: {score}"
    topScoreLabel["text"] = f"Лучший результат: {topScore}"
    userTryLabel["text"] = f"Осталось попыток: {userTry}"

def saveTopScore():
    """
    Save the current top score to the score.dat file.

    Args:
        None

    Returns:
        None

    Raises:
        IOError: If the file cannot be opened for writing.
    """
    global topScore
    topScore = score

    try:
        fd = open("score.dat", "w", encoding="utf-8")
        fd.write(str(topScore))
        fd.close()
    except:
        messagebox.showinfo("Ошибка", "Не удалось сохранить счет")

def getWordFromFile():
    """
    This function reads a word list from a file and returns it as a list of words.

    Parameters:
        None

    Returns:
        list: A list of words read from the file.

    Raises:
        IOError: If the file cannot be opened.
    """
    ret = []

    try:
        fd = open("word.dat", "r", encoding="utf-8")
        
        for i in fd.readlines():
            l = l.replace("\n", "")
            ret.append(l)

        fd.close()
    except:
        print("Не удалось открыть файл word.dat")
        quit()
    
    return ret

def getTopScore():
    """
    This function reads the top score from the score.dat file and returns it as
    an integer.

    Parameters:
        None

    Returns:
        int: The top score from the score.dat file.

    Raises:
        IOError: If the file cannot be opened.
    """
    try:
        fd = open("score.dat", "r", encoding="utf-8")
        m = int(fd.readline())
        fd.close()
    except:
        m = 0
    
    return m

def startNewRound():
    """
    This function generates a new word to guess and displays it
    in the center of the screen as asterisks.
    """
    global wordStar, wordComp

    # generate a random word
    wordComp = "ИНТЕРНЕТ"

    # form a string of asterisks representing the word
    wordStar = "*" * len(wordComp)

    # set the text of the label to the asterisk string
    wordLabel.config(text=wordStar)

    # set the text of the score label to the asterisk string
    scoreLabel["text"] = wordStar

    # place the label in the center of the screen
    # based on its requested width
    wordLabel.place(x=WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y=50)
    updateInfo()

def compareWord(s1: str, s2: str) -> int:
    """
    This function compares two strings and returns the number of characters
    that match.

    Parameters:
    s1 (str): The first string to compare.
    s2 (str): The second string to compare.

    Returns:
    int: The number of characters that match between s1 and s2.    
    """
    res = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            res += 1

    print(f"Совпадений найдено: {res}")
    return res

def getWordStart(ch):
    """
    This function takes a single character as input and replaces all the
    characters in the word that are not equal to the input character with the
    same character in the word.

    Parameters:
    ch (str): The character to be compared with each character in the word.

     Returns:
    str: The modified word with all the characters that are not equal to the
    input character replaced with the input character.   
    """
    ret = ""

    for i in range(len(wordComp)):
        if wordComp[i] == ch:
            ret += ch
        else:
            ret += wordStar[i]

    return ret

# by clicking on the button with the letter
def pressLetter(n):
    """
    This function takes a single character as input and replaces all the
    characters in the word that are not equal to the input character with the
    same character in the word.    

    Parameters:
    n (int): The index of the button that was clicked.
    """
    global wordStar, score, userTry
    btn[n]["text"] = '.'
    btn[n]["state"] = "disabled"
    oldWordStar = wordStar
    wordStar = getWordStart(chr(st + n))
    count = compareWord(oldWordStar, wordStar)
    wordLabel["text"] = wordStar
    
    if count > 0:
        score += count * 5
    else:
        score -= 20
        if score < 0:
            score = 0
        userTry -= 1
        
    updateInfo()

#Creating a Window
root = Tk()

 # window variability option
root.resizable(False, False)

# title bar of the window
root.title("Угадай слово")

# adjust window geometry
WIDTH  = 810
HEIGHT = 320

# width and height of the monitor in pixels based on density
SCR_WIDTH  = root.winfo_screenwidth()
SCR_HEIGHT = root.winfo_screenheight()

# define window coordinates
POS_X = SCR_WIDTH // 2 - WIDTH // 2
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2

# set the window options
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# tag to output the word that the person guesses in the current round
# comma in font parameter means "apply system font"
wordLabel = Label(font=", 35")

# tag to display current points
scoreLabel = Label(font=", 12")

 # Record Scoring Mark
topScoreLabel = Label(font=", 12")

# label for remaining attempts
userTryLabel = Label(font=", 12")

# label in window
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# current glasses
score = 0

# game record
topScore = getTopScore()

# attempts
userTry = 10

# define button positions with letters
st = ord('А')
btn = []

for i in range(32):
    btn.append(Button(text=chr(st + i), width=2, font="consolas 15"))
    btn[i].place(x=215 + (i % 11) * 46, y=150 + i // 11 * 42)
    btn[i]["command"] = lambda x=i: pressLetter(x)

# define globally: "The Chosen Word"
wordComp = ""

# define globally: "word in stars"
wordStar = ""
startNewRound()
# start window
root.mainloop()
