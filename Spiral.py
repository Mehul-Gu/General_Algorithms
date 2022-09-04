#  File: Spiral.py

#  Description: Creating a fixed dimension spiral and outputting the sum of adjacent numbers based on inputs

#  Student Name: Mehul Gupta

#  Student UT EID: mdg3739

#  Partner Name: 

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/31/2022

#  Date Last Modified: 9/3/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
from multiprocessing.sharedctypes import Value
import numbers
import sys


def create_spiral ( n ):
# if n is even add one to n
  if n % 2 == 0:
    n += 1
  #creating a 2D array of 0s of size n^2
  blank_list = [[0] * n for k in range(n)] 
  #initialization
  j = 0
  state = 1
  numbers_dict = {}
  numbers_used = [None] * (n**2)
  i = 0
  k = n-1
  #main loop. Iterated through n^2 and places numbers at indexes
  while i<n**2:
    #places number at an index
    blank_list[j][k] = n**2-i
    #records which numbers have been placed to check for later
    numbers_used[i] = n**2 - i
    #adds numbers to dictionary to grab the indexes later for the adjacent sum part of this problem
    numbers_dict[n**2-i] = [j,k]
    i+=1
    #grabbing the new direction (state) and index (j,k) from the move_direction function
    j, k, state = move_direction(j,k, state, blank_list, numbers_used, n)
  return blank_list, numbers_dict

#main function to find direction and index to place numbers to make spiral
#The way this works is the code checks what direction we're moving in the spiral (state 1 = left, etc.)
#Depending on this, it changes the index appropriately to keep moving that direction
#it then checks if we've either hit the end of the 2d array or if we hit a number that has already been placed
#if so, it goes back to the previous index and then changes the 'state'/direction that the code is moving in
#this goes on until we've iterated through the whole 2d array and the while loop in create_spiral ends
def move_direction(j,k, state, blank_list, numbers_used, n):
  if (state == 1):
    j,k = move_left(j,k)
    if (k<0) or (blank_list[j][k] in numbers_used):
      j,k = move_right(j,k)
      state = 2
  if (state == 2):
    j,k = move_down(j,k)
    if (j>n-1) or (blank_list[j][k] in numbers_used):
      j,k = move_up(j,k)
      state = 3
  if (state == 3):
    j,k = move_right(j,k)
    if (k>n-1) or (blank_list[j][k] in numbers_used):
      j,k = move_left(j,k)
      state = 4
  if (state == 4):
    j,k = move_up(j,k)
    if (j<0) or (blank_list[j][k] in numbers_used):
      j,k = move_down(j,k)
      j,k = move_left(j,k)
      state = 1
  return j,k,state

#Below four functions just change index as needed to move a certain direction
def move_left(j, k):
  k-=1
  return j, k

def move_right(j, k):
  k+=1
  return j, k

def move_up(j, k):
  j-=1
  return j, k

def move_down(j, k):
  j+=1
  return j, k

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
# I've designed this to use 8 conditionals checking whether the adjacent slot exists before adding to sum
def sum_adjacent_numbers (spiral, n, numbers_dict, array_size):

  sum = 0
  list_new = numbers_dict.get(n)
  j = list_new[0]
  k = list_new[1]
  if j>0:
    sum = sum + spiral[j-1][k]
  if (j>0) and (k<array_size-1):
    sum = sum + spiral[j-1][k+1]
  if (j>0) and (k>0):
    sum = sum + spiral[j-1][k-1]
  if k>0:
    sum = sum + spiral[j][k-1]
  if (j<array_size-1) and (k>0):
    sum = sum + spiral[j+1][k-1]
  if (j<array_size-1):
    sum = sum + spiral[j+1][k]
  if (j<array_size-1) and (k<array_size-1):
    sum = sum + spiral[j+1][k+1]
  if (k<array_size-1):
    sum = sum + spiral[j][k+1]
  return sum

#main function that reads inputs and outputs the answer
def main():

  # read the size of the matrix
  array_size = sys.stdin.readline()
  array_size = array_size.strip()
  array_size = int (array_size)
  #creating the spiral and grabbing the dictionary with all values and corresponding index
  spiral, numbers_dict = create_spiral(array_size)

  i=1
  #infinite loop. Using this to keep going until we run out of numbers (ValueError)
  while i>0:
    #grabbing the number
    number = sys.stdin.readline()
    number = number.strip()
    try:
      number = int (number)
    #checking if we've gone through all numbers in the file and if so leave the loop
    except ValueError:
      break
    # checking if the number is in range and if not print 0 and then keep iterating
    if (number>(array_size**2)) or (number<1):
      print(0)
      continue
    #printing the answer
    print(sum_adjacent_numbers(spiral, number, numbers_dict, array_size))
    i+=1

if __name__ == "__main__":
  main()