'''
sortStack(stack S)
    if stack is not empty:
        temp = pop(S);
        sortStack(S);
        sortedInsert(S, temp);

Below algorithm is to insert element is sorted order:

sortedInsert(Stack S, element)
    if stack is empty OR element > top element
        push(S, elem)
    else
        temp = pop(S)
        sortedInsert(S, element)
        push(S, temp)
'''
