try:
    with open("explore_file",'w') as file:
        read_file = str(input())
        file.write(read_file)
    with open("explore_file",'r') as file:
        data = file.read()
        print(data)
except SyntaxError:
    print("Syntax Error") 
except ValueError:
    print("Value Error")               
finally:
    print("YES")
        