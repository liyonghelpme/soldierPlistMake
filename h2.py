#coding:utf8
#魔法师文件夹名字不对
import os
#10*4 = 40 * 8 
#*7move *8 attack

#拷贝所有 文件夹中 行走 战斗 图片到 allPic 
#不进行切割

ids = [
["剑士", 1],  ["吸血鬼", 0],  ["弓箭手",1 ], ["骑士", 1], ["精灵", 1], ["泰坦", 1], ["火焰魔法师", 1], ["龙骑士", 1], ["矮人", 1], ["天使", 0], 
]

allDir = os.listdir('.')
for d in allDir:
    if os.path.isdir(d):
        id = -1
        for k in ids:
            if k[0] == d:
                id = ids.index(k)
                break
        if id == -1:
            continue
        #crop = ids[id][1]
        crop = 0
         
        print d, id, crop
        os.system('cp han.py '+d+'/han.py; cd '+d+'; python han.py '+str(id*10) + ' '+str(crop))

