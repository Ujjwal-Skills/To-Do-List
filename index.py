#To do List

#making program to run until user select exit
while True:

    # show menu
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit\n")

    #user make choice from menu by entering the number
    choice = int(input("Enter your choice by entering the number: "))

    tasks = [] #add tasks entered by user
    
    #reading file and removing extra space
    try:
        with open("tasks.txt","r") as f:
            for line in f:
                tasks.append(line.strip())
    #fixing using try except, if file doesn't exist
    except:
        pass
    #if user choose option 1
    if choice == 1:
        task_name = input("\nEnter the task: ")
        tasks.append(task_name)

        #adding task in file (task.txt)
        with open("tasks.txt","a") as f:
            f.write(task_name + "\n")

        print("Task added successfully!")
        print("---------------------------------------------")
        #print(tasks)

    #if user choose option 2
    elif choice == 2:
        if len(tasks) == 0:
            print("\nNo tasks yet!")
            print("---------------------------------------------")
        else:
            
            print()
            for i in range(len(tasks)):
                #print(i+1,".",tasks[i])
                print(f"{i+1}. {tasks[i]}")
            print("---------------------------------------------")

            '''i = 1
            for task in tasks:
                print(i,".",task)
                i += 1'''
            
    #if user choose option 3
    elif choice == 3:
        mark_task_done = int(input("Enter the task number to mark it done: "))

        #preventing invalid number entry
        if mark_task_done > len(tasks):
            print("\nInvalid task number!")
        #preventing marking twice it task is already marked
        elif "[✔️ ] " in tasks[mark_task_done - 1]: 
            print("\nTask is already marked done!")
        #marking the task done
        else:
            tasks[mark_task_done - 1] = "[✔️ ] " + tasks[mark_task_done - 1]

            #overwriting the file with updated task
            with open("tasks.txt","w") as f:
                for task in tasks:
                    f.write(task + "\n")
        
            print("\nTask marked done successfully")
        
        print("---------------------------------------------")

    #if user choose option 4
    elif choice == 4:
        delete_task = int(input("Enter the task number to delete it: "))
        tasks.pop(delete_task - 1)

        #overwriting the file with updated task
        with open("tasks.txt","w") as f:
            for task in tasks:
                f.write(task + "\n")
        
        print("Task deleted successfully!")
        print("---------------------------------------------")

    #if user choose option 5    
    elif choice == 5:
        print("\nGoodbye!")
        print("---------------------------------------------")
        break
    
    #handling invalid choice
    else:
        print("\nInvalid Choice")
        print("---------------------------------------------")
        
