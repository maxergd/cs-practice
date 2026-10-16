a = float(input())
b = float(input())
print('сумма = ', a + b)
print('разность = ' a - b)
print('произведение = ' a * b)

def divide(a, b):
    if b == 0:
	print('err/0')
	return None
    return a / b