import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def rotateImageWithPivot(image, degree):
    radian_deg = np.radians(degree)
    cos_deg = np.cos(radian_deg)
    sin_deg = np.sin(radian_deg)

    height, width = image.shape[:2]
    new_height = int(abs(height * cos_deg) + abs(width * sin_deg))
    new_width = int(abs(height * sin_deg) + abs(width * cos_deg))

    # Membuat citra output dengan ukuran baru
    outputImage = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    # Menghitung titik pusat gambar baru
    center_y, center_x = new_height // 2, new_width // 2

    for y in range(height):
        for x in range(width):
            # Menghitung posisi baru dengan memindahkan pusat rotasi
            newX = int(center_x + (x - width // 2) * cos_deg - (y - height // 2) * sin_deg)
            newY = int(center_y + (x - width // 2) * sin_deg + (y - height // 2) * cos_deg)

            # Memastikan koordinat baru berada dalam batas citra
            if 0 <= newX < new_width and 0 <= newY < new_height:
                outputImage[newY, newX] = image[y, x]

    return outputImage

# Ubah dengan jalur gambar Anda
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\Ihsan.jpg')

# Pastikan image tidak kosong
if image is not None and image.size > 0:
    rotated_image = rotateImageWithPivot(image, 45)

    # Menampilkan hasil
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Citra Asli")
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title("Citra Setelah Rotasi")
    plt.imshow(rotated_image)

    plt.show()
else:
    print("Gambar tidak ditemukan atau tidak valid.")
