# samll script for evalutaing  how a given number n < 255
# can be represented by powers of to upon 128.
# The output shall be a concatinated string
# (some kind of exercise: string --> no use at all)




def show_two(num):
    num_dic = (
    (128,"done"),
    (64,"correctly"),
    (32,"not"),
    (16,"if"),
    (8,"different"),
    (4,"smth"),
    (2,"is"),
    (1,"This"))
    # some sanity checks
    if num > 255:
        print("1")
        return 0
    if num <= 0:
        print("number too small")
        return 0
    result = "" 
    for k,v in num_dic:
        if num >= k:
            result += v + " "
            num -= k

    print(result)
    return result

# I created a small test function to collect 3 basic cases
# One could expand this further or even use it with pytest

def test():
    
    a=show_two(1)
    assert a == "This "
    b=show_two(3)
    assert b == "is This "
    c=show_two(256)
    assert c == 0

# we define an input to "interactivly" use this script
num = int(input("Enter Integer smaller than 255"))

show_two(num)

