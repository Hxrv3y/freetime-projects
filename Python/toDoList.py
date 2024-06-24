import time

tasks = []

def addATask():
    task = input("Enter the task you want to add: ")
    deadline = input("Enter the deadline for the task (DD/MM/YYYY): ")
    priority = input("Enter the priority for the task (High, Medium, Low): ")
    category = input("Enter the category for the task: ")
    tasks.append({"Task": task, "Deadline": deadline, "Priority": priority, "Category": category})
    
def viewAllTasks():
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['Task']} - {task['Deadline']} - {task['Priority']} - {task['Category']}")
    else:
        print("No tasks found.")
            
def deleteATask():
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['Task']} - {task['Deadline']} - {task['Priority']} - {task['Category']}")
        taskToDelete = int(input("Enter the task number you want to delete: "))
        if 0 <= taskToDelete < len(tasks):
            del tasks[taskToDelete]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks found.")

while True:
    toDoListMenu = int(input("1. Add a task\n2. View all tasks\n3. Delete a task\n4. Exit \nEnter your choice: "))
    if toDoListMenu == 1:
        addATask()
    elif toDoListMenu == 2:
        viewAllTasks()
    elif toDoListMenu == 3:
        deleteATask()
    elif toDoListMenu == 4:
        break
    else:
        print("Invalid input. Please try again.")