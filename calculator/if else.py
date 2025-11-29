while True:
    num1=int(input("enter first number :"))
    num2=int(input("enter second number :"))
    op=input("enter mathematical operator :")
    if(op=='+'):
        a=num1+num2
        print("result is :",a)
        continue
    elif(op=='-'):
        a=num1-num2
        print("result is :",a)
        continue
    elif(op=='*'):
        a=num1*num2
        print("result is :",a)
        continue
    elif(op=='/'):
        a=num1/num2
        print("result is :",a)
        continue
    elif(op=='%'):
        a=num1%num2
        print("result is :",a)
        continue
    elif(op=='**'):
        a=num1**num2
        print("result is :",a)
        continue
    elif(op=='//'):
        a=num1//num2
        print("result is :",a)
        continue
    else:
        print("please enter valid operator")
        continue 