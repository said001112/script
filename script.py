import pyautogui
import math

R = 80 #сужает круг
(x, y) = pyautogui.size()
(X, Y) = pyautogui.position(x / 6, y / 6) #Позиция где будет крутиться курсор
pyautogui.moveTo(X + R,  Y)
for _ in iter(int, 1):
    pass
    for i in range(460):
        if i % 40 == 1: #"40"-скорость с которой будет двигаться курсор!
            pyautogui.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))

