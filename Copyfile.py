file1 = input("please enter 1.txt for text to be copied from: ")
file2 = input("please enter 2.txt for text to be copied to: ")
with open(file1, 'r') as f1:
    with open(file2, 'w') as f2:
        file1_text = f1.readlines()
        for text in file1_text:
            f2.write(text)
        f1.close()
        f2.close()
print("Done")
