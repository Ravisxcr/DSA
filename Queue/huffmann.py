import heapq
import os

class BinaryTreeNode:
    
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    # less than
    def __lt__(self,other) -> bool:
        return self.freq < other.freq
    
    # equal to
    def __eq__(self,other) -> bool:
        return self.freq == other.freq

class HuffmanCoding:

    # initilizer
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}

    # making frequey table
    def __make_freq_dict(self,text) -> dict:

        freq_dict = {}

        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1

        return freq_dict
    
    # build Heap
    def __buidHeap(self,freq_dict) -> None:

        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap,binary_tree_node)

    def __buildTree(self) -> None:

        while(len(self.__heap)>1):
            binary_tree_node_1 = heapq.heappop(self.__heap)
            binary_tree_node_2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node_1.freq + binary_tree_node_2.freq
            newNode = BinaryTreeNode(None,freq_sum)
            newNode.left = binary_tree_node_1
            newNode.right = binary_tree_node_2
            heapq.heappush(self.__heap,newNode)

        return
    
    def __buildCodesHelper(self,root,curr_bits):

        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value] = curr_bits
            self.__reverseCodes[curr_bits] = root.value
            return
        
        self.__buildCodesHelper(root.left,curr_bits+"0")
        self.__buildCodesHelper(root.right,curr_bits+"0")
    
    def __buidCodes(self):

        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")

    def __getEncodedText(self,text):
        encoded_text = ""

        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text
    
    def __paddedEncodedText(self, encoded_text):
        padded_amount = 8 - (len(encoded_text)%8)

        for i in range(padded_amount):
            encoded_text += '0'
        padded_info = "{0:08b}".format(padded_amount)
        return padded_info + encoded_text
    
    def __bytesArray(self, padded_encoded_text):
        arr = []

        for i in range(0,len(padded_encoded_text),8):
            byte = padded_encoded_text[i:i+8]
            arr.append(int(byte,2))

        return arr
    
    def compress(self):

        file_name , file_extension = os.path.splitext(self.path)
        output_path = file_name +'.bin'

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            freq_dict = self.__make_freq_dict(text)
            self.__buidHeap(freq_dict)
            self.__buildTree()
            self.__buidCodes()

            encoded_text = self.__getEncodedText(text)
            padded_encoded_text = self.__paddedEncodedText(encoded_text)
            bytes_array = self.__bytesArray(padded_encoded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)

        print('Compressed')
        return output_path
    
    def __removePadding(self, text):
        padded_info = text[0:8]
        extra_padding = int(padded_info,2)
        text = text[8:]
        text_after_padding_removed = text[:-1*extra_padding]
        return text_after_padding_removed
    
    def __decodeText(self,text):
        decoded_text = ""
        current_bits = ""

        for bit in text:
            current_bits += bit
            if current_bits in self.__reverseCodes:
                character = self.__reverseCodes[current_bits]
                decoded_text += character
                current_bits = ""
        
        return decoded_text
    
    
    def decompress(self, input_path):
        filename , fileextension = os.path.splitext(input_path)
        output_path = filename + '_decompressed' + '.txt'
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ''
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bit_string += bits
                byte = file.read(1)

            actual_text = self.__removePadding(bit_string)
            decompressed_text = self.__decodeText(actual_text)
            output.write(decompressed_text)
        print("Decompressed")


if __name__ == '__main__':

    path = 'new.txt'
    h = HuffmanCoding(path)
    output_path = h.compress()
    h.decompress(output_path)
