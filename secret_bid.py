from os import system,name

def clear():
	# for windows
	if name == 'nt':
		system('cls')

	# for ios and linux
	else:
		system('clear')


data={}

flag='y'
while flag=='y':
    key=input("enter name : ")
    value=int(input("enter bid : "))
    data[key]=value

    flag=input("another bid y/n : ").lower()
    clear()

max=0
for i in data:
    if data[i] > max:
        max=data[i]
        name=i

print('max bid is ',max , ' by ',name)
