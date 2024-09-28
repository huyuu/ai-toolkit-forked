import os

# Directory containing the images
image_directory = '@impressionism'

# Iterate over all files in the directory
for filename in os.listdir(image_directory):
    # Check if the file is an image (you can add more extensions if needed)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Extract the name without the extension
        name_without_extension = os.path.splitext(filename)[0]
        
        # Create the corresponding .txt file
        txt_filename = f"{name_without_extension}.txt"
        txt_filepath = os.path.join(image_directory, txt_filename)
        
        # Write the name to the .txt file
        with open(txt_filepath, 'w') as txt_file:
            txt_file.write(name_without_extension)
