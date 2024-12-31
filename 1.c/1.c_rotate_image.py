import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def rotateImage(image, degree):
    radians = np.deg2rad(degree)
    height, width = image.shape[:2]
    new_width = int(abs(width * np.cos(radians)) + abs(height * np.sin(radians)))
    new_height = int(abs(height * np.cos(radians)) + abs(width * np.sin(radians)))

    outputImage = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
    centerX, centerY = width // 2, height // 2
    new_centerX, new_centerY = new_width // 2, new_height // 2

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int((y - new_centerY) * np.cos(radians) + (x - new_centerX) * np.sin(radians) + centerY)
            ori_x = int(-(y - new_centerY) * np.sin(radians) + (x - new_centerX) * np.cos(radians) + centerX)
            if 0 <= ori_x < width and 0 <= ori_y < height:
                outputImage[y, x] = image[ori_y, ori_x]

    return outputImage

# Membaca gambar
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\Ihsan.jpg')

# Rotasi gambar
rotated_image = rotateImage(image, 45)

# Menampilkan gambar
plt.figure(figsize=(8, 6))
plt.title("Rotated Image (45°)")
plt.imshow(rotated_image)
plt.axis('off')
plt.show()
