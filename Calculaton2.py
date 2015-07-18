#this program will solve: {6-4+((81/3)*(6*3))}^2

def main():
    a = div(81,3)
    b = mult(6,3)
    c = mult(a,b)
    d = sub(6,4)
    e = add(d,c)
    f = exp(e,e)
    print("The solution of the problem, {6-4+((81/3)*(6*3))}^2, is", f)

def div(a,b):
    return(a/b)
def mult(c,d):
    return(c*d)
def add(e,f):
    return(e+f)
def sub(x,y):
    return(x-y)
def exp(z,f):
    return(z*f)

main()
    
