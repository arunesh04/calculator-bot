'''calculator for simple algebraic calculations'''

from random import randint


def greet_random():
    greetings=["Hey","Hello","Welcome","Hurray"]
    n=randint(0,len(greetings))
    return greetings[n-1]


greeting = greet_random()
quit_msg=["quit","bye","exit","q",]
greet=greet_random()
print(greeting,",I am a Calculator Bot , Lets solve the basic arithematic operations")
while True:
    msg=input()
    if msg in quit_msg:
            q=input("Do you want to quit[y/n]")
            if q=='y':
                break

    else:
        summ=0
        mul=0
        div=0
        sub=0
        sqr=0
        for i in msg.split():
            try:
                a=float(i)
                if "add" in msg:
                    summ+=a
                elif "mul" in msg:
                    if mul==0:
                        mul=a
                    else:
                        mul*=a
                elif "divide" in msg:
                    if div==0:
                        div=a
                    else:
                        div/=a
                elif "square" in msg:
                    if sqr == 0:
                        sqr=a
                    else :
                        sqr=sqr**a
                elif "sub" in msg:
                    if sub==0:
                        sub=a
                    else:
                        sub-=a
            except:
                continue
        if "add" in msg: 
            print(summ)
        elif "mul"in msg:
            print(mul)
        elif "divide" in msg:
            print(div)
        elif "square" in msg:
            print(sqr)
        elif "sub" in msg:
            print(sub)

            
        
            