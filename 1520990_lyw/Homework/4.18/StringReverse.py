def reverse(str):
    if len(str)<=1:
        return str
    else:
        return reverse(str[1:])+str[0]


if __name__ == '__main__':
    str = input("请输入一个字符串: ")
    print("反转后的字符串为: "+format(reverse(str)))





