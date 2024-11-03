def repeat_string(input_str):
    # 分割輸入的字串和數字
    # 利用迴圈取出每個 char，並且判斷是否為數字
    text = ''.join([char for char in input_str if not char.isdigit()])
    number = int(''.join([char for char in input_str if char.isdigit()]))

    # 輸出重複的字串
    return ' '.join([text] * number)

# 範例輸入
input_str = input("請輸入字串數字（例如：熊貓3）：")
print(repeat_string(input_str))
