# 11. Read and write into a file

with open("file.txt", "w") as f:
    f.write("Hello, world!\nThis is Python.")

with open("file.txt", "r") as f:
    print(f.read())














# my own
# with open("mm.txt","w+") as f:
#     f.write("Hello Python...")
#     f.seek(0)
#     print(f.read())