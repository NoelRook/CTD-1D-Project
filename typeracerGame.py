
import random
import time
import tkinter as tk
from tkinter import font
from tkinter import ttk
import json
import os
import numpy as np




class Level:
    def __init__(self,lvl,special =False) :
        self.lvl_num = lvl
        self.list_of_enemies = []
        self.event = special
        f = open('Enemy.json')
        self.enemyjson = json.load(f)['enemy_details']

    def get_level(self):
        return self.lvl_num+1
    
    def get_list_of_enemies(self):
        return self.list_of_enemies

    def generate_lvl(self):
        if self.event == False:
            
            NumOfEnemies = int(2+abs(1+self.lvl_num)*.4)
            temp = random.sample(self.enemyjson,3)
            for i in temp:
                self.list_of_enemies.append(enemy(enemyname=i['enemy_name'],enemyhp=i['enemy_health'],enemyimage=i['enemy_pic_name'],damage= i['enemy_damage'],cooldown = 0)) # remeber to change damage and cooldown

            
            self.LvlUp()
            return self
        elif self.event== True:
            pass

    def LvlUp(self):
        temp =[]
        for i in self.list_of_enemies:

            temp.append(i.set_Lvl(self.lvl_num))
        self.list_of_enemies = temp
        
    def Choose_Enemy(self):
        return random.sample(self.list_of_enemies,1)[0]
    
   
class enemy:
    def __init__(self,enemyname,enemyhp,enemyimage, dialogue= '',EXP= 0,damage= 0,cooldown = 10):

        self.enemyhp =enemyhp
        self.enemyimage=enemyimage
        self.enemyname=enemyname
        self.EXP = 10  # Change later
        self.dialogue =dialogue
        self.damage =damage
        self.cooldown =10 # Change to cooldown later
        self.WordList=["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor","vagabond","knowing","hellish","ragged","brush"
             ,"nine","hideous","homeless","annoying","damaged","alcoholic","malicious","perpetual","wondeful","language","chemical","crazy","I was crazy once","They locked me","A rubber room","A rubber room with rats"]
    def gethealth(self):
        ###Everyword typed, check for hp###
        return self.enemyhp
    def getname(self):
        return self.enemyname   
    def getimage(self):
        return self.enemyimage
    def getdamage(self):
        return self.damage
    def getWordList(self):
        return self.WordList
    def sethealth(self,value):
        self.enemyhp += value

    def getcooldown(self):
        return self.cooldown
    def getEXP(self):
        return self.EXP
    
    def set_Lvl(self,lvl):
        self.enemyhp =  RoundtoNearest(self.enemyhp*(1+lvl*.1),5)
        self.damage =RoundtoNearest(self.damage*(1+lvl*.5),5)

        self.cooldown = int(self.cooldown- 2*np.log2((lvl+1)*.9))
        
        return self

