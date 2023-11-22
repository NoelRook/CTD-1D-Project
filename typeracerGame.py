import tkinter as tk
import random
import time
import json
class TyperacerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typeracer Game")

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
        f = open('C:\\Users\\aungk\\Documents\\Python\\Json files\\Enemy.json')
        enemyjson = json.load(f)
        enemynamelist = []
        enemyhplist = []

        for i in enemyjson["enemy_details"]:
            enemynamelist.append(i["enemy_name"])
            enemyhplist.append(i["enemy_health"])
        print(enemynamelist)
        print(enemyhplist)
    
    def gethealth(self):
        ###Everyword typed, check for hp###

        print("hello")

    
    def getlevel(self):
        ###Get the level in order to determine the difficulty of the enemy###
        print("hello")

    def getimage(self):
        ###based on the inputed enemy, retrieve the image needed###

        print("hello")
    
    def sethealth(self):
        ###change the hp with every word typed###

        print("hello")

    

    
    

    


    


    




if __name__ == "__main__":
    root = tk.Tk()
    game = TyperacerGame(root)
    root.mainloop()



cek = enemy()

