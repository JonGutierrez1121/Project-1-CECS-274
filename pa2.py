import numpy as np

def get_information(path):
    with open(path) as file:
        data = np.zeros(5)
        i = 0
        for line in file:
            data[i] = int(line)
            i += 1

        return data
    print('Read Failed')

def put_information(data):
    with open("output.txt", "w") as file:
        i = 4
        while i > -1:
            file.write(str(int(data[i])) + "\n")
            i -= 1
        return
    print("Write Failed")

def main():
    file_path = input()
    read_data = get_information(file_path)
    print(read_data)
    put_information(read_data)

if __name__ =="__main__":
    main()