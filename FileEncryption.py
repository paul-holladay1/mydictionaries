# 8) FileEncryption.py - Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:
# codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} Using this example, the letter A would be assigned the symbol %, 
# the letter a would be assigned the number 9, the letter B would be assigned the symbol @, and so forth. The program should open this 
# file -  info_security.txt   Download info_security.txt , read its contents, then use the dictionary to write an encrypted version of 
# the file’s contents to a second file (name it 'encrypted.txt'). Each character in the second file should contain the code for the 
# corresponding character in the first file.
def encryption(code):

    infile = open('info_security.txt', 'r')
    infile_read = infile.read()

    file_encryption = open('encrypter.txt', 'w')

    for letter in infile_read:
        if letter in code:
            file_encryption.write(code[letter])
        else:
            file_encryption.write(letter)

    file_encryption.close()


def main():
    code = {'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', 'C' : '^', 'c' : 'i', 'D' : '!', 'd' : 'x', 'E' : '-', 'e' : '*',
            'F' : 'G', 'f' : '5', 'G' : '0', 'g' : '?', 'H' : '~', 'h' : '`', 'I' : 'b', 'i' : 'k', 'J' : '[', 'j' : 'T',
            'K' : '.', 'k' : ':', 'L' : 'q', 'l' : 'w', 'M' : '8', 'm' : '=', 'N' : 'y', 'n' : '}', 'O' : ']', 'o' : 'A',
            'P' : ';', 'p' : '|', 'Q' : '(', 'q' : '"', 'R' : 'J', 'r' : 'E', 'S' : 'u', 's' : '{', 'T' : 'O', 't' : '3',
            'U' : '_', 'u' : 's', 'V' : 'r', 'v' : 'L', 'W' : 't', 'w' : 'p', 'X' : 'a', 'x' : 'v', 'Y' : '1', 'y' : '&',
            'Z' : '>', 'z' : ','}

    encryption(code)
main()


# def encryption(code):

#     infile = open('info_security.txt', 'r')
#     infile_read = infile.read()

#     file_encryption = open('encrypter.txt', 'w')

#     for i in infile_read:
#         if i in code:
#             file_encryption.write(code[i])
#         else:
#             file_encryption.write(i)

#     file_encryption.close()

