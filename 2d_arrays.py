# Function to calculate sum of all elements in matrix 
# sum(arr) is a python inbuilt function which calculates 
# sum of each element in a iterable ( array, list etc ). 
# map(sum,arr) applies a given function to each item of 
# an iterable and returns a list of the results. 
def findSum(arr): 

	# inner map function applies inbuilt function 
	# sum on each row of matrix arr and returns 
	# list of sum of elements of each row 
	return sum(arr) 

if __name__ == "__main__":
    arr=[[1,2,3],[4,5,6],[2,1,2]]

    for x in range(3):
        this_arr = arr[x]
        p= findSum(this_arr)
        print(p)
