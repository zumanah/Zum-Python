#this program will tell you if an input is a three digit number and divisible by 3
def main():
    a = eval(input("Enter answer"))
    if(a>=100 and a<=999 and a%3==0):
        print("True")
    else:
        print("False")
main()
