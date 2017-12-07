import os
flage=0
def walkdir( dir_path, count,glass_num_list,normal_num_list):
    png_list = []
    list = os.listdir(dir_path)
    for i in list:
        #ID_list=os.listdir(dir_path+os.sep+i)
        if i == 'normal':
            png_list = os.listdir(dir_path+os.sep+i)
            normal_num = len(png_list)
            ID = dir_path.split(os.sep)[-1]
            print ("|  %-4s  | %-35s | %-10d | %-10d |  " % (
                count, ID, normal_num, glass_num))
            normal_num_list.append(normal_num)
            return

        if i == 'glass':
            png_list = os.listdir(dir_path+os.sep+i)
            glass_num = len(png_list)
            glass_num_list.append(glass_num)
            #count=count+1
            #ID = dir_path.split(os.sep)[-1]
        else:
            count=count+1
            walkdir(dir_path+os.sep+i, count,glass_num_list,normal_num_list)
    return  glass_num_list ,normal_num_list


if __name__ == '__main__':
    dir_path='D:\Share\data\output_glass'
    print ("|  %-4s  | %-35s | %-10s | %-10s |  " % (
            'ID', 'Video Name', 'normal', 'glass'))
    glass_num_list=[]
    normal_num_list=[]
    glass_num_list,normal_num_list=walkdir(dir_path,0,glass_num_list,normal_num_list)
    print ("|  %-4s  | %-35s | %-10d | %-10d |  " % (
        'xx', 'sum', sum(normal_num_list), sum(glass_num_list)))
