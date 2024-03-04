import random

def get_value(node):
	sum_val = 0
	addend_val1 = 0
	addend_val2 = 0
	
	for i in node[2]:
		sum_val = 10*sum_val + elements[i]
	
	for i in node[0]:
		addend_val1 = 10*addend_val1 + elements[i]

	for i in node[1]:
		addend_val2 = 10*addend_val2 + elements[i] 

	return abs(sum_val - (addend_val1+addend_val2))

def iterate(elements,add1,add2,add_sum):
	node = [add1,add2,add_sum]
	curr_val = get_value(node)	
	print(curr_val)
	
	i = random.choice(list(elements.items()))[0]
	j = random.choice(list(elements.items()))[0]
	while True:
	
		temp = elements[i]
		elements[i] = elements[j]
		elements[j] = temp

		node = [add1,add2,add_sum]
		node_val = get_value(node)
		print(node_val)

		if node_val<curr_val:
			curr_node = node
			curr_val = node_val

		if node_val == 0:
			print("done")
			return elements


		i = random.choice(list(elements.items()))[0]
		j = random.choice(list(elements.items()))[0]
		break
		


add1 = 'SEND' #input("Enter 1st string")
add2 = 'MORE' #input("Enter 2nd string")
add_sum = 'MONEY' #input("Enter the sum of the numbers")

elements = {}
numbers = [0,1,2,3,4,5,6,7,8,9]
for i in add1:
	if i not in elements.keys():
		elements[i] = numbers.pop(0)
		
for i in add2:
		if i not in elements.keys():
			elements[i] = numbers.pop(0)

for i in add_sum:
	if i not in elements.keys():
		elements[i] = numbers.pop(0)

print(elements)
elements = iterate(elements,add1,add2,add_sum)
print(elements)
