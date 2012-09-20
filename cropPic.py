#coding:utf8
#只是切割掉 图片的底端空白
#切割掉 左右两端 对称的空白
#吸血鬼行走文件夹名字不对
#泰坦图片左侧存在1像素的白线 需要先切割掉 再crop

import os
import Image
import sys
import ImageOps

#key: mid:--->
res = {}
#计算编号id 的 攻击图片 和 移动图片的 maxBoundary 
#保存到
def cropBound(id):

    print 'cropBound', id
    maxBoundary = [1000, 1000, 0, 0]
    for k in range(0, 8):#attack
        im = Image.open('ss'+str(id)+'a'+str(k)+'.png') 

        #需要使用两种技术分别 处理 图片的左右和上下空白
        #直接getbbox  做灰度图 之后 getbbox
        #nim = im.convert('L')
        #nim = ImageOps.invert(nim)
        #nim = nim.crop([1, 0]+list(nim.size))

        box = list(im.getbbox())
        size = im.size
        if box[2] == size[0] and box[3] == size[1]:
            print "notBox", id
            nim = im.convert('L')
            nim = ImageOps.invert(nim)
            nim = nim.crop([1, 0]+list(nim.size))
            box = list(nim.getbbox())
            
        print box, size
        midX = im.size[0]/2
        difx = max(abs(box[0]-midX), abs(box[2]-midX))
        box[0] = midX-difx
        box[2] = midX+difx

        if box[0] < maxBoundary[0]:
            maxBoundary[0] = box[0]
        if box[1] < maxBoundary[1]:
            maxBoundary[1] = box[1]
        if box[2] > maxBoundary[2]:
            maxBoundary[2] = box[2]
        if box[3] > maxBoundary[3]:
            maxBoundary[3] = box[3]
    print id, 'a', maxBoundary
    res['a%d'%(id)] = maxBoundary
    for k in range(0, 8):
        im = Image.open('ss'+str(id)+'a'+str(k)+'.png') 
        nim = im.crop(maxBoundary)
        nim.save('ss'+str(id)+'a'+str(k)+'.png')

    maxBoundary = [1000, 1000, 0, 0]
    for k in range(0, 7):#move
        im = Image.open('ss'+str(id)+'m'+str(k)+'.png') 

        #nim = im.convert('L')
        #nim = ImageOps.invert(nim)
        #nim = nim.crop([1, 0]+list(nim.size))

        box = list(im.getbbox())

        size = im.size
        if box[2] == size[0] and box[3] == size[1]:
            print "notBox", id
            nim = im.convert('L')
            nim = ImageOps.invert(nim)
            nim = nim.crop([1, 0]+list(nim.size))
            box = list(nim.getbbox())
        print box, size

        midX = im.size[0]/2
        difx = max(abs(box[0]-midX), abs(box[2]-midX))
        box[0] = midX-difx
        box[2] = midX+difx

        if box[0] < maxBoundary[0]:
            maxBoundary[0] = box[0]
        if box[1] < maxBoundary[1]:
            maxBoundary[1] = box[1]
        if box[2] > maxBoundary[2]:
            maxBoundary[2] = box[2]
        if box[3] > maxBoundary[3]:
            maxBoundary[3] = box[3]
    print id, 'm', maxBoundary
    res['m%d'%(id)] = maxBoundary
    for k in range(0, 7):
        im = Image.open('ss'+str(id)+'m'+str(k)+'.png') 
        nim = im.crop(maxBoundary)
        nim.save('ss'+str(id)+'m'+str(k)+'.png')

fi = open('../mb.txt', 'w')
print sys.argv
b = int(sys.argv[1])
e = int(sys.argv[2])
n = int(sys.argv[3])
def main():
    for i in range(b, e, 10):
        for j in range(0, n):
            cropBound(i+j)

main()
import json
fi.write(json.dumps(res))
fi.close()
