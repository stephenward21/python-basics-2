# sum the numbers
# numbs = [1, 3, 5, 7]
# print (sum(numbs))

# largest number
# numbs = [5, 1, 9, 21]
# print (max(numbs))

# smallest number
# numbs = [5, 1, 9, 21]
# print (min(numbs))


# even numbers
numbs = [4, 3, 8, 10, 11]
for x in numbs:
	if (x % 2 != 0):
		numbs.remove(x)
print (numbs)

# positive numbers I and II
numbs = [5, -3, 7, -9]
pos_numbs = []
for x in numbs:
	if (x >= 0):
		pos_numbs.append(x)
print (pos_numbs)

# Multiply a list
numbs = [4, 3, 8, 10, 11]
factor = 2
lists_multiplied = []
for i in range (0, len(numbs)):
	lists_multiplied.append(numbs[i] * factor)
print (lists_multiplied)

# Multiply Vectors
vector_one = [4, 3, 8, 10, 11]
vector_two = [2, 4, 7, 3, 1]
vectors_multiplied = []
for i in range (0, len(vector_one)):
	vectors_multiplied.append(vector_one[i] * vector_two[i])
print (vectors_multiplied)


# Matrix Addition
matrix_one = [ [1, 3], 
               [2, 4] ]
matrix_two = [ [5, 2], 
               [1, 0] ] 
matrix_three = [ ]
for i in range (0, len(matrix_one)):
	mat_next = []
	for j in range (0, len(matrix_two)):
		new_mat = matrix_one[i][j] + matrix_two[i][j]
		mat_next.append(new_mat)
	matrix_three.append(mat_next)
	print (matrix_three)







