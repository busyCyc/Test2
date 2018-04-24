def reverse(s):
    if len(s)<=1:
        return s
    else:
        return reverse(s[1:])+s[0]


s=input("请输入一个字符串")
print("其反转字符串为：{:s}".format(reverse(s)))