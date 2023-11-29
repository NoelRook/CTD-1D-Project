
import random
import time
import tkinter as tk
from tkinter import ttk
import json
class TyperacerGame(object):
    
    def __init__(self, root):
        self.root = root
        self.root.title("Typeracer Game")
        obj = enemy()
        obj.getrandomenemy()


        self.words = ["python", "programming", "challenge", "typeracer", "keyboard", "developer", "coding", "practice", "speed", "game"]
        self.current_word = ""
        self.user_input = ""
        self.score = 0
        self.time_start = 0
        self.timer_running = False

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=30)

        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_input)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 18))
        self.score_label.pack()
        self.timer_label = tk.Label(root,text="this is timer")
        self.timer_label.pack()
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)
        
        





    def start_game(self):
        self.score = 0
        self.update_score()
        self.start_new_word()
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.timer_running = True
        self.time_start = time.time()
        self.update_timer()
        enemykek.getrandomenemy()
        
        

        

    def update_score(self):
        self.score_label.config(text="Score: {}".format(self.score))

    def start_new_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)

    def check_input(self, event):
        if self.timer_running:
            self.user_input = self.entry.get().strip()
            if self.user_input == self.current_word:
                self.score += 1
                self.update_score()
                self.start_new_word()
                self.entry.delete(0, tk.END)
                

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.time_start)           
            self.root.title("Typeracer Game - Time: {}s".format(elapsed_time))
            self.root.after(1000, self.update_timer)
            if elapsed_time >= 30:
                self.timer_running = False
                self.root.title("Typeracer Game - Time's up!")
                self.entry.delete(0, tk.END)
                self.entry.unbind("<Return>")
                self.start_button.config(state=tk.NORMAL)
        
class enemy:
    def __init__(self):
        f = open('C:\\Users\\aungk\\Documents\\Python\\CTD-1D-Project\\Enemy.json')

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
        randomenemyimage = self.enemyimagelist[randomenemyindex]
        image = tk.PhotoImage(file=randomenemyimage)      
        



    def gethealth(self):
        ###Everyword typed, check for hp###

        print("chingchong")

    
    def getlevel(self):
        ###Get the level in order to determine the difficulty of the enemy###
        print("hello")

    def getimage(self):
        ###based on the inputed enemy, retrieve the image needed###

        print("hello")
    
    def sethealth(self):
        ###change the hp with every word typed###

        print("hello")
    def update_image(widget,container,image):
        widget.itemconfig(container,image=image)


if __name__ == "__main__":
    enemykek = enemy()
    
    

    window = tk.Tk()
    window.title("TEST ALPHA")  
    window.geometry("860x500")
    #update image Function

        
    #create image variable
    img1 =tk.PhotoImage(file="FIshMAn.png")
    img2 = tk.PhotoImage(file='GayMam.png')

    Enemy_image = tk.Label(window, image =img1, width=30,height = 20)
    cavas =tk.Canvas(width=200,height=300,bg='black')

    # Declare Widgits
    settings_button = tk.Button(window, text = "Settings", width=30, borderwidth=2, relief="raised",command=lambda:update_image(cavas,container,img2))

    Blank = tk.Label(window,text='',width=45)

    Blank2 = tk.Label(window,text='',width=45)
    Enemy_info = tk.lable()

    Entry = ttk.Label(window, text = "Name:{name}   Health:{health}".format(), width=30, borderwidth=2, relief="raised")

    #Grid methods
    Blank.grid(row=0,column=0) 
    Blank2.grid(row=0,column=3)

    cavas.grid(row = 0, column = 1, sticky = tk.W, pady = 2)


    settings_button.grid(row = 1,column = 3)

    Entry.grid(row=3,column=1) 


    #add image
    container = cavas.create_image(0,0,image=img1,anchor='nw')


    tk.mainloop()
        
    
    




