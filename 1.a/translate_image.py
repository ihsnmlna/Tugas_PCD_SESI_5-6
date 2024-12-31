import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def translateImage(image, tx, ty):
    height, width = image.shape[:2]
    translated_image = np.zeros_like(image)

    for y in range(height):
        for x in range(width):
            new_x = x + tx
            new_y = y + ty
            if 0 <= new_x < width and 0 <= new_y < height:
                translated_image[new_y, new_x] = image[y, x]

    return translated_image

# Membaca gambar
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\Agus Buntung.jpeg')

# Translasi gambar (geser 50 piksel ke kanan dan 30 piksel ke bawah)
tx, ty = 50, 30
translated_image = translateImage(image, tx, ty)

# Menampilkan gambar
plt.figure(figsize=(8, 6))
plt.title("Translated Image (tx=50, ty=30)")
plt.imshow(translated_image)
plt.axis('off')
plt.show()
