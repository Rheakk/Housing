
def get_fib ():
    print "0"
    last1 = 0
    last2 = 1
    new_number = 1
    while (new_number < 10):
        print new_number
        new_number = last1 + last2  
        last1 = last2
        last2 = new_number
    
    print "Done !"
    