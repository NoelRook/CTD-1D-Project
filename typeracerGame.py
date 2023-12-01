
import random
import time
import tkinter as tk
from tkinter import ttk
import json
enemynamelist = []
enemyhplist = []
enemyimagelist = []



class enemy:
    def __init__(self):
        f = open('Enemy.json')

        enemyjson = json.load(f)
        global enemyhplist
        global enemyimagelist
        global enemynamelist
        
        for i in enemyjson["enemy_details"]:
            enemynamelist.append(i["enemy_name"])
            enemyhplist.append(i["enemy_health"])
            enemyimagelist.append(i["enemy_pic_name"])
        print(enemyhplist)
        print(enemynamelist)
        print(enemyimagelist)
        

        
    
    def getrandomenemy(self):
        randomenemy= random.choice(enemynamelist)
        
        
        return randomenemy     
        



    def gethealth(self,enemyname):
        ###Everyword typed, check for hp###
        
        currenthealth = enemyhplist[enemynamelist.index(enemyname)]
        return currenthealth
        

    
    def getlevel(self):
        
        print("hello")

    def getimage(self,enemyname):
        randomenemyindex = enemynamelist.index(enemyname)
        randomenemyimage = enemyimagelist[randomenemyindex]
        return randomenemyimage
        
    
    def sethealth(self):
        

        print("hello")
def update_image(widget,container,image):
    widget.itemconfig(container,image=image)
    
def create_MainMenu_window():
    #START
    window.title("TEST ALPHA")  
    window.geometry("860x500")
    #Declare Widgits
    Blank = ttk.Label(window,text='',width=45)
    Blank2 = ttk.Label(window,text='',width=10)
    #Blank.grid(row=0,column=0) 
    #Blank2.grid(row=1,column=0)
    Title = tk.Label(window,text='Type Caster',font=("Comfortaa",40))
    PlayButton = tk.Button(window,text='Play',command =lambda:start_game() )
    #Grid Method
    Title.grid(row=0,column=1)
    PlayButton.grid(row = 1, column = 1)
    
def start_game():
    game_page()
def game_page():    
    enemy1 = enemykek.getrandomenemy()
    enemy2 = enemykek.getrandomenemy()
    img =tk.PhotoImage(file=enemykek.getimage(enemy1))
    window.img =img 
    img2 =tk.PhotoImage(file=enemykek.getimage(enemy2))
    #Declare Widgits
    settings_button = tk.Button(window, text = "Settings", width=30, borderwidth=2, relief="raised",command=lambda:update_image(Enemy_canvas,container,img2)) #Add setting menu, Currently randomise picture
    Enemy_canvas =tk.Canvas(width=200,height=300,bg='white')
    Blank = ttk.Label(window,text='',width=45)
    Blank2 = ttk.Label(window,text='',width=45)
    

    
    Enemy_info = ttk.Label(window,text='Name: {Name} Health: {health}'.format(health= enemykek.gethealth(enemy1),Name=enemykek.getrandomenemy())) #Call method get_health and get_name for format
    Entry = ttk.Label(window, text = "Name: {name}   Health: {health}".format(name="Player",health = 100), width=30, borderwidth=2, relief="raised") #Call method get_health and get_name for format
    #Grid Method
    Blank.grid(row=0,column=0) 
    Blank2.grid(row=0,column=3)
    Enemy_info.grid(row=1,column=1)
    Enemy_canvas.grid(row = 0, column = 1, sticky = tk.W, pady = 2)
    settings_button.grid(row = 1,column = 3)
    Entry.grid(row=3,column=1)
    #add image
    container = Enemy_canvas.create_image(0,0,image=img,anchor='nw') 

if __name__ == "__main__":
    enemykek = enemy()
    window = tk.Tk()
    create_MainMenu_window()
    #game_page(window)        
    tk.mainloop()
        