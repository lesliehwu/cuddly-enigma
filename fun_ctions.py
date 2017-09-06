#Odd/Even.
def odd_even():
    for num in range(1,2001):
        if(num%2 == 1):
            typeof = "odd"
        else:
            typeof = "even"
        print("Number is", str(num) + ". This is an", typeof, "number.")

#Multiply.
def multiply(the_list,the_val):
    for num in range(len(the_list)):
        the_list[num] *= the_val
    return the_list


#Hacker Challenge.
def layered_multiples(the_list):
    for num in range(len(the_list)):
        the_list[num] *= "1"
    return the_list

#All 3 functions called.
odd_even()

a = [1,3,5]

print(multiply(a,2))

print(layered_multiples(multiply(a,2)))

