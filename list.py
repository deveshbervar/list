# Simple To-Do List (Console Version)

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if not tasks:
            print("\nNo tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':
        task = input("Enter the task to add: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '3':
        if not tasks:
            print("\nNo tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                del_index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= del_index < len(tasks):
                    removed_task = tasks.pop(del_index)
                    print(f"Deleted: {removed_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
