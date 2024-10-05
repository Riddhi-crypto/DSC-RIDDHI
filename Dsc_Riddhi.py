'''ques1 1. Arrange words in a string in the order of their length.
Write a function that inputs a string. The function should return the string sorted in ascending order of the length of the words.

Example Test Case:Input: "This is a cool sentence"
Output: "a is this cool sentence"
'''

#code in python
def sort_words_by_length(input_str):
    # Split the string into words
    words = input_str.split()
    
    # Sort the words based on their length
    words.sort(key=len)
    
    # Join the sorted words back into a single string
    return ' '.join(words)

if __name__ == "__main__":
    input_str = input("Enter a sentence: ")		#Input:"This is a cool sentence"
    print(sort_words_by_length(input_str))




''' ques 2 Remove duplicates from array
Write a function that inputs an array. This function should return an array that has the elements in the same order, but with each element appearing only once. Assume the input array is already sorted.

Example Test Case: 
Input: [2,3,4,4,6,7,7]
Output: [2,3,4,6,7]  
'''

# code in python
def remove_duplicates(arr):
    # Initialize the result list with the first element
    result = []
    
    # Iterate through the array
    for num in arr:
        # Add to result if it's not already the last element in result
        if not result or num != result[-1]:
            result.append(num)
    
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted integers separated by spaces: ").split())) 		#Input: [2,3,4,4,6,7,7]
    print(remove_duplicates(arr))



'''ques 3  Print the date based on the entered day and year
Write a function that inputs two integers: the day number and the year. This function should generate a string that has the entire date with the date, month and year mentioned. Ensure that the function also considers leap years.

Example Test Case:
Inputs:  256, 2021
Output: “13 September, 2021”
'''

# code in python
from datetime import datetime, timedelta

def day_of_year_to_date(day, year):
    # Starting date of the given year
    start_date = datetime(year, 1, 1)
    
    # Adding the day number to the starting date
    date = start_date + timedelta(days=day-1)
    
    # Formatting the date in the desired format
    return date.strftime("%d %B, %Y")

if __name__ == "__main__":
    day, year = map(int, input("Enter the day number and year separated by space: ").split())		#Inputs:  256, 2021
    print(day_of_year_to_date(day, year))



'''ques 4 The bottle shipping problem
A company manufactures packing cartons in four sizes: small, medium, large and xl. These cartons can hold 6 bottles, 12 bottles, 24 bottles and 48 bottles respectively.
//Write a function that inputs the number of bottles to be shipped by the company. The function should print the break-up of the number of cartons used in descending order of capacity.

Example Test Case:
Input: 140
Output: 2 xl, 1 large, 1 medium, 1 small 
'''
#code in python
def bottle_shipping(num_bottles):
    carton_sizes = [48, 24, 12, 6]
    carton_names = ['xl', 'large', 'medium', 'small']
    result = []

    for i in range(len(carton_sizes)):
        count = num_bottles // carton_sizes[i]
        if count > 0:
            result.append(f"{count} {carton_names[i]}")
        num_bottles %= carton_sizes[i]

    return ", ".join(result)

if __name__ == "__main__":
    num_bottles = int(input("Enter the number of bottles to be shipped: "))		#Input: 140
    print(bottle_shipping(num_bottles))
