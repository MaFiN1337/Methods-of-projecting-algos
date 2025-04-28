from collections import Counter

def get_huffman_dict(input_string):
    class Node:
        def __init__(self, freq, char=None, left=None, right=None):
            self.freq = freq
            self.char = char
            self.left = left
            self.right = right

    def generate_freq_tree(freq_map):
        symbols_freq_list = [Node(freq, char) for char, freq in freq_map.items()]
        symbols_freq_list.sort(key=lambda node: node.freq, reverse=True)
        while len(symbols_freq_list) > 1:
            right_son = symbols_freq_list.pop()
            left_son = symbols_freq_list.pop()
            symbols_freq_list.append(Node(right_son.freq+left_son.freq, right_son.char+left_son.char, left_son, right_son))
            symbols_freq_list.sort(key=lambda node: node.freq, reverse=True)
        return symbols_freq_list[0]

    def generate_codes(node, current_code="", codes=None):
        if codes is None:
            codes = {}

        if node.left is None:
            codes[node.char] = current_code or "0"
            return codes
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
        return codes

    if len(input_string) > 100000 or not input_string:
        print("Something wrong with input")
        return {}
    top_of_encoding_tree = generate_freq_tree(Counter(input_string))
    return generate_codes(top_of_encoding_tree)

def main():
    input_text = input("Введіть рядок: ")
    encoding_dict = get_huffman_dict(input_text)
    for symbol, freq in encoding_dict.items():
        print(f"\"{symbol}\": {freq}")


if __name__ == "__main__":
    main()
