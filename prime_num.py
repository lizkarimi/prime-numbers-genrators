
def list_prime_numbers(last):
prime_number_list = []
for num in range (0, int(last)):
	if check_if_prime(num):
		prime_number_list.append(num)
	return prime_number_list


""""conditional statements to be checked first"""
def check_if_prime(n):
	if (n == 2 or n == 3):
		return True
	if n <= 1:
		return False
	else: 
#use else instead of elif to get the rest, the other part is more than 2 so....
		for i in range(3, n):
	if ((n % 2 == 0) or (n % 3 == 0) or ( n % i == 0)): #change applied
		return False
		return True
print(list_prime_numbers(50))