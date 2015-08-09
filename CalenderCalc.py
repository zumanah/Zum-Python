# part 2

def main():
    while True:
        y = eval(input("Enter year between 1900 and 2100: "))
        if(y >= 1900 and y <= 2100):
            z = y//100
            c = y%100
            if(y == 2000):
                c = 0
            while True:
                m = eval(input("Enter month: "))
                if(m >= 1 and m <= 12):
                    a = m - 2
                    if(a == -1):
                        a = 11
                        c = c - 1
                    elif(a == 0):
                        a = 12
                        c = c - 1
                    while True:
                        d = eval(input("Enter day: "))
                        if((d<=31 and d>=1) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)):
                            print("a =", a, "b =", d, "c=", c, "d =", z)
                        elif((d<=30 and d>=1) and (m==4 or m==6 or m==9 or m==11)):
                            print("a =", a, "b =", d, "c=", c, "d =", z)
                        elif((m==2) and ((y%400==0) or ((y%100!=0) and (y%4==0))) and (d<=29 and d>=1)):
                            print("a =", a, "b =", d, "c=", c, "d =", z)
                        elif(m==2 and d<=28 and d>=1):
                            print("a =", a, "b =", d, "c=", c, "d =", z)
                        a = a
                        b = d
                        c = c
                        d = z
                        w = (13*a-1)//5
                        x = c//4
                        y = d//4
                        z = w+x+y+b+c-2*d
                        r = z%7
                        r = (r+7)%7
                        if(r == 0):
                            print("Sunday")
                        if (r == 1):
                            print("Monday")
                        break
                    break
            break
main()
