todo=[]
while True:
    print(f"\n \nSimple todo list progam \nWhat would you like to do?\n1) Add a task\n2) Mark a task as completed\n3) View tasks\n4) Quit")
    choice = int(input(f"\n: "))

    if choice==1:
        todo.append(input("Please enter a new task: "))
        print(f"Here is the updated task list: {todo}")
        continue
    elif choice==2:
        choice2=int(input(f"Here are your tasks: {todo}\n \nWhich would you like to mark as completed? :"))
        todo.pop(choice2)
        print("Done!")
        continue
    elif choice==3:
        print(f"Here are your tasks: {todo}")
    elif choice==4:
        print("Thanks for using this program!")
        break
    else:
        print("Please choose a valid option")
        continue