'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
复制
abcdd
输出
复制
dd
'''

while True:
    try:
        input_str = input().strip()
        map = {}
        for char in input_str:
            if char in map.keys():
                map[char] += 1
            else:
                map[char] = 1
        new_str = ''
        min_count = min(map.values())

        for char in input_str:
            if map[char] != min_count:
                new_str += char
        print(new_str)
    except:
        break
