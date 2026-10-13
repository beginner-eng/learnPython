# 比较字符串的大小，比较规则为：从左到右逐个比较字符串中的字符的ASCII码值，
# 直到遇到不同的字符为止，如果一个字符串是另一个字符串的前缀，那么较长的字符串更大
print(f"abd>abcd的结果为：{'abd'>'abcd'}")

print(f"ab>a的结果：{'ab'>'a'}")

print(f"a>A结果：{'a'>'A'}")#a=97 A=65

print(f"key2>key1的结果是：{'key2'>'key1'}")