# Test commit
file_path = "new_file.txt"
with open(file_path, 'w') as file:
    for i in range(1000):
        file.write("bolbo na \n")
print(f"File '{file_path}' created successfully.")



