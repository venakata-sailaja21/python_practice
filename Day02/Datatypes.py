#=========================
# 1.Type of DataType
#=========================
a=10
b=10.0
c='a'
d='sailu'
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#==========================
# 2. Float 
#==========================
x=10.5
print(type(x))
#-------------------------
print(10e1)
print(10e+1)#same as 10e1
print(10e2)
print(10e+2)#same as 10e2
print(10e3)
print(2e4)
print(10e-1)
print(10e-2)
#=========================


#==========================
# 3.String
#==========================
str1='Sailu'
str2="Sailu"
print(str1)
print(str2)
#----------------------------------------
# To highlet the a string in a sentence
#----------------------------------------
str3="I am learning 'python'"
print(str3)
print(type(''))
#----------------------------------------
# Length
#----------------------------------------
print(len(''))
print(len('       '))
str1='sailu'
str2='sailu   '
# It seems to be same answer but it varries in length so if we are working through iteration then we will face problem if you include a single space
print(f'String: {str1},Length of the string: {len(str1)}')
print(f'String: {str2},Length of the string: {len(str2)}')


#===================================
# 4.Boolean
#===================================
print(type(True))
print(type(False))
print(10==10)
#10=10#wrong
a=10#assigning the variable
a==10#asking to compare
#--------------------------------
# Examples
#--------------------------------
print(True)         
print(False)          

# Comparison operators
print(10 > 5)       
print(10 < 5)          
print(10 == 10)        
print(10 != 10)     

# Using bool()
print(bool(1))        
print(bool(0))         
print(bool("Python"))  
print(bool(""))        
print(bool([1, 2]))    
print(bool([]))        
print(bool(None))     

# Logical operators
print(True and False) 
print(True or False)  
print(not True)      

