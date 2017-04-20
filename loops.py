# 1 to 10
for i in range (1,11):
	print i

#n to m
start = int(raw_input("Start with a number: "))
end = int(raw_input("End with number: "))


for i in range (start, end + 1):
	print i


# Odd Numbers
for i in range (1, 11, 2):
	print i

# Print a Square
line = "*****" 	
box = ""
for line in line:
	box = line * 5
	print box

# Print a Square II
n = int(raw_input("How big is your square?"))
for i in range (n):
	print n * "*"

# Box
width = int(raw_input("Width?"))
height = int(raw_input("Height?"))

for i in range(width):
	if (i == 0) or (i == height - 1):
		print (width * "*")
	else:
		print "*" + (width - 2)* " " + "*"


# width = 5
# height = 3

# *****
# *   *
# *****





