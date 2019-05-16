from os import path,mkdir
from random import randint
p = path.abspath('.')
data = []
# if path exists
currentPath =  path.join(p,path.dirname(__file__)) 
if path.exists(currentPath+'in') and path.exists(currentPath+'out'):
    pass
else:
    mkdir(path.join(currentPath,'in'))
    mkdir(path.join(currentPath,'out'))

for item in range(0,10):
    inf = p+'/oneChapter/in/main'+bytes(item+1)+'.in'
    f = open(inf,'w')
    f.write(str(randint(1,1000)))

def func(x):
    return str(x*(x+1)/2)

for item in range(0,10):
    inf = p+'/oneChapter/in/main'+bytes(item+1)+'.in'
    f = open(inf,'r')
    outf = p+'/oneChapter/out/main'+bytes(item+1)+'.out'
    of = open(outf,'w')
    #num =int(f.readline())
    of.writelines(func(int(f.readline())))


for item in range(0,10):
    inf = p+'/oneChapter/out/main'+bytes(item+1)+'.out'
    f = open(inf,'r')
    print f.readline()