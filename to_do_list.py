to_do_list=[]
def add():
    task=input("Enter the task to be addded: ")
    to_do_list.append(task)
    print("The task is added to the list")
def delete():
    if(len(to_do_list)<1):
        print("List is empty")
    else:
        idx=int(input("Enter the idx from where the task is to be deleted"))
        del to_do_list[idx]
        print("The task is deleted from the list")
def view():
    if(len(to_do_list)<1):
        print("List is empty")
    else:
        print("The task in your to-do-list are")
        for i in to_do_list:
            print(i)
def main():
    print("Press 1 to add")
    print("Press 2 to delete")
    print("Press 3 to view")
    while True:
        choice=int(input("Enter your choice"))
        if(choice==1):
            add()
        elif(choice==2):
            delete()
        elif(choice==3):
            view()
        elif(choice==4):
            print("Exit")
            break
        else:
            print("Invalid Choice")
if __name__=='__main__':
    main()
