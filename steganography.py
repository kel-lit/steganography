import sys
import argparse
import binascii



class Steganograph():

	def __init__(self):
		self.joiners = {"SEP": chr(8205), "0": chr(8288), "1": chr(8203)}
		self.inv_joiners = {v: k for k, v in self.joiners.items()}

	def encode(self, message, secret, outfile):

		if len(message) < 2:
			raise Exception("Message is too short")
		
		if len(secret) < 1:
			raise Exception("Please provide a secret")

		binary = ""
		for letter in secret:
			binary += (bin(ord(letter))[2:].zfill(8)) #Remove '0b' from the binary string and forces 8 bits.

		bin_secret = r""
		for bit in binary:
			bin_secret += self.joiners[bit]
		
		encoded_secret = f"{self.joiners['SEP']}{bin_secret}{self.joiners['SEP']}"

		with open(outfile, "w", encoding="utf-8") as f:
			f.write(message[0:-1] + encoded_secret + message[-1:])

	def decode(self, message, infile=False):

		if infile:
			print(f"Reading from file: {message}")
			with open(message, "r", encoding="utf-8") as f:
				message = f.read()

		if self.joiners["SEP"] not in message:
			print("There is no secret in this message.")
			return

		start, end = [i for i, sep in enumerate(message) if sep == self.joiners["SEP"]]
		encoded_secret = message[start+1:end] #+1 removes 'SEP's from output
		binary = ""
		for byte in encoded_secret:
			binary += self.inv_joiners[byte]

		secret = ""
		for i in range(0, len(binary), 8):
			secret += chr(int(binary[i:i+8], 2))

		return secret
	  


def main():

	args = parse_args(sys.argv[1:])
	s = Steganograph()

	if args.encode:
		return s.encode(args.message, args.secret, args.outfile)
	
	elif args.message:
		secret = s.decode(args.message)
		print(f"Secret: {secret}")
		return secret
	
	elif args.infile:
		secret = s.decode(args.infile, infile=True)
		print(f"Secret: {secret}")
		return secret

def parse_args(argv):

	description = """steganography.py is a Python program that conceals a secret message within a 
	plain text message using unicode Zero-Width Joiners."""

	parser = argparse.ArgumentParser(description=description)
	enc_dec = parser.add_mutually_exclusive_group(required=True)
	enc_dec.add_argument("-e", "--encode", action="store_true", help="Encode a secret within a message. Must be used with -s/--secret.")
	enc_dec.add_argument("-d", "--decode", action="store_true", help="Decode a message and return the secret.")

	input_ = parser.add_mutually_exclusive_group(required=True)
	input_.add_argument("-m", "--message", help="The message to encode/decode.")
	input_.add_argument("-i", "--infile", default="in.txt", help="The name of the input file. Default is 'in.txt'.")

	parser.add_argument("-s", "--secret", help="The secret to encode in a message.")
	
	parser.add_argument("-o", "--outfile", default="out.txt", help="The name of the output file. Default is 'out.txt'.")

	args = parser.parse_args(argv)

	if args.encode and not args.secret:
		parser.error("A secret (-s/--secret) is required when using -e/--encode.")
	
	if args.decode and args.secret:
		parser.error("A secret (-s/--secret) is not required when using -d/--decode.")
	
	return args

if __name__ == "__main__":

	main()