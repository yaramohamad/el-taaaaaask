l = ('apples')  
l1 = ('apples' 'and oranges')  
l2 = ('apples,' 'oranges' 'and bananas')  
l3 = ('apples,' 'oranges,' 'bananas,' 'and lemons')  
n = int(input("Enter a number (1-4): "))  
if n == 1:  
    print(l)  
elif n == 2:  
    print(l1)  
elif n == 3:  
    print(l2)  
elif n == 4:  
    print(l3)  
else:  
    print("Invalid input, please enter a number between 1 and 4.")