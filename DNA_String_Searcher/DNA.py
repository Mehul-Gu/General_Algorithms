#  File: DNA.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence (s1, s2):
    common_seq = ""
    longest_current_seq = ""
    counter = 1
    answer = [None]
    if len(s2) > len(s1):
        temp = s1
        s1 = s2
        s2 = temp
    for j in range (len(s1)):
        s1_letter = s1[j]
        addition = 1
        for k in range (len(s2)):
            s2_letter = s2[k]
            if s1_letter == s2_letter:
                common_seq = common_seq + s1_letter
                try:
                    s1_letter = s1[j+addition]
                except IndexError:
                    addition = addition - 1
                else:    
                    addition = addition + 1
            else:
                s1_letter = s1[j]
                common_seq = ""
        if len(common_seq) > len(longest_current_seq):
            answer = [None]
            longest_current_seq = common_seq
            answer[0] = longest_current_seq
            counter = 1
            common_seq = ""
        elif (len(common_seq) == len(longest_current_seq)) and (common_seq != longest_current_seq):
            answer.append(common_seq)
            counter = counter + 1
            common_seq = ""
        else:
            common_seq = ""
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

    # get the longest subsequences
    long_sub = longest_subsequence (st1, st2)
    try:
        if len(long_sub[0]) > 1:
            long_sub.append(long_sub)
            print(long_sub)
        else:
            print("No Common Sequence Found")
    except TypeError:
        print("No Common Sequence Found")
    # print the result

    # insert blank line
    print("\n")
if __name__ == "__main__":
  main()
