original_wheel = ['ZWAXJGDLUBVIQHKYPNTCRMOSFE',
                  'PBELNACZDTRXMJQOYHGVSFUWI',
                  'BDMAIZVRNSJUWFHTEQGYXPLOCK',
                  'RPLNDVHGFCUKTEBSXQYIZMJWAO',
                  'IHFRLABEUOTSGJVDKCPMNZQWXY',
                  'AMKGHIWPNYCJBFZDRUSLOQXVET',
                  'GWTHSPYBXIZULVKMRAFDCEONJQ',
                  'NOZUTWDCVRJLXKISEFAPMYGHBQ',
                  'XPLTDSRFHENYVUBMCQWAOIKZGJ',
                  'UDNAJFBOWTGVRSCZQKELMXYIHP',
                  'MNBVCXZQWERTPOIUYALSKDJFHG',
                  'LVNCMXZPQOWEIURYTASBKJDFHG',
                  'JZQAWSXCDERFVBGTYHNUMKILOP ']#所给初始状态的轮转机
shifted_wheel = []
key = [2,3,7,5,13,12,9,1,8,10,4,11,6] #所给密钥
ciphertext = 'NFQKSEVOQOFNP' #所给密文

#按照密钥顺序对轮排序
for i in key:
    shifted_wheel.append(original_wheel[i-1])
print('按照密钥重新排序后的轮转机：\n',shifted_wheel)

#按照密文顺序转动轮
for i in range(len(shifted_wheel)):
    index = shifted_wheel[i].index(ciphertext[i])
    shifted_wheel[i] = shifted_wheel[i][index:]+shifted_wheel[i][0:index]
print('按照密文重新排序后的轮转机：\n',shifted_wheel)

#读取所有恢复的明文
print('输出所有可能的明文：')
for i in range(1,len(shifted_wheel[0])):
    for j in range(len(shifted_wheel)):
        print(shifted_wheel[j][i],end='')
    print('\n')