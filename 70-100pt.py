# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590)
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False
hit = False

direction = 5


class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = 3
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        self.rocketFired = False
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        if rocket1Fired == True:
            drawpad.move(rocket1,0,-5)
        hit = self.collisionDetect()
        if hit == True:
            drawpad.delete(enemy)
            drawpad.move(rocket1,px1-rx1+10,py1-ry1+10)
        if ry1 < 0:
            drawpad.move(rocket1,px1-rx1+10,py1-ry1+10)
            rocket1Fired = False
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        global rocket1Fired
        px1,py1,px2,py2 = drawpad.coords(player)
        if event.char == "a" and px1 > 0:
            drawpad.move(player,-4,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,-4,0)
        elif event.char == "d":
            drawpad.move(player,4,0)
            if rocket1Fired == False:
                drawpad.move(rocket1,4,0)
        elif event.char == "w": 
            drawpad.move(player,0,-4)
            if rocket1Fired == False:
                drawpad.move(rocket1,0,-4)
        elif event.char == "s" and py2 < 600:
            drawpad.move(player,0,4)
            if rocket1Fired == False:
                drawpad.move(rocket1,0,4)
        elif event.char == " ":
            rocket1Fired = True
            self.rockets = self.rockets -1
            self.rocketsTxt.configure(text=str(self.rockets))
    
    def collisionDetect(self):
        global enemy
        global rocket1
        x1,y1,x2,y2 = drawpad.coords(enemy)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        if rx1 >= x1 and rx2 <= x2 and ry1 >= y1 and ry2 <= y2:
            return True
app = myApp(root)
root.mainloop()