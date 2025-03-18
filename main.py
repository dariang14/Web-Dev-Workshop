from fastapi import FastAPI
from task_model import Task

app = FastAPI() #constructor creating the instance. storing it under the variable app

#create a list called tasks to store a bunch of tasks.
tasks = [
    Task(description= "Hello"), #creating a task object from our task class
    Task()
]

@app.get("/get-tasks") # get("create any address name you want") is a built in function, we're using on our variable "app". The address name is the end of your url and will describe what the get function is doing
def get_all_tasks(): #creating a function."def" defines the fucntion followed by its name
    return tasks # get retrieves information. so we want to retrieve the list of tasks named "tasks"

# @app.get("/") # get("create any address name you want") is a  built in function, we're using on our variable "app"
# def get_task(): #creating a function."def" defines the fucntion followed by its name
#     return "Hello"

# @app.put("/")
# def update_task(): 
#     return "Hello"

# @app.post("/") 
# def create_task(): 
#     return "Hello"

# @app.delete("/") 
# def delete_task(): 
#     return "Hello"
