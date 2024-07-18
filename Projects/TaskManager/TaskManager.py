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
        priority = priority.title()
        self.priority = priority
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_incompleted(self):
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

    def mark_task_complete(self, index):
        self.tasks[index].mark_completed()

    def mark_task_incomplete(self, index):
        self.tasks[index].mark_incomplete()

    #File I/O FUNCTION
    '''Save and load tasks to and form file
    file type - JSON
    save file function
    load file function
    '''
    def save_to_file(self, filename):
        tasks_data = [
            {
                'title': task.title,
                'description': task.description,
                'priority': task.priority,
                'category': task.category,
                'completed': task.completed
            } for task in self.tasks
        ]
        with open(filename, 'w') as file:
            json.dump(tasks_data, file)


    def read_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [
                    Task(task['title'], task['description'], task['priority'], task['category'])
                    for task in tasks_data
                ]
                for task, task_data in zip(self.tasks, tasks_data):
                    if task_data['completed']:
                        task.mark_completed()
        except FileNotFoundError:
            print("File not found")

#User Interface Function with features
'''add features'''
def add_task(manager):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    while True:
        priority = input("Enter task priority (High, Medium, Low): ")
        priority = priority.title()
        if priority in ['High', 'Medium', 'Low']:
            break
        else:
            print("Enter valid input like High, Medium, Low")
    category = input("Enter task category: ")
    task = Task(title, description, priority, category)
    manager.add_task(task)
    print("Task added successfully")

def update_task(manager):
    while True:
        try:
            index = int(input("Enter task index to update: "))
            break
        except ValueError:
            print("Enter Integer number")
    index -= 1
    title = input("Enter new task title: ")
    description = input("Enter new task description: ")
    while True:
        priority = input("Enter task priority (High, Medium, Low): ")
        priority = priority.title()
        if priority in ['High', 'Medium', 'Low']:
            break
        else:
            print("Enter valid input like High, Medium, Low")
    category = input("Enter new task category: ")
    task = Task(title, description, priority, category)
    manager.update_task(index, task)
    print("Task updated successfully")

def delete_task(manager):
    while True:
        try:
            index = int(input("Enter task index to delete: "))
            break
        except ValueError:
            print("Enter Integer number")
    index -= 1
    manager.delete_task(index)
    print("Task deleted successfully")

def list_all_tasks(manager):
    tasks = manager.list_tasks()
    for i, task in enumerate(tasks, start = 1):
        print(f"{i}: {task.title} - {task.description} - {task.priority} - {task.category} - {'Completed' if task.completed else 'Pending'} ")

    if len(tasks) == 0:
        print("There are no Tasks")

def list_status_tasks(manager, completed= True):
    tasks = manager.list_tasks(lambda t: t.completed == completed)
    for i, task in enumerate(tasks, start = 1):
        print(f"{i}: {task.title} - {task.description} - {task.priority} - {task.category} - {'Completed' if task.completed else 'Pending'} ")

    if len(tasks) == 0:
        print("There are no Tasks")

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
    menu=['add task','update task','delete task','list all task','list completed','list pending', 'mark complete tasks',
    'save tasks to file','load task from file','exit']
    while True:
        print("\n*******************************************************************")
        print("Menu")

        for i,j in zip(menu,(1,2,3,4,5,6,7,8,9,10)):
            print(str(j)+"."+str(i))
        while True:
            try:
                x = int(input("Enter your choice number"))
                break
            except ValueError:
                print("Enter number from the option: ")
        if x == 1:
             add_task(manager)

        elif x == 2:
            while True:
                try:
                    update_task(manager)
                    break
                except IndexError:
                    print("List assignment index out of range")

        elif x == 3:
            while True:
                try:
                    delete_task(manager)
                    break
                except IndexError:
                    print("List assignment index out of range")

        elif x == 4:
            list_all_tasks(manager)

        elif x == 5:
            #list completed
            list_status_tasks(manager, completed= True)

        elif x == 6:
            #list pending
            list_status_tasks(manager, completed= False)

        elif x == 7:

            while True:
                try:
                    index = int(input("Enter task index to mark complete: "))
                    if index < 1 or index > len(manager.tasks):
                        raise IndexError
                    manager.mark_task_complete(index - 1)
                    break
                except ValueError:
                    print("Enter Integer number")
                except IndexError:
                    print("List assignment index out of range")

        elif x == 8:
            #save tasks to file
            filename = input("Enter filename to save tasks: ")
            manager.save_to_file(filename)

        elif x == 9:
            #load task from file
            filename = input("Enter filename to load tasks: ")
            manager.read_from_file(filename)
        elif x == 10:
            break

        else:
            print("Invalid Input. Please try again")

if __name__ == '__main__':
    main()
