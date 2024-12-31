import numpy as np
import imageio as img
import matplotlib.pyplot as plt

def mirrorImage(image):
    return np.flip(image, axis=1)  # Mirroring horizontal

# Membaca gambar
image = img.imread(r'C:\Users\HP\Documents\Tugas Kampus Unsp\Semester 5\Pengolahan Citra Digital\PCD\PCD SESI 5-6\Gambar\UPIN IPIN.jpg')

# Mirroring gambar
mirrored_image = mirrorImage(image)

# Menampilkan gambar
plt.figure(figsize=(8, 6))
plt.title("Mirrored Image")
plt.imshow(mirrored_image)
plt.axis('off')
plt.show()
