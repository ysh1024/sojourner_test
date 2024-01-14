from method_test.serviceImpl import methodTestServiceImpl

import re

def text_replace(text):
    text = text.replace('a', '1')
    text = text.replace('b', '2')

    return text


def final_text(re_text):
    # 문자를 별도 변수에 저장
    text_val = re.sub(r'[0-9]', '', re_text)

    # 숫자를 별도 변수에 저장
    num_val = re.sub(r'[^0-9]', '', re_text)

    # 숫자의 합을 합산 후 문자열로 저장
    num_str = methodTestServiceImpl.sum_number(num_val)

    return text_val + num_str
