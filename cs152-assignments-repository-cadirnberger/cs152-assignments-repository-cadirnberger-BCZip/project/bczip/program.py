from  project.bczip.bczip import BCZip


class main():
    file_path = input("Enter the path to the file to compress: ").strip()
    bczip = BCZip(file_path)
    bczip.compress()
    file_path = input("Enter the path to the file to decompress:").strip()
    bczip = BCZip(file_path)
    bczip.decompress()




if __name__ == '__main__':
    main()