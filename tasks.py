tasks=[]
def add_task():
    task=input("enter a task to add:")
    tasks.append(task)
    print("task added successfully!")
    def remove_task():
        task=input("enter the task to remove:")
        if task in tasks:
            tasks.remove(task)
            print("task removed successfully!")
        else:
            print("task not found!")
            def view_tasks():
                if len(tasks)==0:
                    print("no tasks in the list.")
                else:
                    print("tasks:")
                    for task in tasks:
                        print(task)
                        while True:
                            print("1.add task")
                            print("2.remove task")
                            print("3.view tasks")
                            print("4.exit")
                            choice=input("enter your choice:")
                            if choice=="1":
                                add_task()
                            elif choice=="2":
                                remove_task()
                            elif choice=="3":
                                view_tasks()
                            elif choice=="4":
                                print("goodbye!")
                                break
                            else:
                                print("invalid choice.please try again.")