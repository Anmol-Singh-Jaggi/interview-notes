# Round 1

## Problem 1: Implement FB notification algorithm.

```
Data :
Person -> P
Person - Person relationship -> P-P (friendship, factor1 : 1-10, depends on the closeness)
Notification -> N
Person - Notification -> P-N (relationship, factor2 : 1-10, depends on the importance of notification)
```

Algo to find the top k notifications (for a person from his/her friends) based on sum of factor1 & factor2

DS to store the data.

## Solution 1

```
Friend
{
    int closeness;
    notifications[]
}

Input -> friends[]
output-> notifications[]

Person
{
    closeness[] -> size=graph.size() // sorted, size can be maximum number of friends
    notifications[] // sorted, size can be number of notifications a person can have
}
```

- Iterate through the closest k persons.
- Insert k most important notifications with the value factor1+factor2 into a min-heap.
- Extract the first k elements from the heap.
- Sample Data :
  - First Friends - factor1 = 1 - notifications : factor2 = 1 (k notifications)
  - First k friends - factor1 varying from 1 to 4 - notifications varying from 9 to 10
  - k + 1 friend - factor1 equal to 5 - notifications varying factor2 1

## Solution 2

- Iterate through all the friends.
- Important Question : After getting first k notifications from closest friends, how do you decide whether to go through the next-closest friend or not?
- We can check if the most important notification from the next closest friend is strictly less than the greatest (maximum sum of factor1 and factor2) we currently have in our min-heap
- Important Question 2 : If the first notification is actually strictly less than one of the notification is the min-heap, and the friend has 1000s of notifications, how do we go about that?
- Go through the notifications till the point the point where the notification stops to satisfy the strictly lesser than the greatest min-heap notification
- Imporant Question 3 : Do we go through all the friends?
- If factor1 is not strictly less than the greatest min-heap notification, we skip the friend and the remaining ones.


## Problem 2: You have to write a function which takes an array storing a tree in it, and return the height of the tree.

- Rules:
  - Every array element is a tree node.
  - Value of an array element is actually the index of its parent element.
  - The value stored in the root element is -1.
- Sample Array:
```
   0  1  2  3  4  5  6  7  8  9
   2  3  3  8  3 -1  9  9  5  8

            5
            8
       3          9
   1   2  4     6   7
       0

Sample Output => 5
```

## Solution 1 :
- Array for storing the height and map for remembering the children of a node
- Time Complexity : n log n
- Space Complexity : n

```cpp
function (array arr, size n)
{
    vector<int> heights(n,-1);
    unordered_map<int, set<int> > mapping;
    map<int, set<int> >::iterator it;

    for(i=0;i<n;i++)
    {
        mapping[arr[i]].insert(i);
    }

    // 2->(1,4,3)
    heights[mapping[-1]] = 1;
    for(it = mapping.begin();
    // return height
    return height
}
```

## Solution 2:
- Creating hash-map instead of map.
- Time Complexity : n
- Space Complexity : ?

## Solution 3:
- Find any node not present in the array, loop upwards.
- Loop upwards through all the leaves.
- Time Complexity : n log n.

## Solution 4:
- All nodes -> recurse upwards and save heights at negative.
- Time Complexity -> n.
- Space Complexity -> constant.

```
   0  1  2  3  4  5  6  7  8  9
   2  3  3  8  3 -1  9  9  5  8

            5
            8
       3          9
   1   2  4     6   7
       0

Sample Output => 5
```

Code :

```cpp
int getHeightHelper(vector<int>& arr, int i)
{
    if(arr[i]<0)
    {
        return arr[i];
    }

    int parentHeight = getHeightHelper(arr, arr[i]);
    arr[i] = parentHeight-1;

    return arr[i];
}

int getHeight(vector<int>& arr)
{
    if(arr.empty())
        return 0;

    for(int i=0; i<arr.size(); i++)
    {
        getHeightHelper(arr, i);
    }

    return (*min_element(arr.begin(), arr.end())) * -1;
}
```

# Round 2

- Design TinyURL.
- Convert doubly linked list to tree (and vice-versa).