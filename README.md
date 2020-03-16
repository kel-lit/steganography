# steganography.py
steganography.py is a Python program that conceals or reveals a secret message within a plain text message encoded using unicode Zero-Width Joiners. 


#### How does it work?
When encoding, it takes a message and a secret. It breaks down the secret text into binary and uses 2 different Zero-Width Joiners ('U+2060' for 0's, and 'U+200B' for 1's) to encode that secret. Then, it adds a third Zero-Width Joiner ('U+200D') to the start and end of the encoded binary, as a separator. This encoded binary is then placed in the middle of the plaintext string and written to a file. This program can also be used to decode encoded messages, either on the command line or by providing an input file.

Try `python steganography.py -d -i in.txt`.

Use `python steganography.py -h` for help.