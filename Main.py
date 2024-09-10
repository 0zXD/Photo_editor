from PIL import Image, ImageEnhance, ImageFilter
import os

# To get the current working directory.
cwd = os.getcwd()
print(f"This is the cwd;- {cwd}")

# To tell it the directory containing the images.
img_dir = os.path.join(cwd, "Images to be processed")
print(f"This is the img_dir;- {img_dir}")
output = os.path.join(img_dir, "Processed")
# The os.path.join is basically used to join two paths together. 

image_files = [b for b in os.listdir(img_dir) if b.endswith((".jpg", ".png", ".jpeg"))]
# What we did here was create a list of all the images in the folder of the respective format. Since we first saved all these photos as b, we'll have to use the same variable so as to add them as the element in the list. os.listdir() is used to show all the elements in the said directory.  


for image in image_files:
    x = os.path.join(img_dir, image)
    with Image.open(x) as img:

        # Convert to grayscale
        grayscale_img = img.convert("L")
        grayscale_img.save(os.path.join(output, f"Processed_{image}"))
        
        # # Apply Gaussian blur
        # blurred_img = grayscale_img.filter(ImageFilter.GaussianBlur(radius=3))
        
        # # Increase sharpen
        # sharpen_img = ImageEnhance.Sharpness(img).enhance(10)
        # sharpen_img.save("sharpened.jpg")
        
        # # Save the processed image
        # grayscale_img.save("wall_processed.jpg")
        
        # # Resize the image to 500x500 pixels
        # resized_img = grayscale_img.resize((500, 500))
        
        # # Save the resized image
        # resized_img.save("wall_resized.jpg")
        
        # Rotate the image 90 degrees clockwise
        # rotated_img = grayscale_img.rotate(90)
        
        # Save the rotated image
        # rotated_img.save("wall_rotated.jpg")


    
