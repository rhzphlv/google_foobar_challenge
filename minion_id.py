def solution(num):
	prime_num = ['2']
	for i in range(3,20250,1):
		for j in range(2,i,1):
			if (i%j)==0:
				i+=1
				break
			if (j+1)==i:
				prime_num.append(str(i))
	long_text = ''.join(prime_num)
	minion_id = long_text[num:num+5]
	return minion_id

if __name__=='__main__':
	num = int(input('input number: '))
	test = solution(num)
	print(test)
	print(type(test))