# import cv2

# image=cv2.imread("bubu.jpg")
# cv2.imshow("title",image)
#
# cv2.waitKey(0)

import cv2

# Configurable Parameters
source = "bubu.jpg"
destination = 'newImage.png'
scale_percent = 50

# Read the image
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Check if the image is loaded successfully
if src is None:
    print(f"Error: Unable to load image from {source}")
else:
    # Calculate the new dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    # Resize the image
    output = cv2.resize(src, (new_width, new_height))

    # Save the resized image
    success = cv2.imwrite(destination, output)

    # Check if the image is saved successfully
    if success:
        print(f"Resized image saved to {destination}")
    else:
        print("Error: Unable to save resized image")
