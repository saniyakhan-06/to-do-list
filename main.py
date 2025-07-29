todo_list = []
def show_task():
    if not todo_list:
        print("\nNo tasks yet!\n")
        return
    print("To Do list:")
    for i, task in enumerate(todo_list, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['task']} [{status}]")
    print()

def add_task():
    task = input("Enter a task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added!\n")

def mark_done():
    show_task()
    try:
        num = int(input("Enter task number to be marked as done: "))
        todo_list[num - 1]['done'] = True
        print("Task added!\n")
    except:
        print("Invalid input\n")

def delete_task():
    show_task()
    try:
        num = int(input("Enter task number to be deleted: "))
        todo_list.pop(num - 1)
        print("Task deleted!\n")
    except:
        print("Invalid input")


def main():
    while True:
        print("To-Do List Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")
            

main()