#To do List

#making program to run until user select exit
while True:

    # show menu
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    #user make choice from menu by entering the number
    choice = int(input("Enter your choice by entering the number: "))

    tasks = [] #add tasks entered by user

    #if user choose option 1
    if choice == 1:
        task_name = input("Enter the task: ")
        tasks.append(task_name)
        print("Task added successfully!")
        #print(tasks)

    #if user choose option 2
    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(tasks)):
                #print(i+1,".",tasks[i])
                print(f"{i+1}. {tasks[i]}")

            '''i = 1
            for task in tasks:
                print(i,".",task)
                i += 1'''
            
    #if user choose option 3    
    elif choice == 3:
        print("Goodbye!")
        break
        
