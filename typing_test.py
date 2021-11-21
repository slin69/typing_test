from tkinter import *
import random
import datetime
import math
root=Tk()
open("speed.txt","x")
class Gui:
    def __init__(self):
        #parts of a sentence
        self.subjects=["Jimmy,","Bobby,","Stefan,","Sam,"]
        self.verbs=[" ate "," peed "," danced "," played "]
        self.preposition=["on ","between ","over ","at "]
        self.predicate=["the floor.","dinner table.","blue car.","yard."]
        #////////////////////
        #defining ta.gs
        self.start_time=datetime.datetime.now().time()
        self.start_time.strftime('%H:%M:%S')
        self.sh=self.start_time.strftime("%H")
        self.sm=self.start_time.strftime("%M")
        self.ss=self.start_time.strftime("%S")
        self.wmp=None
        self.new=Button(root,text="new sentence",command=self.new)
        self.speed=Label(root, text=f"wmp: {self.wmp}")
        self.sentence=f"{random.choice(self.subjects)}{random.choice(self.verbs)}{random.choice(self.preposition)}{random.choice(self.predicate)}"
        self.string=Label(root,text=self.sentence)
        self.entry=Entry(root)
        self.fastest_string=self.max_num_in_file("speed.txt")
        self.fastest=Label(root,text=f"fastest wmp: {self.fastest_string}")
        #//////////////////
        # packing the tags
        root.geometry("400x400")
        self.string.pack()
        self.entry.pack()
        self.speed.pack()
        self.fastest.pack()
        self.new.pack()
        #//////////////////////////
        #key binding 
        root.bind("<Return>",self.check)
        root.bind("<KeyPress>",self.input)
        root.mainloop()
        #/////////////////////////
        #functions
    def input(self,event=None):
        now=datetime.datetime.now().time()
        hour=int(now.strftime("%H"))-int(self.sh)
        minute=int(now.strftime("%M"))-int(self.sm)
        seconds=int(now.strftime("%S"))-int(self.ss)
        time=abs(int(seconds+minute))
        print(f"time: {time}")
        textLength=self.entry.get()
        #print(f"final wmp: {(len(textLength)/5)/time*60}")
        self.wmp=f"wmp: {int((len(textLength)/5)/time*60)}"
        self.speed["text"]=self.wmp
    def max_num_in_file(self,filename):    
        """Returns the largest integer found in the file"""
        file=open(filename)
        maxs=0
        for line in file.readlines():
                num=int(line.split()[0])
                if maxs<num:
                    maxs=num
        return maxs

    def new(self):
        self.sentence=f"{random.choice(self.subjects)}{random.choice(self.verbs)}{random.choice(self.preposition)}{random.choice(self.predicate)}"
        self.string["text"]=self.sentence 
        self.start_time=datetime.datetime.now().time()
        self.start_time.strftime('%H:%M:%S')
        self.sh=self.start_time.strftime("%H")
        self.sm=self.start_time.strftime("%M")
        self.ss=self.start_time.strftime("%S") 
        self.entry.delete(0,END)  
    def check(self,event=None):
        if self.string.cget("text")==self.entry.get():
            self.sentence=f"{random.choice(self.subjects)}{random.choice(self.verbs)}{random.choice(self.preposition)}{random.choice(self.predicate)}"
            now=datetime.datetime.now().time()
            hour=int(now.strftime("%H"))-int(self.sh)
            minute=int(now.strftime("%M"))-int(self.sm)
            seconds=int(now.strftime("%S"))-int(self.ss)
            self.entry.delete(0,END)
            self.string["text"]=self.sentence
            time=abs(int(seconds+minute))
            textLength=self.string.cget("text")
            print(f"time: {time}")
            print(f"final wmp: {(len(textLength)/5)/time*60}")
            self.start_time=datetime.datetime.now().time()
            self.start_time.strftime('%H:%M:%S')
            self.sh=self.start_time.strftime("%H")
            self.sm=self.start_time.strftime("%M")
            self.ss=self.start_time.strftime("%S")
            with open("speed.txt","a") as f:
                #trial

                speed=int((len(textLength)/5)/time*60)
                f.write(f"{speed}\n")
                answer=self.max_num_in_file("speed.txt")
                print(answer)
                print(answer)
                f.close()
            self.fastest_string=self.max_num_in_file("speed.txt")
            self.fastest_string=self.max_num_in_file("speed.txt")
            self.fastest["text"]=f"fastest wmp: {self.fastest_string}"
        #//////////////////
Gui()