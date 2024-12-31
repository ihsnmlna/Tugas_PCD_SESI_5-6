import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height / factor)
    new_width = int(width / factor)

    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            # Menghitung koordinat asal
            ori_y = int(y * factor)
            ori_x = int(x * factor)

            # Memastikan koordinat tidak melebihi batas
            ori_y = min(ori_y, height - 1)
            ori_x = min(ori_x, width - 1)

            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

# Ubah dengan jalur gambar Anda
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\UPIN IPIN.jpg')

# Pastikan image tidak kosong
if image is not None and image.size > 0:
    skala = 2  # Faktor zoom
    imgZoomed = zoomMinus(image, skala)

    # Menampilkan hasil
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Citra Asli")
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title("Citra Setelah Zoom Minus")
    plt.imshow(imgZoomed)

    plt.show()
else:
    print("Gambar tidak ditemukan atau tidak valid.")
