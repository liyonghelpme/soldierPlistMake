#coding:utf8
#拷贝所有文件夹中的特征色 重新命名为ssm Id f picId .png 到allFeature 文件夹中  
import os
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
        crop = ids[id][1]
         
        print d, id, crop
        os.system('cp hfall.py '+d+'/hfall.py; cd '+d+'; python hfall.py '+str(id*10) + ' '+str(crop))

