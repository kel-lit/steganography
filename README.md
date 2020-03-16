# steganography.py
steganography.py is a Python program that conceals or reveals a secret message within a plain text message encoded using unicode Zero-Width Joiners. 


#### How does it work?
When encoding, it takes a message and a secret. It breaks down the secret text into binary and uses 2 different Zero-Width Joiners ('U+2060' for 0's, and 'U+200B' for 1's) to encode that secret. Then, a third Zero-Width Joiner is used ('U+200D') as a separator, to easily find the encoded secret within the plaintext.
