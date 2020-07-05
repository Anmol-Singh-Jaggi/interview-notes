import heapq
from ds.tree.binary_tree import BinaryTreeNode


def get_huffman_tree(msg):
    char_freq = {}
    for ch in msg:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    heap = []
    for ch, freq in char_freq.items():
        node = BinaryTreeNode((freq, ch))
        heapq.heappush(heap, node)
    root = None
    while heap:
        first = heapq.heappop(heap)
        if not heap:
            root = first
            break
        second = heapq.heappop(heap)
        new_freq = first.data[0] + second.data[0]
        # Non-leaf nodes are not associated with any character!
        new_node = BinaryTreeNode((new_freq, ""), first, second)
        heapq.heappush(heap, new_node)
    return root


def populate_encoding_map(root, current_encoding, encoding_map):
    if root.is_leaf():
        encoding_map[root.data[1]] = current_encoding
        return
    populate_encoding_map(root.left, current_encoding + "0", encoding_map)
    populate_encoding_map(root.right, current_encoding + "1", encoding_map)


def get_encoding_map(huffman_tree_root):
    encoding_map = {}
    if huffman_tree_root.is_leaf():
        encoding_map[huffman_tree_root.data[1]] = "0"
    else:
        populate_encoding_map(huffman_tree_root, "", encoding_map)
    return encoding_map


def encode_msg(msg):
    root = get_huffman_tree(msg)
    encoding_map = get_encoding_map(root)
    encoded_list = []
    for ch in msg:
        encoded_list.append(encoding_map[ch])
    return "".join(encoded_list), root


def decode_msg(msg, root):
    if root.is_leaf():
        return root.data[1]
    decoded_list = []
    node = root
    for ch in msg:
        if ch == "0":
            node = node.left
        else:
            node = node.right
        if node.is_leaf():
            decoded_list.append(node.data[1])
            node = root
    return "".join(decoded_list)


def main():
    msg = "aasaafs"
    msg_ascii = bin(int.from_bytes(msg.encode(), "big"))
    print(f"Original msg = ({len(msg)}){msg} = ({len(msg)*8}){msg_ascii}")
    encoded_msg, huffman_root = encode_msg(msg)
    print(f"Encoded msg = ({len(encoded_msg)}){encoded_msg}")
    data_savings = (len(msg) * 8 - len(encoded_msg)) / (len(msg) * 8)
    print(
        f"Data savings = ({len(msg)*8}-{len(encoded_msg)})/{len(msg)*8} = {data_savings*100}%"
    )
    decoded_msg = decode_msg(encoded_msg, huffman_root)
    print("Decoded msg = " + decoded_msg)
    assert decoded_msg == msg


main()
