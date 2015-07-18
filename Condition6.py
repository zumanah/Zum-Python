#this program will tell you if an input is not a 3 digit number
def main():
    a = eval(input("Enter answer"))
    if(a<100 or a>999):
        print("True")
    else:
        print("False")
main()
