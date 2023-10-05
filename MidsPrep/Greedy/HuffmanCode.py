class Huffman:
    def __init__(self, char, count):
        self.symbol = char
        self.freq = count
        self.left = None
        self.right = None


def huffman_tree_gen(data):
    count_dict = {}
    for i in list(data):
        count_dict[i] = list(data).count(i)
    print(count_dict)

    node_list = [Huffman(symbol, freq) for symbol, freq in count_dict.items()]
    while len(node_list) > 1:
        # using > 1 because at last iteration we just need one element in the list which will
        # be the root of the tree
        node_list.sort(key=lambda x: x.freq)
        left = node_list.pop(0)  # first pop goes to the left
        right = node_list.pop(0)  # second pop goes to the right
        new_merge = Huffman(char=None, count=left.freq + right.freq)
        new_merge.left, new_merge.right = left, right
        node_list.append(new_merge)

    return node_list[0]  # 0th index contains the root node to the Huffman tree


def huffman_code_gen(start, code, huffman_code):
    if start is None:
        return

    if start.symbol:
        huffman_code[start.symbol] = code

    huffman_code_gen(start.left, code + "0", huffman_code)  # moving left adds "0" to the string representing the code
    huffman_code_gen(start.right, code + "1", huffman_code)  # moving right adds "0" to the string representing the code


def huffman_encoding(data):
    if len(data) is None:
        return None, None

    root = huffman_tree_gen(data)  # nested fn - 1 : builds the Huffman tree and returns the root

    huffman_code = {}
    huffman_code_gen(root, "", huffman_code)

    return huffman_code, root


if __name__ == '__main__':
    # input case from lecture
    data = "bbbbbeeeeeeeeeeccccccccccccaaaaaaaaaaaaaaaadddddddddddddddddffffffffffffffffffffffffff"
    # data = "huffman code"
    encoded, tree = huffman_encoding(data)
    print(encoded)
