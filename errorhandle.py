file = open('youtube.txt','w')
try:
    file.write('youtube video manager')
finally:
    file.close()


    with open('youtube.txt','w')as file:
        file.write('youtbe and python')