class player(enemy):
    def __init__(self):
        self.enemyname ='Player'
        self.enemyhp = 100
        self.damage = 100
        self.Defence = 0
        self.EXP = 0
        self.Level = 1
        self.TimeBonus = 0
        self.DMG_Multi = 1.0
        self.DEF_Multi = 1.0
    def addEXP(self,value):
        self.EXP += value

    def LvlUp(self,root):
        self.EXP = 0
        self.Level+=1
        self.LvlUp_screen(root)
    def LvlUp_Helper(self,key,popup):
        if key =='increase_Dmg':
            self.damage += 1
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()

        elif key =='increase_HP':
            self.enemyhp += 10
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()
            Game.Player_info.config(text='  Name: {Name}'.format(Name=self.getname()).ljust(17)+'Health: {health}'.format(health=self.gethealth()).ljust(15))
        

        elif key =='increase_Def':
            self.Defence += 1
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()
            
        elif key =='increase_Time':
            self.TimeBonus += 1
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()
            
        elif key =='Mulitply_DMG':
            self.DMG_Multi += .1
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()
            
        elif key =='Mulitply_Def':
            self.DEF_Multi += .1
            popup.destroy()
            Game.NextEnemy()
            Game.update_timer()
            
    def LvlUp_screen(self,root):
        #---------------------------------------Logic--------------------------------------------
        ListofUpgrade = {'increase_Dmg':'Increae Damage by 1','increase_HP':'Increase Health by 10','increase_Def':"Reduce Damage taken by 1","increase_Time":"Increase timer on monster by 3","Mulitply_DMG":"Increase Damamge Mulitpyer by 10%","Mulitply_Def":"Increase Defence Mulitpyer by 10%"}
        Avaiable_options = random.sample(list(ListofUpgrade),3)
        
        #-----------------------------------Window Settings-------------------------------
        popup = tk.Toplevel()
        popup.title("LEVEL UP")
        
        Text = tk.Label(popup,text="LEVEL UP!",font=("Comfortaa",20))
        Text.grid(row=0,column=1)
        Option1_Text = tk.Label(popup,text=ListofUpgrade[Avaiable_options[0]]).grid(row=1,column=0)
        Option2_Text = tk.Label(popup,text=ListofUpgrade[Avaiable_options[1]]).grid(row=1,column=1)
        Option3_Text = tk.Label(popup,text=ListofUpgrade[Avaiable_options[2]]).grid(row=1,column=2)
        Option1_Button = ttk.Button(popup,text='LVL UP',command=lambda: self.LvlUp_Helper(Avaiable_options[0],popup)).grid(row=2,column=0)
        Option2_Button = ttk.Button(popup,text='LVL UP',command=lambda: self.LvlUp_Helper(Avaiable_options[1],popup)).grid(row=2,column=1)
        Option3_Button = ttk.Button(popup,text='LVL UP',command=lambda: self.LvlUp_Helper(Avaiable_options[2],popup)).grid(row=2,column=2)

        
def RoundtoNearest(value,base):
    return base*round(value/base)    

class TyperacerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Type Caster")
        self.current_word = ""
        self.user_input = ""
        self.score = 0
        self.time_start = 0
        self.Levels = []
        self.timer_running = False
        self.Current_Level = 0
        #Styles --------------------------------------------------------------------------------
        style =ttk.Style()
        Font =font.Font(family = 'MS Gothic')
        style.configure('TFrame', background='black')
        style.configure('TLabel',background='black',font=Font,foreground='white')
        #Main Menu--------------------------------------------------------------------------
        Frame = ttk.Frame(root,style='TFrame',width=600,height=300)
        Frame.grid_propagate(False)

        #START
        root.title("Type Caster")
        #Declare Widgits
        Title = ttk.Label(Frame,text='Type Caster',font=("Comfortaa",40),style='TLabel')
        PlayButton = ttk.Button(Frame,text='Play',command =lambda:self.start_game() )
        #Settings =ttk.Button(Frame,text='Settings',command =lambda:self.setting_window() )
        #Grid Method
        Frame.grid(row=0,column=0)
        Title.place(x=150,y=100)
        PlayButton.place(x=250, y = 200)
        #Settings.place(x=250, y = 250)
    def setting_window(self):
        pass
        
    def check_exp(self):
        if self.Player.EXP >= 10:
            return True
        return False
    def NextEnemy(self):
        self.Player_Stats.config(text=" Level: {L}\n Damage: {d}\n Defence: {Def}\n EXP: {exp}\n DMG Multiplier: {DMG_Multi}\n DEF Multipler: {DEF_Multi}".format(L=self.Player.Level,n=self.Player.getname(),h=self.Player.gethealth(),d=self.Player.getdamage(),Def= self.Player.Defence,exp = self.Player.EXP,DMG_Multi= self.Player.DMG_Multi,DEF_Multi=self.Player.DEF_Multi))    
        #Update Level list and Selected Enemy------------------------------------
        self.Current_Level +=1
        self.Levels.append(Level(self.Current_Level).generate_lvl())
        self.enemy = self.Levels[-1].Choose_Enemy()

        # Update GUI-----------------------------------------------
        img =tk.PhotoImage(file="assets/images/"+self.enemy.getimage())
        self.Frame.img =img 
        self.Enemy_canvas.itemconfig(self.container,image=img) 
        self.Enemy_info.config(text='  Name: {Name}'.format(Name=self.enemy.getname()).ljust(17)+'Health: {health}'.format(health=self.enemy.gethealth()).ljust(15),relief="solid")
        self.Enemy_stats.config(text=" Level: {L}\n Enemy: {n}\n Health: {h}\n Damage: {d}\n".format(L=self.Current_Level,n=self.enemy.getname(),h=self.enemy.gethealth(),d=self.enemy.getdamage()))

    def game_page(self): 

        #Declare Widgits-----------------------------------------------
        #FRAMES----------------------------------------------
        self.Frame = ttk.Frame(root,style='TFrame')
        Left_block = ttk.Frame(self.Frame,width=200,height=300,relief="solid")
        Mid_block= ttk.Frame(self.Frame,width=200,height=300,relief="solid")
        Right_block = ttk.Frame(self.Frame,width=200,height=300,relief="solid")
        # Right Frame----------------------------------------
        self.Enemy_stats = ttk.Label(Right_block,text=" Level: {L}\n Enemy: {n}\n Health: {h}\n Damage: {d}\n".format(L=self.Current_Level,n=self.enemy.getname(),h=self.enemy.gethealth(),d=self.enemy.getdamage()))    
        self.Enemy_stats.place(x=4,y=10)
        Right_block.grid_propagate (False) 
        self.PB = ttk.Progressbar(Right_block,orient='horizontal',mode='determinate',length=180)
        self.PB.place(x=10,y=200)
        # Left Frame -------------------------------------------------------------
        self.Player_Stats = ttk.Label(Left_block,text=" Level: {L}\n Damage: {d}\n Defence: {Def}\n EXP: {exp}\n DMG Multiplier: {DMG_Multi}\n DEF Multipler: {DEF_Multi}".format(L=self.Player.Level,n=self.Player.getname(),h=self.Player.gethealth(),d=self.Player.getdamage(),Def= self.Player.Defence,exp = self.Player.EXP,DMG_Multi= self.Player.DMG_Multi,DEF_Multi=self.Player.DEF_Multi))    
        self.Player_Stats.place(x=4,y=10)
        Right_block.grid_propagate (False) 
    

        #----------------------------------------------------------------------
        settings_button = tk.Button(self.Frame, text = "Next", width=10, borderwidth=2, relief="raised",command=lambda:self.NextEnemy()) #Add setting menu, Currently randomise picture
        self.Enemy_canvas =tk.Canvas(Mid_block,width=200,height=300,bg='black')
        self.Enemy_info = ttk.Label(self.Frame,text='  Name: {Name}'.format(Name=self.enemy.getname()).ljust(17)+'Health: {health}'.format(health=self.enemy.gethealth()).ljust(15),relief="solid") #Call method get_health and get_name for format
        self.Player_info = ttk.Label(self.Frame, text = '  Name: {Name}'.format(Name=self.Player.getname()).ljust(17)+'Health: {health}'.format(health=self.Player.gethealth()).ljust(15), borderwidth=2, relief="solid") #Call method get_health and get_name for format
        self.Word_box = ttk.Frame(self.Frame,width=200,height=45,relief="solid",padding=10)
        self.Entry = ttk.Entry(self.Frame,width=30)
        
        self.Word_request = ttk.Label(self.Word_box,text=random.choice(self.enemy.getWordList()))

        #Grid Method-----------------------------------------------
        Left_block.grid(row=0,column=0,padx=3,pady=5) 
        Right_block.grid(row=0,column=3,padx=3,pady=5)
        Mid_block.grid_propagate (False) 
        Mid_block.grid(row=0,column=1,padx=3,pady=5)
        self.Enemy_info.grid(row=1,column=1,pady=5)
        self.Enemy_canvas.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
        settings_button.grid(row = 1,column = 3)
        self.Player_info.grid(row=3,column=1,pady=5)
        self.Entry.grid(row=5,column=1,pady=20)
        self.Word_box.grid_propagate(False) 
        self.Word_box.grid(row=4,column=1,pady=5)
        self.Word_request.place(relx=0.5, rely=0.5, anchor="center")
        self.Frame.grid(row=0,column=0, sticky=(tk.W,tk.E,tk.N,tk.S))
        self.Entry.bind("<Return>", self.check_input)
        self.Entry.focus()
        #add image
        img =tk.PhotoImage(file="assets/images/"+self.enemy.getimage())
        self.Frame.img =img 
        self.container = self.Enemy_canvas.create_image(0,0,image=img,anchor='nw') 
        self.update_timer()
        
    def start_game(self):
        self.score = 0
        self.Player=player()
      #  self.update_score()
        self.Current_Level+=1
        self.timer_running = True
        self.time_start = time.time()   
        self.Levels.append(Level(self.Current_Level).generate_lvl())
        self.enemy = self.Levels[self.Current_Level-1].Choose_Enemy()

        #-------------------------------------------------------------------
        
        self.game_page()

    def start_new_word(self):
        self.Word_request.config(text =random.choice(self.enemy.getWordList()))
    def check_input(self, event=None):
        if self.timer_running:
            self.user_input = self.Entry.get().strip()
            if self.user_input == self.Word_request.cget('text'):
                self.start_new_word()
                self.deal_damage()
                self.Entry.delete(0, tk.END)
                self.score+=1

    def deal_damage_to_player(self,value):
        self.Player.sethealth(-int(((value-self.Player.Defence)*self.Player.DEF_Multi)))
        if self.Player.gethealth() <0: 
            self.timer_running = False
            self.Entry.delete(0, tk.END)
            self.Entry.unbind("<Return>")
            self.root.after_cancel(self.timer_queue)
            Lose_screen = tk.Toplevel(bg='black')
            Text = ttk.Label(Lose_screen,text=" You have Died\n Higest Level Reached: {level}\n Number of words typed: {num}".format(level = self.Current_Level,num = self.score))
            Text.grid(row=0,column=0)
            self.Frame.destroy()
            
        else:
            self.Player_info.config(text='  Name: {Name}'.format(Name=self.Player.getname()).ljust(17)+'Health: {health}'.format(health=self.Player.gethealth()).ljust(15))
        

    def update_timer(self):
        time_limit = self.enemy.getcooldown()+self.Player.TimeBonus
        if self.timer_running:
            elapsed_time = time.time() - self.time_start
            timepercent = int((elapsed_time/time_limit)*100)
            
            self.PB['value'] = timepercent
            if timepercent >=100:
                    self.PB['value'] = 0
                    self.time_start = time.time() 
                    self.deal_damage_to_player(self.enemy.getdamage())

        self.timer_queue =self.root.after(1000,lambda: self.update_timer())
    
    
    def deal_damage(self):
        self.enemy.sethealth(-int((self.Player.damage*self.Player.DMG_Multi)))
        if self.enemy.gethealth() >0:
            self.Enemy_info.config(text='  Name: {Name}'.format(Name=self.enemy.getname()).ljust(17)+'Health: {health}'.format(health=self.enemy.gethealth()).ljust(15))
        else:
            self.root.after_cancel(self.timer_queue)
            self.Player.addEXP(self.enemy.getEXP())
            if self.check_exp():
                self.Player.LvlUp(self.root)
                
                
            
            

Levels = []
if __name__ == "__main__":
    Current_Level = 1
    root = tk.Tk()
    Game = TyperacerGame(root)

    #game_page(root)        
    tk.mainloop()   
        