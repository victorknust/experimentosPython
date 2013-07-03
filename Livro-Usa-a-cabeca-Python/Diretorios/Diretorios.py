import os

fileName = 'text.txt'
if os.path.exists(fileName):
    file = open(fileName)
    try:
        count = 0;
        for line in file:
            print('#' + str(count), end=' - ')
            if not line.find(':') == -1:
                (author, phrase) = line.split(':', 1)
                print(author + ': ' + phrase, end='============================ \n')
            else:
                print('* ' + line, end='============================ \n')

            count += 1
        
    except:
        print('Deu zebra')
    
    finally:
        file.close()
    
else:
    print('Infelizmente o seu arquivo nao existe amigo =(')
