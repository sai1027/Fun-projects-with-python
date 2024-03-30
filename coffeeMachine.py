
#  not yet completed
'''
      m (200)     w300    c 100       p
 tea  150   200    24  25

 coffee  100   250  24   30

 green - 50 18       15
'''




def store(a):
    storel=[200,300,100]
    print(a)
    for i in storel:
        if storel[i]-a[i]<0:
            return 0

    else:
        for i in storel:
            storel[i]=storel[i]-a[i]

        return 1


def tea(n):
    teal=[150,200,24]
    check=[n*i for i in teal]
    return store(check)

def green(n):
    greenl=[0,50,18]
    check=[n*i for i in teal]
    return store(check)


def coffee(n):
    coffeel=[100,250,24]
    check=[n*i for i in teal]
    return store(check)


def wallet(i,q,c):
    price={'tea':25,'coffee':30,'green tea':15}
    cost=price[i]*q
    print("here is the change : ",c-cost)


# main

type=input("what do u want ? (tea/ coffee/ green tea : )")
quantity=int(input("enter the quantity : "))


if type=='tea':
    status=tea(quantity)
    if status==1:
        wallet(item,quantity,cash)

elif type=='coffee':
    status=coffee(quantity)
    if status==1:
        wallet(item,quantity,cash)

elif type=='green tea':
    status=green(quantity)
    if status==1:
        wallet(item,quantity,cash)








#
