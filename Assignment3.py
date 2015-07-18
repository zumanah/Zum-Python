##########################
# Leap year calculation
# Author: Zumanah
# Date : July,18 ,2015
###########################
def main():
    y = eval(input("Enter year: "))
    if (y >= 1900 and y <= 2100):
        m = eval(input("Enter month: "))
        if(m>=1 and m<=12):
            d = eval(input("Enter day: "))
            if((d<=31 and d>=1) and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)):
                print("True")
            elif((d<=30 and d>=1) and (m==4 or m==6 or m==9 or m==11)):
                print("True")
            elif((m==2) and ((y%400==0) or ((y%100!=0) and (y%4==0))) and (d<=29 and d>=1)):
                print("True")
            elif(m==2 and d<=28 and d>=1):
                print("True")
            else:
                print("False")
        else:
            print("False")  
    else:
        print("False")
main()
