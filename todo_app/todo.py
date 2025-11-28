
'''
writelines() = A method that writes a list of strings to a file without 
               adding newline characters automatically.

readlines() = A method that reads all lines from a file and returns them 
               as a list of strings.
               
read() = A method that reads the entire content of a file as a single string.

write() = A method that writes a single string to a file.

'''



while True:
    # Get User input and strip chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action :
        case "add":
            todo = input("enter  a todo :") + '\n'
            
            todoFilename = open(r"C:\Users\Relanto\Desktop\python_AI_course_1\file\todo.txt",'r')
            todos = todoFilename.readlines()
            todoFilename.close()
            
            todos.append(todo)
            todoFilename = open(r"C:\Users\Relanto\Desktop\python_AI_course_1\file\todo.txt",'w')
            todoFilename.writelines(todos)
            todoFilename.close()
        case "show":
            
            file = open(r"C:\Users\Relanto\Desktop\python_AI_course_1\file\todo.txt",'r')
            todos = file.readlines()
            file.close()
            
            # print(todos)
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(new_todos)
            
            # new_todos = [item.strip() for item in todos]
                
            for index,item in enumerate(todos):
                item = item.strip('\n ')
                row = f'{index+1}-{item}'
                print(row)
        case "edit":
            number = int(input("number of the todo to edit :"))
            todos[number] = input("enter the new todo :")
        case "exit":
            break
        case "complete":
            number = int(input("number of todos to complete :"))
            todos.pop(number-1)
        case _:
            print("you entered invalid command")
print("bye!!!")