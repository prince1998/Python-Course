def compute_value(n):
    n1 = int( "%s" %n )
    n2 = int( "%s%s" % (n,n) )
    n3 = int( "%s%s%s" % (n,n,n) )
    result = n1+n2+n3
    return result

n = int(input("Input an integer : "))
print(f"Computed value: {compute_value(n)}")