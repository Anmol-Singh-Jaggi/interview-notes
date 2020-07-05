'''
Implement data structure “Map” storing pairs of integers (key, value) and define following member functions in O(1) runtime:
void insert(key, value), void delete(key), int get(key), int getRandomKey().

SOLUTION:

Keep a hashmap of kry-value pairs.
Apart from that, keep all the keys in an array (vector).
Insertions in the vector are amortized O(1).
But deletion are O(n).
But we can do something clever; rather than deleting it normally, we can just swap the last element over the deleted element.
For example, if the array is [1, 6, 3, 2 ,5] and rand()%5 returned 2.
So we can simply replace 3 with 5 and change the length variable to 4.
So, we'll have to keep a variable 'length' also.
'''
