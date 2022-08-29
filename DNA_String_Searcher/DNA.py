#  File: DNA.py

#  Description: Python file to find the longest common substring

#  Student Name: Mehul Gupta

#  Student UT EID: mdg3739

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 8/28/2022

#  Date Last Modified: 8/29/2022

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
# This specific function will take two substrings and output the longest common substring
def longest_subsequence (s1, s2):
    #defining some variables
    common_seq = ""
    longest_current_seq = ""
    counter = 1
    answer = [None]
    k = 0
    j = 0
    #making sure the string being used in the outer loop is longer than the one for the innter loop and changing the variables if this isn't so
    if len(s2) > len(s1):
        temp = s1
        s1 = s2
        s2 = temp
    #double loop that is iterating through every character in both strings and finding the matching substrings
    while j < (len(s1)):
        s1_letter = s1[j]
        addition = 1
        while k < (len(s2)):
            s2_letter = s2[k]
            if s1_letter == s2_letter:
                common_seq = common_seq + s1_letter
                try:
                    s1_letter = s1[j+addition]
                except IndexError:
                    break
                else:
                    addition = addition + 1
                    k+=1
            else:
                k+=1
                break
        #Checking for if there's a new longest_current_seq
        if len(common_seq) > len(longest_current_seq):
            answer = [None]
            longest_current_seq = common_seq
            answer[0] = longest_current_seq
            counter = 1
            common_seq = ""
        #Checking for if there are two substrings of the same length that are different
        elif (len(common_seq) == len(longest_current_seq)) and (common_seq != longest_current_seq):
            answer.append(common_seq)
            counter = counter + 1
            common_seq = ""
        else:
            common_seq = ""
        #Messing around with loop iterations in order to iterate through the whole string completely
        if k == (len(s2)):
            j+=1
            k = 0
        if j == (len(s1)-1):
            break
    answer.sort()
    return answer


def main():
  # read the number of pairs
  num_pairs = sys.stdin.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # for each pair call the longest_subsequence
  for i in range (num_pairs):
    st1 = sys.stdin.readline()
    st2 = sys.stdin.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper()
    st2 = st2.upper()

    # get the longest subsequences and printing them
    long_sub = longest_subsequence (st1, st2)
    try:
        if len(long_sub[0]) > 1:
            long_sub.append(long_sub)
            print(long_sub)
        else:
            print("No Common Sequence Found")
    except TypeError:
        print("No Common Sequence Found")

    # insert blank line
    print("\n")
if __name__ == "__main__":
  main()
