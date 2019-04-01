def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result  

lis = input()

for let in lis:
	let = swap_case(let)
	print(let, end = "")
