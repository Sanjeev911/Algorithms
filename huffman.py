 # huffman encoding

 #-*-*-*-**-**-**-*-**-**-**-**-*  COMPRESSION *-**-**-**-**-**-**-**-**-**-*
 # step 1: calcualte the frequency of each character from the document
 # step 2: create a heap of the nodes based on the frequency
 # step 3: find the character encoding of each of the characters
 # step 4: replace the characters with the encoded format

 #-*-*-*-**-**-**-*-**-**-**-**-*  DE-COMPRESSION *-**-**-**-**-**-**-**-**-**-*
# step 1: read the bin file byte by bite
# step 2: decode each byte into espective binary notation
# step 3: extract the padding info out of the last bite added , and the remove the padded characters
# step 4: decode the text using reverse_mapping dictionary
# step 5: write the decoded string into "decompressed-"+filename+".txt"



import os
	# helper function to return the frequency(value) of a node 
def node_value(node):
	return node.value

#custom defined priority queue which sorts the elements present in the queue based on their frequency(value)

class priority_queue():
	def __init__(self):
		self.queue = []

	def add(self,node_list):
		for node in node_list:
			self.queue.append(node)
		self.queue.sort(key = node_value)

	def pop(self):
		if len(self.queue)>0:
			a = self.queue[0]
			del self.queue[0]
			return a
		return None



class Node():
	def __init__(self,char,value):
		self.char = char
		self.value = value
		self.right = None
		self.left = None

	def __repr__(self):
		return str(self.value)

	def __lt__(self,operand):
		if operand == None:
			return -1
		if (not isinstance(operand,Node)):
			return -1
		if self.freq<operand.value:
			return True
	def __le__(self,operand):
		if operand == None:
			return -1
		if (not isinstance(operand,Node)):
			return -1
		if self.freq<=operand.value:
			return True
	def __gt__(self,operand):
		if operand == None:
			return -1
		if (not isinstance(operand,Node)):
			return -1
		if self.freq>operand.value:
			return True
	def __ge__(self,operand):
		if operand == None:
			return -1
		if (not isinstance(operand,Node)):
			return -1
		if self.freq>=operand.value:
			return True
	def __eq__(self,operand):
		if operand == None:
			return -1
		if (not isinstance(operand,Node)):
			return -1
		if self.freq==operand.value:
			return True


class huffman_encoding():
	def __init__(self):
		self.path = None
		self.frequency_dict = {}
		self.reverse_mapping = {}
		self.huffman_code = {}
		self.heap = priority_queue()
		self.text = ""
	def read_file(self,path):

		with open (path,'r+') as f:
			text = f.read()
			self.text = text.strip()
		f.close()
		return text


	def write_file(self,path,byte_array):
		filename,extension = os.path.splitext(path)
		output_file = filename+".bin"
		with open(output_file,"wb") as f:
			f.write(bytes(byte_array))
		f.close()

	def create_dictionary(self):
		for character in self.text:
			if character in self.frequency_dict:
				self.frequency_dict[character]+=1
			else:
				self.frequency_dict[character]=1
		return self.frequency_dict

	def create_heap(self):
		for key,value in self.frequency_dict.items():
			node = Node(key,value)
			self.heap.add([node])

	def merging_nodes(self):
		while(len(self.heap.queue)>1):
			node_a = self.heap.pop()
			node_b = self.heap.pop()
			merged_node = Node(None,node_a.value+node_b.value)
			merged_node.left = node_a
			merged_node.right = node_b
			self.heap.add([merged_node])


	def create_character_code(self,node,pattern):
		if (node.char != None):
			self.huffman_code[node.char]=pattern
			self.reverse_mapping[pattern]=node.char
			return

		self.create_character_code(node.right,pattern + "1")

		self.create_character_code(node.left,pattern + "0")

	def encode_document_and_add_padding(self,text_to_encode):
		text = ""
		for character in text_to_encode:
			text+=self.huffman_code[character]
		padding_amount = 8-(len(text)%8)
		text+="".join(["0" for i in range(padding_amount)])
		# ------------------ adding the information about padding ; to be useful for decompression ------------
		text+= "{0:08b}".format(padding_amount)
		self.text = text
		if (len(text)%8) !=0:
			print("Encoding ha not been done properly:PLEASE CHECK THE SOURCE CODE!!!")
			exit(0)
		return text

	def create_byte_array(self):
		byte_array = bytearray()
		for i in range(0,len(self.text),8):
			byte_array.append(int(self.text[i:i+8],2))


		return byte_array

	def compress(self,path):
		self.text = self.read_file(path)
		frequency_dictionary = self.create_dictionary()
		self.create_heap()
		self.merging_nodes()
		root = self.heap.pop()
		pattern = ""
		self.create_character_code(root,pattern)
		self.encode_document_and_add_padding(self.text)
		byte_array = self.create_byte_array()
		self.write_file(path,byte_array)
		#***------------------ Compression done ------------------***#

	def remove_padding(self,bit_string):
#------------ bit_string currently consists of padding info as well as padded text------------  **
#------------ we remove first the padded info from the end and then the padded string------------ **

		padding_amount_info = bit_string[len(bit_string)-8:]
		padding_amount_info_integer = int(padding_amount_info,2)
		text_without_info = bit_string[:len(bit_string)-8]

		text_without_padding = text_without_info[:-padding_amount_info_integer]

		return text_without_padding



	def decode(self,bit_string):
		decoded_string = ""
		substring = ""
		for bit in bit_string:
			substring+=bit
			if substring in self.reverse_mapping:
				decoded_string+=self.reverse_mapping[substring]
				substring=""

		return decoded_string

	def decompress(self,path):
		filename,extension = os.path.splitext(path)
		output_file = filename+"-decompressed.txt"
		with open(path,"rb") as f:
			bit_string = ""
			byte = f.read(1)
			while(byte != b''):	# reached end of the bytes 
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = f.read(1)

		f.close()
		text_without_padding = self.remove_padding(bit_string)
		decoded_string = self.decode(text_without_padding)
		with open(output_file,"w+") as f:
			f.write(decoded_string)
		f.close()



if __name__ == '__main__':
	compressor  =huffman_encoding()
	compressor.compress("sample.txt")
	compressor.decompress("sample.bin")






