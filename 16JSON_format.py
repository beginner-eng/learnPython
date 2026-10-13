import json
#准备能转换成json的数据，列表，里面的元素为字典
data=[{"name":"zhangsan","age":23,"gender":"male"},
      {"name":"lisi","age":21,"gender":"female"},
      {"name":"王五","age":34,"gender":"male"}]

#将data转化为json格式,ensure_ascii=False可以让中文不用ASCII编码 
json_str=json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

d={"name":"周杰伦","addr":"taipei"}
json_str2=json.dumps(d,ensure_ascii=False)
print(type(json_str2))
print(json_str2)

str1='[{"name":"zhangsan","age":23,"gender":"male"},{"name":"lisi","age":21,"gender":"female"},{"name":"王五","age":34,"gender":"male"}]'
list1=json.loads(str1)#转化为了列表
print(type(list1))
print(list1)

str2='{"name":"周杰伦","addr":"taipei"}'
dict1=json.loads(str2)#转化为了字典
print(type(dict1))
print(dict1)