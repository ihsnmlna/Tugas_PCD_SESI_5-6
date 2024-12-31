import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def mirrorBoth(image):
    height, width = image.shape[:2]
    
    # Membuat citra baru dengan ukuran dua kali lipat
    combined = np.zeros((height * 2, width * 2, 3), dtype=image.dtype)

    for y in range(height):
        for x in range(width):
            combined[y, x] = image[y, x]  # Citra asli
            combined[y, width + x] = image[y, width - 1 - x]  # Mirroring Horizontal
            combined[height + y, x] = image[height - 1 - y, x]  # Mirroring Vertikal
            combined[height + y, width + x] = image[height - 1 - y, width - 1 - x]  # Mirroring Horizontal dan Vertikal

    return combined

# Ubah dengan jalur gambar Anda
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\Agus Buntung.jpeg')

# Pastikan image tidak kosong
if image is not None and image.size > 0:
    mirrored_image = mirrorBoth(image)

    # Menampilkan hasil
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Citra Asli")
    plt.imshow(image)

    plt.subplot(1, 2, 2)
    plt.title("Citra Setelah Mirroring")
    plt.imshow(mirrored_image)

    plt.show()
else:
    print("Gambar tidak ditemukan atau tidak valid.")
