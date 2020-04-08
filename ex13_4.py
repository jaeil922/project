#!/usr/bin/env python
# coding: utf-8

# In[1]:


from turtle import *

class MyTurtle(Turtle):
    def drawSquare(self):
        for i in range(4):
            self.right(90)
            self.forward(100)
        
turtle=MyTurtle()
turtle.forward(100)
turtle.drawSquare()


# In[ ]:




