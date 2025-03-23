from db_task_model import Task
from sqlmodel import select, Session

def get_all_tasks(session: Session):
   statment = select(Task)
   tasks = session.exec(statment).all()
   return tasks

def create_task(task: Task, session: Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def update_task(task_id: int, updated: Task, session: Session):
    task= session.get(Task, task_id)
    if not task:
        return "Task Not Found"
    
    task.description = updated.description
    task.isComplete = updated.isComplete
    session.commit()
    session.refresh(task)

    return task

def delete_task(task_id: int, session: Session):
    task = session.get(Task, task_id)
    
    if not task:
        return "Task Not Found"
    session.delete(task)
    session.commit()
    
    return "Task deleted successfully"

def get_task(task_id: int, session: Session):
    task = session.get(Task, task_id)
    
    if not task:
        return "Task Not Found"
    
    return task    

    