import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def zoomPlus(image, factor):
    new_height = int(image.shape[0] * factor)
    new_width = int(image.shape[1] * factor)
    imgZoom = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            ori_y = min(ori_y, image.shape[0] - 1)
            ori_x = min(ori_x, image.shape[1] - 1)
            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

# Membaca gambar
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\Ihsan.jpg')

# Zooming gambar
zoomed_image = zoomPlus(image, 2)

# Menampilkan gambar
plt.figure(figsize=(8, 6))
plt.title("Zoomed Image (2x)")
plt.imshow(zoomed_image)
plt.axis('off')
plt.show()
