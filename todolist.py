tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    for idx, task in enumerate(tasks, 1):
        status = "completed" if task["completed"] else "pending"
        print(f"{idx}. {task['task']} [{status}]")

def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    else:
        print("Invalid task number.")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter task number to mark completed: ")) - 1
        mark_completed(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
