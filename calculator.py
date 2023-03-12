
quant_digit = int(input('сколько будет чисел? '))
oprnd = input('Введите операнд (+, -, *, /: )')
enter_digit = int(input(f'Введите 1 число'))
result = enter_digit

for digit in range(2, quant_digit + 1):
	enter_digit = int(input(f'Введите {digit} число'))
	if oprnd == '+':
		result += enter_digit
	elif oprnd == '-':
		result -= enter_digit
	elif oprnd == '*':
		result *= enter_digit
	elif oprnd == '/':
		result /= enter_digit
print(result)