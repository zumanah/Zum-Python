def main():
    y = eval(input("Enter year: "))
    a = y%19
    b = y//100
    c = y%100
    d = b//4
    e = b%4
    g = (8*b+13)//25
    h = (19*a+b-d-g+15)%30
    j = c//4
    k = c%4
    m = (a+11*h)//319
    r = (2*e+2*j-k-h+m+32)%7
    n = (h-m+r+90)//25
    p = (h-m+r+n+19)%32
    if(n==1):
        print("January")
    if(n==2):
        print("February")
    if(n==3):
        print("In", y, "Easter Sunday is on", p, "March.")
    if(n==4):
        print("In", y, "Easter Sunday is on", p, "April.")
    if(n==5):
        print("May")
    if(n==6):
        print("June")
    if(n==7):
        print("July")
    if(n==8):
        print("August")
    if(n==9):
        print("September")
    if(n==10):
        print("October")
    if(n==11):
        print("November")
    if(n==12):
        print("December")
main()
