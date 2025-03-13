import numpy as np
from PIL import Image

# Load the image
image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

# 1. Flip the Image (Horizontally and Vertically)
flipped_horizontal = np.fliplr(image_array)
flipped_vertical = np.flipud(image_array)

# 2. Add Random Noise
noise = np.random.randint(-50, 50, image_array.shape, dtype=np.int16)
noisy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)

# 3. Brighten Channels (Increase brightness by 40)
brightened_image_array = np.clip(image_array + 40, 0, 255).astype(np.uint8)

# 4. Apply a Mask (Set a 100x100 region in the center to black)
masked_image_array = image_array.copy()
height, width, _ = masked_image_array.shape
start_x, start_y = width // 2 - 50, height // 2 - 50
masked_image_array[start_y:start_y+100, start_x:start_x+100] = [0, 0, 0]

# Save the modified images
Image.fromarray(flipped_horizontal).save("images/flipped_horizontal.jpg")
Image.fromarray(flipped_vertical).save("images/flipped_vertical.jpg")
Image.fromarray(noisy_image_array).save("images/noisy_image.jpg")
Image.fromarray(brightened_image_array).save("images/brightened_image.jpg")
Image.fromarray(masked_image_array).save("images/masked_image.jpg")

print("Image manipulations completed and saved.")