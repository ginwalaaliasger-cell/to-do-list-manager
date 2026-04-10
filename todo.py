import os

FILE_NAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            tasks = file.read().splitlines()
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show all tasks
def view_tasks(tasks):
    print("\n------ YOUR TO-DO LIST ------")
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    print("-----------------------------")

# Add a task
def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task == "":
        print("Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

# Remove a task
def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"❌ Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("=============================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-4.")

# Run the program
if __name__ == "__main__":
    main()
