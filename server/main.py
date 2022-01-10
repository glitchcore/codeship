from time import sleep

my_code = '''
x = 10
print(y)
print(x)
'''

y = 2
for line in my_code.splitlines():
	print(f"line: {line}")
	exec(line)
	sleep(1)

print(x)