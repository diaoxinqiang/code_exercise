'''
题目:
https://www.nowcoder.com/practice/03ba8aeeef73400ca7a37a5f3370fe68?tpId=37&tqId=21250&tPage=2&rp=&ru=/ta/huawei&qru=/ta/huawei/question-ranking
'''
while True:
    try:
        input_list = input().strip().split(' ')
        word_length = int(input_list[0])
        words = input_list[1:-2]
        target_word = input_list[-2]
        target_chars = [char for char in target_word]
        target_chars = sorted(target_chars)
        brother_index = int(input_list[-1])
        words = sorted(words)
        brother_words = []
        for word in words:
            if word == target_word or len(word) != len(target_word):
                continue
            else:
                if sorted([char for char in word]) == target_chars:
                    brother_words.append(word)
        print(len(brother_words))
        brother_words = sorted(brother_words)
        if len(brother_words) > 0 and brother_index <= len(brother_words):
            print(brother_words[brother_index - 1])
    except:
        break
