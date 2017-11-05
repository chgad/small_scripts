
# Another way to do what the script two.py does
# now I'm using the collections lib.

from collections import OrderedDict
import sys, getopt


# rewrite the function

def show_two(num):
    num_dic =  OrderedDict()
    num_dic[128] = "What"
    num_dic[64] = "is"
    num_dic[32] = "going"
    num_dic[16] = "on"
    num_dic[8] = "here"
    num_dic[4] = "tell"
    num_dic[2] = "me"
    num_dic[1] = "now!"

    if num > 255:
        print(num_dic[1])
        return 0
    if num <= 0:
        print("number to small")
    result = ""

    for k,v in num_dic.items():
        if num >= k:
            result += v +" "
            num -= k

    print(result)
    return(result)

if __name__ == "__main__":
 
    #try:
    #    opts , args = getopt.getopt(sys.argv[1:], "hn:")
    #except getopt.GetoptError:
    #    print("usage: two_2.py -n <number: integer>")
    #    sys.exit(2)
    #for opt, arg in opts:
    #    if opt == "-h":
    #        print("usage: two_2.py -n <number: integer>")
    #        sys.exit(2)
    #    elif opt == "-n":
    #        num = int(arg)
    
    num = int(input("enter an integer smaller than 255: "))
    
    show_two(num)


