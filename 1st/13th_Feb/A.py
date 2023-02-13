# 길이 입력
lenth = int(input())

# 암호문 입력
input_password = list(map(int, input().split()))

# 기대 평문 입력
expected_string = input()


encoding_number_list = list()
# TODO: 평문을 암호화
for i in input_password:
    if i == " ":
        encoding_number_list.append("0")
        # print("띄어쓰기입니다.")
    elif 1 <= ord(i) - 64 <= 26:  # TODO: 대문자인 경우
        encoded_number = ord(i) - 64
        encoding_number_list.append(encoded_number)
        print("대문자 입니다.")
    elif 27 <= ord(i) - 70 <= 52:  # TODO: 소문자인 경우
        encoded_number = ord(i) - 70
        encoding_number_list.append(encoded_number)
        print("소문자 입니다.")

count = 0
for i in encoding_number_list:
    for j in input_password:
        if i == j:
