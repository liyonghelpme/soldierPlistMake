#coding:utf8
#只是切割掉 图片的底端空白
#切割掉 左右两端 对称的空白
#吸血鬼行走文件夹名字不对
#泰坦图片左侧存在1像素的白线 需要先切割掉 再crop

import os
import Image
import sys
import ImageOps
import json

#读取士兵图片的边沿 根据士兵 图片 切割 特征色图片的边沿
fi = open('../mb.txt', 'r')
fi = json.loads(fi.read())
#mId aId

print sys.argv
b = int(sys.argv[1])
e = int(sys.argv[2])
n = int(sys.argv[3])

def cropBound(id):
    maxBoundary = fi['a%d' % id]
    for k in range(0, 8):
        im = Image.open('ssa'+str(id)+'f'+str(k)+'.png') 
        nim = im.crop(maxBoundary)
        nim.save('ss'+str(id)+'fa'+str(k)+'.png')

    maxBoundary = fi['m%d' % id]
    for k in range(0, 7):
        im = Image.open('ssm'+str(id)+'f'+str(k)+'.png') 
        nim = im.crop(maxBoundary)
        nim.save('ss'+str(id)+'fm'+str(k)+'.png')


def main():
    for i in range(b, e, 10):
        for j in range(0, n):
            cropBound(i+j)

    os.system('rm ssa*')
    os.system('rm ssm*')
main()
