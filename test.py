# Test commit
file_path = "new_file.txt"
# with open(file_path, 'w') as file:
#     for i in range(1000):
#         file.write("bolbo na \n")
# print(f"File '{file_path}' created successfully.")

with open(file_path, "r+") as file:
    data = file.read()
    file.seek(0)  # Move the cursor to the beginning of the file
    for i in range(1000):
         file.write("test input\n")
    file.truncate() 



