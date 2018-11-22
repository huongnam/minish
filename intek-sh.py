import os

if __name__ == '__main__':
    while True:
        print('intek-sh$:',end=' ')
        command = input().split()
        if len(command) == 0:
            pass
        elif command[0] == 'exit':
            exit()
        elif command[0] == 'printenv':
            if len(command) == 1:
                print(os.environ)
            else:
                print(os.environ[command[1]])
        elif command[0] == 'pwd':
            print(os.getcwd())
        elif command[0] == 'cd':
            if len(command) == 1:
                os.chdir(os.environ['HOME'])
            else:
                os.chdir(command[1])
        elif command[0] == 'export':
            print(command[1][0])
            print("ha")
            command[1] = command[1].split('=')
            print("ha1")
            print(command[1][0])
            print("ha2")
            os.environ[command[1][0]] = command[1][1]
        elif command[0] == 'unset':
            del os.environ[command[1]]
