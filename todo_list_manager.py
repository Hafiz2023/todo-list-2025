# To-Do List Manager

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nThank you for using the To-Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()