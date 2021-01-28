#About The Code 
#okay this is was a fun to make lol, this is a spammer which you can use to spam anyone 
#you can use this code on any websites which uses gui like `whatsapp web, Discord(would also work on desktop version) and many more` 
#edit the `spam.txt`(right now it has the script of the movie frozen) with the text you wanna spam your friends/family with and enjoy
#now you can win all those spam wars on whatsapp super easily lol

import time, pyautogui
time.sleep(10)
f = open("spam.txt", 'r') #reads the texts to be spammed from the `.txt` file 
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press("enter")
    
