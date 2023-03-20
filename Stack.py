stack=[1,2,3]
stack1=[5,4]
stack2=[]
print(stack,stack1,stack2)
stack2.append(stack1.pop())
print(stack,stack1,stack2)
for a in range(2):
    if stack1[-1]%2 !=0:
        stack2.append(stack1.pop())
        print(stack,stack1,stack2)
        if stack[-1]%2 ==0:
            stack1.append(stack.pop())
            print(stack,stack1,stack2)
        else: 
            stack1.append(stack2.pop())
            print(stack,stack1,stack2)
            stack1.append(stack.pop())
            print(stack,stack1,stack2)
            stack.append(stack2.pop())
            print(stack,stack1,stack2)
            stack2.append(stack1.pop())
            print(stack,stack1,stack2)
c=len(stack)
for b in range(c):
    if stack1[-1]%2 !=0:
        stack2.append(stack1.pop())
        print(stack,stack1,stack2)
        stack2.append(stack.pop())
        print(stack,stack1,stack2)
        stack1.append(stack.pop())
        print(stack,stack1,stack2)
        stack1.append(stack.pop())
        print(stack,stack1,stack2)
    elif len(stack)!=0:
        if stack[-1]%2 == 0:
            stack1.append(stack.pop())
            print(stack,stack1,stack2)
        elif stack2[-1]%2 == 0:
            stack1.append(stack2.pop())
            print(stack,stack1,stack2)
        else:
            if len(stack)!=0:
                stack2.append(stack.pop())
                print(stack,stack1,stack2)
if stack2[-1]!= 1:
    stack.append(stack2.pop())
    print(stack,stack1,stack2)
else:
    stack.append(stack1.pop())
    print(stack,stack1,stack2)
    stack.append(stack1.pop())
    print(stack,stack1,stack2)
    stack.append(stack2.pop())
    print(stack,stack1,stack2)
    stack1.append(stack2.pop())
    print(stack,stack1,stack2)
    stack1.append(stack2.pop())
    print(stack,stack1,stack2)
    stack2.append(stack.pop())
    print(stack,stack1,stack2)
    stack2.append(stack1.pop())
    print(stack,stack1,stack2)
    stack2.append(stack1.pop())
    print(stack,stack1,stack2)
    stack1.append(stack.pop())
    print(stack,stack1,stack2)
    stack1.append(stack.pop())
    print(stack,stack1,stack2)
    stack.append(stack2.pop())
    print(stack,stack1,stack2)
    stack.append(stack2.pop())
    print(stack,stack1,stack2)
if len(stack2)==2:
    if stack2[-1]!=1:
        stack.append(stack2.pop())
    else:
        stack.append(stack1.pop())
        print(stack,stack1,stack2)
        stack1.append(stack2.pop())
        print(stack,stack1,stack2)
        stack.append(stack2.pop())
        print(stack,stack1,stack2)
        stack2.append(stack1.pop())
        print(stack,stack1,stack2)
        stack2.append(stack.pop())
        print(stack,stack1,stack2)
        stack1.append(stack.pop())
        print(stack,stack1,stack2)
        stack.append(stack2.pop())
        print(stack,stack1,stack2)
