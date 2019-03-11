# Make a function to determine if a number is odd or even

def odd_even(x):
    if x%2==0:
        return "EVEN"
    return "ODD"


        # Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    numbers1=[]
    for number in numbers:
        if number%2==0:
            numbers1.append(number)
    return numbers1


    # Given a list return the unique names in the list

def unique_names(list_of_names):
    return set(list_of_names)

# Make a function that determines if a word is a palindrome


def palindrome_detector(string):
     # Run loop from 0 to len/2
    for i in range(0, len(string)/2):
        if strung[i] != string[len(strimg)-i-1]:
            return False
    return True


print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racacar'))
print(palindrome_detector('not'))
