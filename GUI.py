
import random
import time
import tkinter as tk
from tkinter import font
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
        image = tk.PhotoImage(file="assets/images/GayMam.png") 
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
    
    Frame = ttk.Frame(window)
    #START
    window.title("TEST ALPHA")  
    #Declare Widgits
    Blank = ttk.Label(Frame,text='',width=45)
    Blank2 = ttk.Label(Frame,text='',width=10)

    Title = tk.Label(Frame,text='Type Caster',font=("Comfortaa",40))
    PlayButton = tk.Button(Frame,text='Play',command =lambda:start_game() )
    #Grid Method
    Title.grid(row=0,column=1)
    PlayButton.grid(row = 1, column = 1)
    Frame.grid(row=0,column=0)
    #Blank.grid(row=0,column=0) 
    #Blank2.grid(row=1,column=0)
def start_game():

    game_page()

def game_page():    
    style =ttk.Style()
    Font =font.Font(family = 'MS Gothic')
    style.configure('TFrame', background='black')
    style.configure('LabelStyle',background='black',font=Font)
    
    
    #Declare Widgits-----------------------------------------------
    Frame = ttk.Frame(window,style='TFrame')
    settings_button = tk.Button(Frame, text = "Settings", width=30, borderwidth=2, relief="raised",command=lambda:update_image(Enemy_canvas,container,img2)) #Add setting menu, Currently randomise picture
    Enemy_canvas =tk.Canvas(Frame,width=200,height=300,bg='black')
    Blank = ttk.Label(Frame,text='',width=45)
    Blank2 = ttk.Label(Frame,text='',width=45)
    Enemy_info = ttk.Label(Frame,text='Name: {Name}      Health: {health}'.format(health= 30,Name='name')) #Call method get_health and get_name for format
    Player_info = ttk.Label(Frame, text = "Name: {name}   Health: {health}".format(name="Player",health = 100), width=30, borderwidth=2, relief="raised") #Call method get_health and get_name for format
    
    #Grid Method-----------------------------------------------
    Blank.grid(row=0,column=0) 
    Blank2.grid(row=0,column=3)
    Enemy_info.grid(row=1,column=1)
    Enemy_canvas.grid(row = 0, column = 1, sticky = tk.W, pady = 2)
    settings_button.grid(row = 1,column = 3)
    Player_info.grid(row=3,column=1)

    Frame.grid(row=0,column=0, sticky=(tk.W,tk.E,tk.N,tk.S))
    #add image
    img =tk.PhotoImage(file="assets/images/GayMam.png")
    Frame.img =img 
    img2 =tk.PhotoImage(file=enemykek.getimage())
    container = Enemy_canvas.create_image(0,0,image=img,anchor='nw') 




if __name__ == "__main__":
    enemykek = enemy()
    window = tk.Tk()
    create_MainMenu_window()
    #game_page(window)        
    tk.mainloop()
        