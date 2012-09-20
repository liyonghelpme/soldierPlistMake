#coding:utf8
#将特征 士兵图片构建成plist png
#soldierIdm  soldierIda soldierIdf

#只是切割掉 图片的底端空白
#切割掉 左右两端 对称的空白
#吸血鬼行走文件夹名字不对

import os
import Image
import sys
#得到最小 2次幂值
def getMin2(v):
    old = v
    id = 0
    while (v>>1) > 0:
        v = v >> 1
        id += 1
    res = 1 << id
    if res < old:
        res = res << 1
    return res


#生成plist文件 不需要col
#kind soldiermId soldieraId soldierfaId soldierfmId  kind = m kind = a kind =fa kind = fm
#width 图片宽度 height 图片高度 总
#size 单个图片的大小
#num 图片的数量
#colNum 每行列的数量
#rowNum 总共行的数量

def savePlistFile(id, width, height, kind, num, size, colNum, rowNum):
    frames = {}
    for k in range(0, num):
        curCol = k%colNum
        curRow = k/colNum

        frames['ss'+str(id)+kind+str(k)+'.png'] = {
            "frame":"{{"+str(curCol*size[0])+","+str(curRow*size[1])+"},{"+str(size[0])+","+str(size[1])+"}}",
            "offset":"{0, 0}",
            "sourceSize":"{"+str(size[0])+","+str(size[1])+"}",
            "sourceColorRect":"{{0, 0}, {"+str(size[0])+","+str(size[1])+"}}",
            "rotated":False
        }

    picName = 'soldier'+kind+id+'.png'
    print kind, picName

    metadata = {"format":2, "realTextureFileName":picName, "size":"{"+str(width)+","+str(height)+"}", "textureFileName":picName}
    return {"frames":frames, "metadata":metadata}

import plistlib
#soldier Id color res/blue
#士兵 特征色 攻击 行走
def makePlist(id, solOrFea):
    #print id, solOrFea
    nim = None
    id = str(id)
    att = 'a'
    mov = 'm'
    if solOrFea == 'f':
        att = 'fa'
        mov = 'fm'
    for k in range(0, 8):#attack
        im = Image.open('ss'+id+att+str(k)+'.png')
        if nim == None:
            colNum = 1024/im.size[0]
            rowNum = (8+colNum-1)/colNum

            width = getMin2(im.size[0]*colNum)
            height = getMin2(im.size[1]*rowNum)

            nim = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        curCol = k%colNum
        curRow = k/colNum
        box = (curCol*im.size[0], curRow*im.size[1], im.size[0]*curCol+im.size[0], curRow*im.size[1]+im.size[1])
        nim.paste(im, box)
    nim.save('../tempPlist/soldier'+att+id+'.png')
    res = savePlistFile(id, width, height, att, 8, im.size, colNum, rowNum)
    plistlib.writePlist(res, '../tempPlist/soldier'+att+id+'.plist')

    nim = None
    id = str(id)
    for k in range(0, 7):#move
        im = Image.open('ss'+id+mov+str(k)+'.png')
        if nim == None:
            colNum = 1024/im.size[0]
            rowNum = (7+colNum-1)/colNum

            width = getMin2(im.size[0]*colNum)
            height = getMin2(im.size[1]*rowNum)

            nim = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        curCol = k%colNum
        curRow = k/colNum
        box = (curCol*im.size[0], curRow*im.size[1], im.size[0]*curCol+im.size[0], curRow*im.size[1]+im.size[1])
        nim.paste(im, box)

    nim.save('../tempPlist/soldier'+mov+id+'.png')
    res = savePlistFile(id, width, height, mov, 7, im.size, colNum, rowNum)
    plistlib.writePlist(res, '../tempPlist/soldier'+mov+id+'.plist')
        
        
import sys
def main(b, e, n, solOrFea):
    for i in range(b, e, 10):
        for j in range(0, n):
            id = str(i+j)
            makePlist(id, solOrFea)
print sys.argv
#col = sys.argv[1]
b = int(sys.argv[1])
e = int(sys.argv[2])
n = int(sys.argv[3])
solOrFea = sys.argv[4]
#print solOrFea == 'f'
main(b, e, n, solOrFea)
