#Task Class
'''Defines the sturcture and behavior of task
Task's Properties-
1)Title
2)Description
3)priority
4)category
'''
class Task:
    def __init__(self, title, description, priority, category):
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.completed = False

    def completed(self):
        self.completed = True

    def incompleted(self):
        self.completed = False


#Task Manager Class
'''Manages a list of task with features
function of each -
1)add task 
2)delete task
3)update task
4)list all task
5)list completed task
6)list pending task'''

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def update_task(self, index, task):
        self.tasks[index] = task
    
    def delete_task(self,index):
        self.tasks.pop(index)
    
    def list_tasks(self, filter_func =  None):
        if filter_func is not None:
            return list(filter(filter_func, self.tasks))
        return self.tasks


#File I/O FUNCTION
'''Save and load tasks to and form file
file type - JSON
save file function 
load file function
'''
#MAIN FUNCTION
'''Display menu for user interaction
menu - 
1.add task
2.update task
3.delete task
4.list all task
5.list completed
6.list pending
7.save tasks to file
8.load task from file
9.exit
'''