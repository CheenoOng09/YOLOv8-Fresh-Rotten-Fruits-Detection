import os

# Directory containing the annotation files
annotations_dir = r'./object/roboflow/ex_tomato/train/labels/'

# Iterate through each file in the directory
for filename in os.listdir(annotations_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(annotations_dir, filename)
        
        # Read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Replace class ID 0 with class ID 6
        updated_lines = []
        for line in lines:
            parts = line.strip().split()        #return splittly by the space
            if parts[0] == '0':
                parts[0] = '1'
            updated_lines.append(' '.join(parts) + '\n')
        
        # Write the updated lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

print("Class IDs updated successfully.")
