do_list = []

def add():
    num = int(input("Enter the number of tasks to perform: "))
    for i in range(num):
        task = input("Enter the task to be executed: ")
        do_list.append(task)

def show():
    print("Tasks to do:")
    for task in do_list:
        print(task)

def remove():
    t_rem = input("Enter the task to be removed: ")
    if t_rem in do_list:
        do_list.remove(t_rem)
        print("Task Removed!")
    else:
        print("Task not found!")

if __name__ == "__main__":
    while True:
        print('Menu:')
        print('1. ADD')
        print('2. SHOW')
        print('3. REMOVE')
        print('4. EXIT')
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            remove()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print('Please choose a valid option.')
