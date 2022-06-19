import os
import os.path
from xml.etree.ElementTree import parse, Element

image_size_file = 'image_size/images_shape.txt'
with open(image_size_file, "r") as f:
    alllines = f.readlines()
    # print(data[0])
# for data in alllines:
#         # print(data)
#     print(data[0:4], ',', data[5:9])


path = "Annotations_modify/" # xml文件所在的目录
files = os.listdir(path)  # 遍历文件夹下所有文件名称
print(len(files),len(alllines))

for xmlFile, size in zip(files, alllines):  # 对所有文件进行循环遍历处理
    print(xmlFile,size)
    true_width = size[5:9]
    true_height = size[0:4]
    print(true_width, true_height)

    path1 = "Annotations_modify/" + xmlFile  # 定位当前处理的文件的路径
    newStr = os.path.join(path, xmlFile)

    dom = parse(newStr)  # 获取xml文件中的参数
    root = dom.getroot()  # 获取数据结构

    for obj in root.iter('size'):  # 获取object节点中的name子节点（此处如果要换成别的比如bndbox）
        width = obj.find('width').text  # 获取相应的文本信息
        height = obj.find('height').text
        print(width,height)
        obj.find('width').text = true_width  # 修改
        obj.find('height').text = true_height
        print('=====================================')
    dom.write(path1, xml_declaration=True)  # 保存到指定文件



