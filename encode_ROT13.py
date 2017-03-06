#！coding:utf-8
def rot13(message):
    a=list(message)
    for i in range(len(message)):
        if a[i].isalpha():
            if ord('a')<=ord(a[i])<=ord('z') and ord(a[i])+13>ord('z'):
                a[i]=chr(ord(a[i])+13-26)
            elif ord('A')<=ord(a[i])<=ord('Z') and ord(a[i])+13>ord('Z'):
                a[i]=chr(ord(a[i])+13-26)
            else:
                a[i]=chr(ord(a[i])+13)
    # print  "".join(a)       
    return "".join(a)

rot13("test asd")
