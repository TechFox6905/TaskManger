#Task Class
'''Defines the sturcture and behavior of task
Task's Properties-
1)Title
2)Description
3)priority
4)category
'''
#Task Manager Class
'''Manages a list of task with features
function of each -
1)add task 
2)delete task
3)update task
4)list all task
5)list completed task
6)list pending task'''
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
    menu=['add task','update task','delete task','list all task','list completed','list pending','save tasks to file','load task from file','exit']
    while True:
        print("Menu")
        
        for i,j in zip(menu,(0,1,2,3,4,5,6,7,8,9)):
            j+=1
            print(str(j)+"."+str(i))
        x=input("Enter your choice ")
        if x==menu[0]:
             #add task
        elif x==menu[1]:
            #update task
        elif x==menu[2]:
            #delete task
        elif x==menu[3]:
            #list all task
        elif x==menu[4]:
            #list completed
        elif x==menu[5]:
            #list pending
        elif x==menu[6]:
            #save tasks to file
        elif x==menu[7]:
            #load task from file
        elif x==menu[8]:
            break
            
        
main()