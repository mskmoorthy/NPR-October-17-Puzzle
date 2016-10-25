
def postfix_evaluation(s):
    s=s.split()
    n=len(s)
    stack =[]
    for i in range(n):
        if s[i].isdigit():
          #append function is equivalent to push
            stack.append(float(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(float(a)+float(b))
        elif s[i]=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(float(a)*float(b))
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            if (a!=0):
                stack.append(float(b)/float(a))
            else:
                stack.append(-1000000.5)
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(float(b)- float(a))
             
    return stack.pop()
ops =["+","-","*","/"]
numbers = [0 for x  in range(101)]
alist = [[] for x in range(14)]
a = 5
b = 4
c = 3
d = 2
e = 1
##print postfix_evaluation(" 2 3 4 / /")

count = 0
for x1 in range(len(ops)):
    for y1 in range(len(ops)):
        for z1 in range(len(ops)):
            for w1 in range(len(ops)):
                count = count + 1
                x = ops[x1]
                y = ops[y1]
                z = ops[z1]
                w = ops[w1]
                alist[0] = [a,b,c,d,e,w,z,y,x]
                alist[1] = [a,b,c,d,w,e,z,y,x]
                alist[2] = [a,b,c,z,d,e,w,y,x]
                alist[3] = [a,b,c,d,w,z,e,y,x]
                alist[4] = [a,b,c,w,d,z,e,y,x]
                alist[5] = [a,b,y,c,d,e,w,z,x]
                alist[6] = [a,b,y,c,d,w,e,z,x]
                alist[7] = [a,b,c,z,y,d,e,w,x]
                alist[8] = [a,b,z,c,y,d,e,w,x]
                alist[9] = [a,b,c,d,w,z,y,e,x]
                alist[10] = [a,b,c,w,d,z,y,e,x]
                alist[11] = [a,b,z,c,d,w,y,e,x]
                alist[12] = [a,b,c,w,z,d,y,e,x]
                alist[13] = [a,b,w,c,z,d,y,e,x]
                for i in range(14):
##                    print "****", count
##                    print alist[i]
##                print "================================="
                    s = ' '.join(map(str, alist[i]))
                    val=postfix_evaluation(s)
                    if (val.is_integer()):
                        if ((int(val)>= 0) & (int(val) < 41)):
                            if (numbers[int(val)]==0):
                                print alist[i],int(val)
                                numbers[int(val)] = 1
for i in range(41):
    if (numbers[i]==0):
        print i



    

