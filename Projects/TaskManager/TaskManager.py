import json
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
    
    def save_to_file(task, filename):
        with open(filename, 'a') as file:
            json.dump(task, file,)


    def read_from_file(filename):
        with open(filename, 'r') as file:
            task = json.load(file)
            return task
    
#User Interface Function with features
'''add features'''

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
def main():
    manager = TaskManager()
    menu=['add task','update task','delete task','list all task','list completed','list pending',
    'save tasks to file','load task from file','exit']
    while True:
        print("Menu")
        
        for i,j in zip(menu,(0,1,2,3,4,5,6,7,8,9)):
            j+=1
            print(str(j)+"."+str(i))
        x=input("Enter your choice ")
        if x==menu[0]:
             add_task(manager)

        elif x==menu[1]:
            update_task(manager)

        elif x==menu[2]:
            delete_task(manager)

        elif x==menu[3]:
            list_all_tasks(manager)

        elif x==menu[4]:
            #list completed
            list_status_tasks(manager, completed= True)

        elif x==menu[5]:
            #list pending
            list_status_tasks(manager, completed= False)

        elif x==menu[6]:
            #save tasks to file
            filename = input("Enter filename to save tasks: ")
            manager.save_to_file(,filename)

        elif x==menu[7]:
            #load task from file
            filename = input("Enter filename to load tasks: ")
            manager.read_from_file(filename)
        elif x==menu[8]:
            break

        else:
            print("Invalid Input. Please try again")
            
if __name__ == '__main__':        
    main()
