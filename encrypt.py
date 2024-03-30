def encode(text,shift):
    entext=''
    for x in text:
        entext+=chr(ord(x)+shift)
    return entext

def decode(text,shift):
    detext=''
    for x in text :
        detext+= chr(ord(x)-shift)
    return detext

ans='y'
while ans=='y':
    option=input("encode / decode : ")
    text=input("enter the message : ")
    shift=int(input("how many shifts : "))

    if option=='encode':
        encrypted_text=encode(text,shift)
        print(encrypted_text)
    elif option=='decode':
        decrypted_text=decode(text,shift)
        print(decrypted_text)
    ans=input("want to use y / n : ")
