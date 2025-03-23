from fastapi import FastAPI
from task_model import Task

app = FastAPI() #constructor creating the instance. storing it under the variable app

#create a list called tasks to store a bunch of tasks.
tasks = [
    Task(description= "Hello"), #creating a task object from our task class
    Task()
]

@app.get("/")
def root():
    return "hello world"

@app.get("/get-tasks") # get("create any address name you want") is a built in function, we're using on our variable "app". The address name is the end of your url and will describe what the get function is doing
def get_all_tasks(): #creating a function."def" defines the fucntion followed by its name
    return tasks # get retrieves information. so we want to retrieve the list of tasks named "tasks"

@app.get("/get-a-task/{task_id}") # get("create any address name you want") is a  built in function, we're using on our variable "app"
def get_a_task(task_id: int): #creating a function."def" defines the fucntion followed by its name
    for task in tasks:
        if task_id == task_id:
            return task
    return "Task not found"
        

@app.put("/update-task/{task_id}")
def update_task(task_id: int, updated_task: Task): 
    for task in tasks:
        if tasks.id == task_id:
            task.description = updated_task.description
            task.isComplete = updated_task.isComplete
            return "Updated task"
    return "Task not updated"
    

@app.post("/create-task") 
def create_task(task: Task): 
    tasks.append(task)
    return "Task Added"

@app.delete("/delete-task/{task_id}") 
def delete_task(task_id:int): 
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return "Deleted task"
    return "Task not deleted"
