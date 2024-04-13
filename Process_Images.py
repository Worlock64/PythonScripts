from PIL import Image
import os

# Function to process image files in a directory
def process_images(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        outfile = os.path.splitext(filename)[0] + ".jpg"
        if os.path.isfile(filepath):
            try:
                # Open the image file
                with Image.open(filepath) as img:
                    # Rotate the image by 90 degrees counter-clockwise
                    img.verify()
                return True
            except(IOError, SyntaxError):
                return False

        with Image.open(filename) as img:
            img = img.rotate(-90, expand=True)
                
            # Resize the image to desired dimensions
            max_size = (128, 128)  # Specify maximum dimensions here
            img.resize(max_size)
                
            # Save the processed image
            img.save(os.path.join(directory, "processed_" + outfile)) 
                    

# Provide the directory containing the icon graphics
directory_path = os.path.join(os.getcwd(), "Images")

process_images(directory_path)
