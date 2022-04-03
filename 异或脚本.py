key = input("Input key:")
for i in range(0,127):
    for j in range(0,127):
        result=i^j
        if(chr(result) is key ):
            print('("'+chr(i)+'"^"'+chr(j)+'")=='+chr(result)+'   chr('+str(i)+')^chr('+str(j)+')=='+chr(result))
