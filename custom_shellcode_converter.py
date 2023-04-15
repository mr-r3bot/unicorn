import argparse
import os
import pickle


def convert_shellcode(file_path: str):
    shellcode_bin = open(file_path, "rb").read()
    output = [f"0x{val}"for val in shellcode_bin.hex(",").split(",")]
    # print ("Writing formatted shellcode to formatted_shellcode.txt file")
    print (output)
   

def main():
    parser = argparse.ArgumentParser("Convert custom shellcode to unicorn formatted shellcode")
    parser.add_argument("shellcode", help="path to shellcode file")
    args = parser.parse_args()
    file_path = args.shellcode
    if not os.path.isfile(file_path):
        print ("File not found, check your file path again")
        return

    convert_shellcode(file_path)

if __name__ == "__main__":
    main()