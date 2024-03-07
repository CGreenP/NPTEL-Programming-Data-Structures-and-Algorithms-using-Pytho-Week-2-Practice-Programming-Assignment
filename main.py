def intreverse(n):
    rev=0
    while(n!=0):
        r=n%10
        n=n//10
        rev=rev*10+r
    return (rev)

def matched(s):
    open_list = ["("]
    close_list = [")"]
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        if i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return (False)
    if len(stack) == 0:
        return (True)
    else:
        return (False)

def sumprimes(l):
    sum=0
    for num in l:
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                sum+=num
    return (sum)
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intreverse":
   arg = parse(farg)
   print(intreverse(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "sumprimes":
   arg = parse(farg)
   print(sumprimes(arg))
else:
   print("Function", fname, "unknown")

