import os
import random
import sys


Annotations_path = r'C:/PaddleSeg/data/histopathology_seg/Annotations/'  #标注图像路径
JPEGImages_path = r'C:/PaddleSeg/data/histopathology_seg/JPEGImages/'  #训练图像路径
AnnotationsImageName = os.listdir(Annotations_path)
JPEGImagesImageName = os.listdir(JPEGImages_path)

# 对Annotations与JPEGImages进行验证是否匹配
Jname = [i.split('.')[0] for i in JPEGImagesImageName]
Aname = [i.split('.')[0] for i in AnnotationsImageName]
err = [i for i in Jname if i not in Aname]
if err==[]:
    print('图像对应')
else:
    print('Annotations缺少'+','.join(err) )
    sys.exit(0)

# 划分数据集
Num = len(JPEGImagesImageName)
trainNum = int(Num*0.8)  # 80%为训练集
# valNum = int(Num*0.1)  # 10%为验证集
# testNum = Num - trainNum - valNum # 剩下的为测试集
testNum = Num - trainNum # 剩下的为测试集
trainImagename = random.sample(JPEGImagesImageName, trainNum) 
No_trainImagename = [i for i in JPEGImagesImageName if i not in trainImagename]
# valImagename = random.sample(No_trainImagename, valNum)
# No_valImagename = [i for i in No_trainImagename if i not in valImagename]
testImagename = random.sample(No_trainImagename, testNum)

# 写入txt
with open("train_list.txt","w") as f: # 训练集写入
    for name in trainImagename:
        # f.write(JPEGImages_path+name+' '+Annotations_path+AnnotationsImageName[Aname.index(name.split('.')[0])]+'\n')
        f.write('JPEGImages/'+ name + ' ' + 'Annotations/' + AnnotationsImageName[
            Aname.index(name.split('.')[0])] + '\n')
# with open("val.txt","w") as f:  #验证集写入
#    for name in valImagename:
#        f.write(JPEGImages_path+name+' '+Annotations_path+AnnotationsImageName[Aname.index(name.split('.')[0])]+'\n')
with open("test_list.txt","w") as f:  # 测试集写入
    for name in testImagename:
        # f.write(JPEGImages_path+name+' '+Annotations_path+AnnotationsImageName[Aname.index(name.split('.')[0])]+'\n')
        f.write('JPEGImages/' + name + ' ' + 'Annotations/' + AnnotationsImageName[
            Aname.index(name.split('.')[0])] + '\n')