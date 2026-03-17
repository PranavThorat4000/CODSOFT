# To-Do List Application

tasks = []

while True:
    print("\n------ TO-DO LIST MENU ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully!")


    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['task']} - {tasks[i]['status']}")


    elif choice == "3":
        num = int(input("Enter task number to update: "))
        if 0 < num <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[num-1]["task"] = new_task
            print("Task updated!")
        else:
            print("Invalid task number")


    elif choice == "4":
        num = int(input("Enter task number to mark completed: "))
        if 0 < num <= len(tasks):
            tasks[num-1]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number")


    elif choice == "5":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid task number")

    
    elif choice == "6":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice, try again!")