'''
Given a list of contacts containing username, email and phone number in any order. Identify the same contacts (i.e., same person having many different contacts) and output the same contacts together.

Notes:
1) A contact can store its three fields in any order, i.e., phone number can appear before username or username can appear before phone number.

2) Two contacts are same if they have either same username or email or phone number.


Example:

Input: contact[] =
     { {"Gaurav", "gaurav@gmail.com", "gaurav@gfgQA.com"},
       { "Lucky", "lucky@gmail.com", "+1234567"},
       { "gaurav123", "+5412312", "gaurav123@skype.com"}.
       { "gaurav1993", "+5412312", "gaurav@gfgQA.com"}
     }
Output:
   0 2 3
   1
contact[2] is same as contact[3] because they both have same
contact number.
contact[0] is same as contact[3] because they both have same
e-mail address.
Therefore, contact[0] and contact[2] are also same.


SOLUTION:

Maintain a hash-map of <key> vs <set-of-indices>.
For example:
Gaurav -> [0]
+5412312 -> [2, 3]
gaurav@gfgQA.com -> [0, 3]

Basically, name, phone and email will be the keys and the parent indices will be in the value list.
At the end, create a graph in which there is an edge between the indices of a list.
For example, if a list is [1, 5, 8, 9].
Then create the following edges:
1-5
5-8
8-9

Now, just find connected components in the resulting unweighted bidirectional graph using DFS.
'''
