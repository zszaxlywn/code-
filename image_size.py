import cv2
import os
import natsort as nt#引入natsort顺序读取时使用
x=0#为了计数即图片的数量
url = 'D:/Program Files/muba/yolov5muba/data/images/'#记录图片地址为了后续拼接地址
file_list = nt.natsorted(os.listdir(r'D:/Program Files/muba/yolov5muba/data/images/') )# 顺序读取目录下的所有文件
for filename in file_list:
    x+=1
    print("第{}张图片".format(x))
    print(filename)
    dirs = url + filename  # 目录与文件名拼接构成完整目录
    img1 = cv2.imread(dirs)   #读取图片
    cv2.imshow("img",img1)     #展示图片
    size = img1.shape           #图片的shape赋给size
    print (size)                #输出size例如(512, 512, 3)
    height = size[0]            #将size中第一个元素赋给height
    width =  size[1]            #将size中第二个元素赋给width
    with open("val2017.shapes","a+") as f:      #打开文件并追加写，没有就创建
        # f.write(str(filename))                    #可以写入文件名
        f.write(str(height))  # 写入height
        f.write(" ")  # 写入空格
        f.write(str(width))  # 写入width
        f.write("\n")  # 写入换行
        #Python引入了with语句来自动帮我们调用close()方法：
    print("第{}张图片写入成功".format(x))
