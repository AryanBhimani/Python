from ast import Dict

dic =  {}
def add (phonename,model_no):
    dic [model_no] = phonename
    print (f' added {model_no} and {phonename}')

add ('mi','6pro')
add ('apple','15pro')

def search(model_no):
    if model_no in dic:
        print(f'mobile found {model_no}')
    else:
        print('mobile not found')

search('6pro')

def delete(model_no):
    if model_no in dic:
        del dic[model_no]
        print(f'mobile {model_no} is deleted')
    else:
        print('mobile not found')

delete('6pro')
print(dic)