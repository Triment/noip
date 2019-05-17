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
    n = randint(1,1000)
    f.writelines(str(n)+'\n')
    f.writelines(func(n))



for item in range(0,10):
    inf = currentPath+'/in/main'+bytes(item+1)+'.in'
    f = open(inf,'r')
    outf = currentPath+'/out/main'+bytes(item+1)+'.out'
    of = open(outf,'w')
    intArr = []                                             # ascii码的数组
    arr = f.readlines()[1].split(' ')                       # 读取文件到int数组
    arr.pop()                                               # 清除尾部空格
    intArr = [int(x) for x in arr]                          # int数组
    strArr = [chr(x) for x in intArr]                       # 字符数组
    of.writelines(''.join(strArr))                          # 写入文件