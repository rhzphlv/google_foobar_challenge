def solution(lamb):
	pelit =[1]
	i = 0
	while sum(pelit)<=lamb:
		pelit.append(pelit[i]*2)
		i+=1


	baik =[1,1]
	i = 0 
	while sum(baik)<=lamb:
		baik.append(baik[i]+baik[i+1])
		i+=1
	
	return abs(len(pelit[:-1])-len(baik[:-1]))

if __name__ == '__main__':
	lamb = int(input('Total lambs:'))
	difference_hencemen = solution(lamb)
	print(difference_hencemen)