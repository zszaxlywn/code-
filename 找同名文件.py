import shutil
import os


def main():
    # 提取名称的目标，我们目前是txt格式
    path_label = 'C:\\Users\\zhaoshizhong\\Desktop\\新建文件夹\\Annotation'
    # 大目录，需要从里面挑出来同名的文件
    path_object = 'F:\\岩石显微数据集\\02 雅鲁藏布江砂粒显微图像数据集\\数据资料\\data\\16A063-2data\\image\\a35'
    type_object = 'jpg'
    # 备份到的输出路径
    path_output = 'C:\\Users\\zhaoshizhong\\Desktop\\新建文件夹\\images'

    for i in os.walk(path_label):
        for j in i[2]:
            p_label = os.path.join(path_label, j)
            # 注意，默认label内是txt文件，长度为3，可以根据自己情况修改
            obj_name = j[:-3] + type_object
            # 挑选出来的同名文件路径
            obj_path = os.path.join(path_object, obj_name)
            # 若找到同名的jpg文件，则拷贝出来
            if os.path.exists(obj_path) == True:
                new_path = os.path.join(path_output, obj_name)
                shutil.copyfile(obj_path, new_path)


if __name__ == '__main__':
    main()
