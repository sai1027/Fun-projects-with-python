import random
lst=['apple','banana','car']
word= random.choice(lst)

n=len(word)
guess=n*['_']

print(f"guess the {n} letter word : ")

x,flag=0,0

while x<5 and flag==0 :
    ans=[]
    a=input("guess any letter : ")

    if a in ans :
        print("its already tried")
        continue
    else :
        ans.append(a)


    for i in range(n):
        if ans[x]==word[i]:
            guess[i]=ans[x]


    print(guess)
    temp=''.join(guess)
    if temp==word:
        flag=1
        print("hurray!..\n you got correct ",word)
    x+=1
if flag==0:
    print("oh!!.. better luck next time \n correct ans is : ",word)
