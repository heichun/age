driving = input('有無開過車?')
age = input('請問幾AGE?')
age = float(age)

if driving != 'yes' and driving != 'no':
	print('只可以入YES/no')
	
if driving == 'yes':
	if age >= 18:
		print('你通過了')
	else:
		print('奇怪,你開過?')
elif driving == 'no':
	if age >= 18:
		print('你可以學車' )
	else:
		print('過2年可以學')
else:
	print('只可入NO/YES')
