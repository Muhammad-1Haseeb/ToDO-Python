import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print("\n📭 Your Todo List is Empty!")
        return
    
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("-" * 20)

def add_task(tasks):
    task_text = input("\nEnter new Task: ").strip()
    if task_text == "":
        print("❌ Task can not be empty!")
        return
    tasks.append(task_text)
    save_tasks(tasks)
    print(f"✅ '{task_text}' successfully added!")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nChoose the task you want to delte: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️ '{removed}' has been deleted.")
        else:
            print("❌ You selected the wrong number")
    except ValueError:
        print("❌ Please enter a valid number")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== PYTHON TO-DO APP ===")
        print("1. Tasks")
        print("2. Add New Task")
        print("3. Delete Task")
        print("4. Exit App")
        
        choice = input("\nChoose a Option (1-4): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("\n👋 Good bye Take care.")
            break
        else:
            print("❌ Invalid choice! Please choose between 1 to 4.")

if __name__ == "__main__":
    main()