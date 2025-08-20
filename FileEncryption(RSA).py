import rsa

def generateKeys(output_path):
    public_key,private_key = rsa.newkeys(1024)
    print("Public & Private Keys Generated")

    namePub = input("Write file name for public key {PEM Extension In Use}: ")
    with open(f"{output_path}/{namePub}.pem",'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))

    namePri = input("Write file name for private key {PEM Extension In Use}: ")
    with open(f"{output_path}/{namePri}.pem",'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))

    print(f"Files Stored in {output_path}")

def encryptFile(output_path,input_file,output_file):

    with open(output_path,'rb') as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open(input_file,'rb') as f:
        fileData = f.read()

    encryptedData = rsa.encrypt(fileData,public_key)
    with open(output_file,'wb') as f:
        f.write(encryptedData)

    print("File Successfully Encrypted.")

def decryptFile(output_path,input_file,output_file):
    with open(output_path,'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    with open(input_file,'rb') as f:
        encryptedData = f.read()

    decryptedData = rsa.decrypt(encryptedData,private_key)
    with open(output_file,'wb') as f:
        f.write(decryptedData)

    print("File Successfully Decrypted.")


while True:
    print("        ===RSA FILE ENCRYPTION===       \n")
    choice = input("Options:\n"
                   "1)Generate Keys\n"
                   "2)File Encryption\n"
                   "3)File Decryption\n"
                   "4)Exit\n"
                   "Pick (1/2/3/4): ")

    if choice == '1':
        output_path = input("Enter a file path to store keys in (Make sure to use '/' for file path): ")

        generateKeys(output_path)

    if choice == '2':
        output_path = input("Enter a file path to public key (Make sure to use '/' for file path): ")
        input_file = input("Enter a file path to the file you want to encrypt (Please append extension with the file & use '/' for file path): ")
        output_file = input("Enter a file path to where you want to store this file (Please append extension with the file & use '/' for file path): ")

        encryptFile(output_path, input_file, output_file)

    if choice == '3':
        output_path = input("Enter a file path to private key (Make sure to use '/' for file path): ")
        input_file = input("Enter a file path to the file you want to decrypt (Please append extension with the file & use '/' for file path): ")
        output_file = input("Enter a file path to where you want to store this file (Please append extension with the file & use '/' for file path): ")

        decryptFile(output_path, input_file, output_file)

    if choice == '4':
        print("Exiting....\n"
              "Thanks For Using Me!")
        break



























