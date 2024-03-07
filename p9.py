with open ('p9.txt','w') as file:
    file.write('Hello world')
with open ('p9.txt','r') as file:
    content = file.read()
    print(content)