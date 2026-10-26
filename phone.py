num = str(input("Phone number: "))
def clean_number(num):
    clean_num = num.replace(" ","").replace("-","").strip()
    return clean_num

def is_valid(num):
    num_only = clean_number(num)
    if len(num_only)==10 and num_only[0]=='0':
        return True
    return False

def digit_sum(num):
    clean_num = clean_number(num)
    count = 0
    for digit in clean_num:
        count += int(digit)
    return count

if is_valid(num) == False:
    print("Invalid phone number")
else:
    format = num.replace(" ","-").strip()
    print(f"Formatted: {format}")
    print(f"Hidden: {format[:4]}XXX{format[7:len(num)+1]}")
    print(f"Digit sum: {digit_sum(clean_number(num))}")
