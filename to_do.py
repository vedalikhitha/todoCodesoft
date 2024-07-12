tasks = []
next_id = 1

def add_task():
    global next_id
    title = input("Enter task title: ")
    task = {'id': next_id, 'title': title, 'status': 'pending'}
    tasks.append(task)
    next_id += 1
    print(f"Task '{title}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nTo-Do List:")
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")

def update_task():
    try:
        task_id = int(input("Enter the task ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    for task in tasks:
        if task['id'] == task_id:
            new_title = input(f"Enter new title for task '{task['title']}' (leave blank to keep current title): ")
            if new_title:
                task['title'] = new_title
            new_status = input(f"Enter new status for task '{task['title']}' (pending/completed): ").lower()
            if new_status in ['pending', 'completed']:
                task['status'] = new_status
            print(f"Task '{task_id}' updated successfully!")
            return

    print(f"Task with ID '{task_id}' not found.")

def delete_task():
    try:
        task_id = int(input("Enter the task ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print(f"Task '{task_id}' deleted successfully!")
            return

    print(f"Task with ID '{task_id}' not found.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
