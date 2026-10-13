#__all__为一个列表，决定from My_module import *时，*所能引用的功能
__all__=['calculate_cube_volume','calculate_cube_superficial_area']

def calculate_cube_volume(length:int,width:int,height:int):
    return length*width*height

def calculate_cube_superficial_area(length:int,width:int,height:int):
    return length*width*2+length*height*2+width*height*2

def calculate_cube_density(length:int,width:int,height:int,weight:int):
    density=calculate_cube_volume(length,width,height)/weight
    return density