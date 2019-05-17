#coding=utf-8
from os import path,mkdir
from random import randint
p = path.abspath('.')
data = []
# if path exists
currentPath =  path.join(p,path.dirname(__file__)) 
print "dirictory:" + currentPath
if path.exists(currentPath+'/in') and path.exists(currentPath+'/out'):
    pass
else:
    mkdir(path.join(currentPath,'in'))
    mkdir(path.join(currentPath,'out'))
# 创建随机ascii码
def func(x):
    s = ''
    for i in range(0,x):
        s+=str(randint(32,127))+' '
    return s
# 创建文件
for item in range(0,10):
    inf = currentPath+'/in/main'+bytes(item+1)+'.in'
    f = open(inf,'w')
    n = randint(1,27)
    c = chr(randint(65, 65+25))
    f.writelines(c+ ' ' + str(n)+'\n')                           # 写入一个字母和一个整数



for item in range(0,10):
    inf = currentPath+'/in/main'+bytes(item+1)+'.in'
    f = open(inf,'r')
    outf = currentPath+'/out/main'+bytes(item+1)+'.out'
    of = open(outf,'w')
    [a, b]=f.readlines()[0].strip().split(' ')
    for i in range(0,int(b)):
        if(i==0):
            print ' '*(int(b)-i) + a
        else:
            if(ord(a)+i>90):
                a = 'A'
                c = chr(65+i)
                print ' '*(int(b)-i) + c + ' '*2*i + c
            else:
                c = chr(ord(a)+i)
                print ' '*(int(b)-i) + c + ' '*2*i + c
        
        
def getch(x):
    if(ord(x)+1>ord('Z')):
        return 'A'
    else:
        return x