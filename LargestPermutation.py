"""
Problem Description

Given an integer array A of size N consisting of unique integers from 1 to N. You can swap any two integers atmost B times.

Return the largest lexicographical value array that can be created by executing atmost B swaps.

Example Input
Input 1:

 A = [1, 2, 3, 4]
 B = 1
Input 2:

 A = [3, 2, 1]
 B = 2


Example Output
Output 1:

 [4, 2, 3, 1]
Output 2:

 [3, 2, 1]


Example Explanation
Explanation 1:

 In one swap we can swap (1, 4) so that the array becomes : [4, 2, 3, 1].
Explanation 2:

 Array is already the largest lexicographical value array.

"""


class Solution:
  def largest(arr, k):
    n = len(arr)
    d= {}
    for i in range(n):
      d[arr[i]] = i
      
    for i in range(n):
      # if k is 0.
      if k == 0:
        break
      
      # if highest value is already present.
      if arr[i]==n-i:
        continue
      
      t = d[n-i]
      
      # swap elements
      
      d[n-i], d[arr[i]] = i, d[n-i]
      arr[t], arr[i] = arr[i], arr[t]
      k-=1
    return arr
    
    
