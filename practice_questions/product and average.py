product = 1
total = 0


n = int(input("Enter the number of inputs (n): "))


if n > 0:
    
    for i in range(n):
      
        num = float(input(f"Enter input {i + 1}: "))
        
   
        product *= num
        total += num
    

    average = total / n
    
    
    print(f"Product of inputs: {product}")
    print(f"Average of inputs: {average}")
else:
    print("Please enter a valid value for n (greater than 0).")
