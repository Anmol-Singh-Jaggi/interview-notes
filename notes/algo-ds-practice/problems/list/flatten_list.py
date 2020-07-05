'''
Merge the sorted lists one by one.
// The main function that flattens a given linked list
Node* flatten (Node* root)
{
    // Base cases
    if (root == NULL || root->right == NULL)
        return root;

    // Merge this list with the list on right side
    return merge( root, flatten(root->right) );
}
'''
