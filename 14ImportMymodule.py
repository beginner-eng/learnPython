from My_module import *

#每个python文件都有一个内置变量__name__，运行此文件时会标记为__main__
if __name__ == '__main__':
    print(f"表面积为：{calculate_cube_superficial_area(2,3,4)}")
    print(f"体积为：{calculate_cube_volume(2,3,4)}")
    #使用了import *,只能使用__all__列表的内容，而calculate_cube_density不在__all__中
    #print(f"重量为：{calculate_cube_density(2,3,4)}")
    
