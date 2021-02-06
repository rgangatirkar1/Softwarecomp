
# Inputs two integers, n and m, and outputs three n x m rectangles,
# one solid, one hollow and one checkered.  For example, for 4 and 7: 
# 
#  *******   
#  *******     
#  *******     
#  *******  
#                           
#  ******* 
#  *     *
#  *     *
#  ******* 
# 
#  * * * *
#      * * * 
#  * * * *
#   * * * 
#    

def drawSolidRectangle(n,m):
# draws solid rectangle
	for r in range(1,n+1):
		for  c in range(1,m+1): 
			print("*",end='')
		print()


def drawHollowRectangle(n,m):
# draws top row of hollow rectangle
	for c in range(1,n): 
		print("*",end='')
	print()
					
# draws inner rows of hollow rectangle
	for r in range(1,n-1): 
		print("*",end='')
		for c in range(2,m): 
			print(" ",end='')
		print("*")

#draws final row of hollow rectangle
	for c in range(0,m): 
		print("*",end='')
	print()	

    

def checkeredRectangle(n,m):
# draws checkerd rectangle
	for c in range(0,n):
		for r in range(0,m): 
			if c%2 == r%2:
				print("*",end='')
			else:
				print(" ",end='')
		print()

n = int(input("Enter the number of rows"))
m = int(input("Enter the number of columns"))
		
drawSolidRectangle(n,m)
print()
drawHollowRectangle(n,m)
print()
checkeredRectangle(n,m)
print()



