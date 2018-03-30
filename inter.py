file = open("Fibonacci.b", "r")
instruction = ('+', '-', '<', '>', '[', ']', ',', '.')
codeFile = file.read()

code = ''
for i in codeFile:
    if instruction.__contains__(i):
        code += i

file.close()
print(code)

# PROP
memSize = 30

pointer = 0
codePointer = 0
mem = []

for i in range(memSize):
    mem.append(0)

end = 1

while codePointer < len(code) :
    if ( code[codePointer] == '[' or code[codePointer] == ']'):
        if ( code[codePointer] == '[' ):
            if mem[pointer] != 0:
                codePointer += 1
            else:
                i = codePointer + 1
                j = 0
                while i < len(code):
                    if ( code[i] == '[' ):
                        j += 1
                    elif ( code[i] == ']' ):
                        if j :
                            j-=1
                        else :
                            codePointer = i + 1
                            break
                    i += 1
        else :
            if mem[pointer] == 0:
                codePointer += 1
            else:
                i = codePointer - 1
                j = 0
                while i >= 0:
                    if ( code[i] == ']' ):
                        j += 1
                    elif ( code[i] == '[' ):
                        if j :
                            j-=1
                        else :
                            codePointer = i + 1
                            break
                    i-=1
    else:
        if ( code[codePointer] == '>'):
            pointer += 1
        elif ( code[codePointer] == '<'):
            pointer -= 1
        elif code[codePointer] == '+':
            mem[pointer] += 1
        elif code[codePointer] == '-':
            mem[pointer] -= 1
        elif code[codePointer] == '.':
            print(chr(mem[pointer]),end='')
        else:
            a=0
        codePointer += 1

print(mem)
