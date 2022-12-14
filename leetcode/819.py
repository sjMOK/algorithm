import re

def most_common_word(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() 
            if word not in banned]

    count_dict = {}
    for word in words:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1

    
    sorted_dict = sorted(count_dict.items(), reverse=True, key=lambda x: x[1])
    return sorted_dict[0][0]
