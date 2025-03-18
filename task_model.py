from pydantic import BaseModel #importing BsseModel from pydantic

cur_id = 0 # acts as a counter to increment

def increment(): #increment function to increment ids
    global cur_id # gloabl is like public or private. if you use a variable that is outside of a function in a function, it will not recognize that you are calling the outside one. Instead it will create a new variable entirely and delete it. Global keyword prevents that
    cur_id += 1 #increment
    return cur_id

class Task(BaseModel): #creating task class using Basemodel for variable types
    id: int 
    decription: str = ""
    isComplete: bool = False
#^^^ set the default values of the parameters (things that every task will have)

    def __init__(self, **data): #"__init__" serves as a constructor to initialize an object's attributes
        super().__init__(id= increment(), **data) # self = this in java. must be listed as one of the parameters