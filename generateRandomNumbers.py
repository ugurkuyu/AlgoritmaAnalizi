def get_n_random_numbers(n=10,min_=-5,max_=5):
 numbers=[]
 for i in range(n):
 numbers.append(random.randint(min_,max_))
 return numbers
get_n_random_numbers() 
