

import cv2  # OpenCV kütüphanesini içe aktar (görüntü işleme için)
import numpy as np  # NumPy kütüphanesini içe aktar (matris işlemleri için)
import matplotlib.pyplot as plt  # Matplotlib'in pyplot modülünü içe aktar (görselleştirme için)

# Görüntüyü yükle (Dosya yolunu kendi sistemine uygun şekilde ayarla)
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # OpenCV ile görüntüyü oku

# Eğer görüntü yüklenemediyse hata mesajı ver
if image is None:
    print("Görüntü yüklenemedi! Dosya yolunu kontrol edin.")
    exit()  # Programı sonlandır

# Farklı renk uzaylarına dönüştürme işlemleri
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye dönüşüm
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR'den Grayscale (Gri tonlama) dönüşüm
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # BGR'den HSV'ye dönüşüm (Hue, Saturation, Value)
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)  # BGR'den LAB'ye dönüşüm
image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)  # BGR'den YCrCb'ye dönüşüm

# ! Görüntüleri Matplotlib ile birden fazla alt pencerede gösterelim
# ! satır sayısı 2 sutun sayısı 3 olcak 2 x 3 ızgara olustur 
# ! figsize toplam grafık alanın boyuutnu ayarlar (inç) 
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # 2x3'lük bir grid oluştur

# RGB renk uzayı
axes[0, 0].imshow(image_rgb)  # RGB görüntüsünü göster
axes[0, 0].set_title("RGB Renk Uzayı")  # Başlık ekle
axes[0, 0].axis("off")  # Eksenleri gizle

# Grayscale (Gri Tonlama) renk uzayı
axes[0, 1].imshow(image_gray, cmap="gray")  # Grayscale görüntüsünü göster (gray colormap)
axes[0, 1].set_title("Grayscale (Gri Tonlama)")  # Başlık ekle
axes[0, 1].axis("off")  # Eksenleri gizle

# HSV renk uzayı
axes[0, 2].imshow(image_hsv)  # HSV görüntüsünü göster
axes[0, 2].set_title("HSV (Hue, Saturation, Value)")  # Başlık ekle
axes[0, 2].axis("off")  # Eksenleri gizle

# LAB renk uzayı
axes[1, 0].imshow(image_lab)  # LAB görüntüsünü göster
axes[1, 0].set_title("LAB Renk Uzayı")  # Başlık ekle
axes[1, 0].axis("off")  # Eksenleri gizle

# YCrCb renk uzayı
axes[1, 1].imshow(image_ycrcb)  # YCrCb görüntüsünü göster
axes[1, 1].set_title("YCrCb Renk Uzayı")  # Başlık ekle
axes[1, 1].axis("off")  # Eksenleri gizle

# Boş kutu (Görsel uyum sağlamak için son pencerede boş bırakıldı)
axes[1, 2].axis("off")  # Boş kutu

# Grafikleri göster
plt.show()  # Ekranda göster
