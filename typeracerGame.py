
import random
import time
import tkinter as tk
from tkinter import ttk
import json

class enemy:
    def __init__(self):
        f = open('Enemy.json')

        enemyjson = json.load(f)
        self.enemynamelist = []
        self.enemyhplist = []
        self.enemyimagelist = []
        for i in enemyjson["enemy_details"]:
            self.enemynamelist.append(i["enemy_name"])
            self.enemyhplist.append(i["enemy_health"])
            self.enemyimagelist.append(i["enemy_pic_name"])
        print(self.enemynamelist)
        print(self.enemyhplist)
    
    def getrandomenemy(self):
        randomenemy= random.choice(self.enemynamelist)
        randomenemyindex = self.enemynamelist.index(randomenemy)
        randomenemyimage = "assets/images/"+self.enemyimagelist[randomenemyindex]
        image = tk.PhotoImage(file=randomenemyimage) 
        print(randomenemy)
        return randomenemyimage     
        



    def gethealth(self):
        ###Everyword typed, check for hp###

        print("chingchong")

    
    def getlevel(self):
        ###Get the level in order to determine the difficulty of the enemy###
        print("hello")

    def getimage(self):
        ###based on the inputed enemy, retrieve the image needed###
        return self.getrandomenemy()
        print("hello")
    
    def sethealth(self):
        ###change the hp with every word typed###

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
    img =tk.PhotoImage(file=enemykek.getimage())
    window.img =img 
    img2 =tk.PhotoImage(file=enemykek.getimage())
    #Declare Widgits
    settings_button = tk.Button(window, text = "Settings", width=30, borderwidth=2, relief="raised",command=lambda:update_image(Enemy_canvas,container,img2)) #Add setting menu, Currently randomise picture
    Enemy_canvas =tk.Canvas(width=200,height=300,bg='white')
    Blank = ttk.Label(window,text='',width=45)
    Blank2 = ttk.Label(window,text='',width=45)
    Enemy_info = ttk.Label(window,text='Name: {Name}      Health: {health}'.format(health= 30,Name='name')) #Call method get_health and get_name for format
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
        