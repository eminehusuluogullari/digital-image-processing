import cv2
import matplotlib.pyplot as plt
# ! Matplotlib, Python'da grafikler ve görselleştirmeler oluşturmak için kullanılan bir kütüphanedir.

# ! pyplot modülü, basit ve hızlı grafik çizimleri yapmak için kullanılır

# Görüntüyü yükle
image_path = "C:\\Goruntu\\bus.jpg"  # Kendi görüntü dosyanın adını yaz
image = cv2.imread(image_path)

# Görüntünün başarıyla yüklenip yüklenmediğini kontrol et
if image is None:
    print(f"Hata: {image_path} bulunamadı veya açılamadı!")
else:
    # OpenCV varsayılan olarak BGR formatında açar, bunu RGB'ye çevirelim
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Görüntüyü göster
    plt.imshow(image_rgb)
    plt.axis("off")  # Eksenleri kaldır
    plt.title("Matplotlib ile Görüntü Gösterme") # Görüntünün üst kısmına bir başlık ekler.
    plt.show()



##########################################




import cv2  # OpenCV kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar (matris işlemleri için)
import matplotlib.pyplot as plt  # Matplotlib'in pyplot modülünü içe aktar (görselleştirme için)

# Görüntüyü yükle (Dosya yolunu kendi sistemine uygun şekilde ayarla)
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # OpenCV ile görüntüyü oku

# Eğer görüntü yüklenemediyse hata mesajı ver
if image is None:
    print("Görüntü yüklenemedi! Dosya yolunu kontrol edin.")
    exit()  # Programı sonlandır

# OpenCV görüntüyü BGR formatında açar, matplotlib ile doğru görüntülemek için RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kesmek istediğin bölgenin koordinatlarını belirle (yatay ve dikey aralık)
y1, y2 = 50, 200   # Yükseklik (satır) aralığı
x1, x2 = 100, 300  # Genişlik (sütun) aralığı

# ! Seçilen bölgeyi görüntü matrisinden al (kes)
cropped_part = image_rgb[y1:y2, x1:x2]

# Kesilen bölgenin matris temsili ekrana yazdır
print("Seçilen Bölgenin Matris Temsili:")
print(cropped_part)

# Kesilen bölgeyi görselleştir
plt.imshow(cropped_part)  # Kesilen bölgeyi göster
plt.axis("off")  # Eksenleri gizle
plt.title("Seçilen Bölge")  # Başlık ekle
plt.show()  # Görüntüyü ekrana getir




##########################################




# ! bu kod usttkıne oranla daha kucuk bır alanı kırpıyor

import cv2  # OpenCV kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar (matris işlemleri için)
import matplotlib.pyplot as plt  # Matplotlib'in pyplot modülünü içe aktar (görselleştirme için)

# Görüntüyü yükle (Dosya yolunu kendi sistemine uygun şekilde ayarla)
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # OpenCV ile görüntüyü oku

# Eğer görüntü yüklenemediyse hata mesajı ver
if image is None:
    print("Görüntü yüklenemedi! Dosya yolunu kontrol edin.")
    exit()  # Programı sonlandır

# OpenCV görüntüyü BGR formatında açar, matplotlib ile doğru görüntülemek için RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Kesmek istediğin bölgenin koordinatlarını belirle (yatay ve dikey aralık)
y1, y2 = 50, 60   # Yükseklik (satır) aralığı (küçük bir alan seçildi)
x1, x2 = 100, 110 # Genişlik (sütun) aralığı (küçük bir alan seçildi)

# Seçilen bölgeyi görüntü matrisinden al (kes)
cropped_part = image_rgb[y1:y2, x1:x2]

# Kesilen bölgenin matris temsili ekrana yazdır
print("Seçilen Bölgenin Piksel Matris Temsili:")
print(cropped_part)

# Kesilen bölgeyi görselleştirme (isteğe bağlı olarak ekleyebilirsin)
plt.imshow(cropped_part)  # Kesilen bölgeyi göster
plt.axis("off")  # Eksenleri gizle
plt.title("Seçilen Küçük Bölge")  # Başlık ekle
plt.show()  # Görüntüyü ekrana getir




####################################



# ! RGB: Renkleri kırmızı, yeşil ve mavi kanallarla ifade eder. Ekranlarda yaygın olarak kullanılır.

# ! Grayscale: Renkli görüntüyü siyah-beyaz tonlarına dönüştürür. Sadece parlaklık bilgisi içerir.

# ! HSV: Renkleri üç bileşende tanımlar: renk tonu (Hue), doygunluk (Saturation) ve parlaklık (Value). Renk analizi için idealdir.

# ! LAB: İnsan gözünün renk algısına göre renkleri aydınlık (L), kırmızı-yeşil (a) ve mavi-sarı (b) olarak ayırır. Profesyonel renk düzeltme için kullanılır.

# ! YCrCb: Parlaklık (Y) ve renk bilgisi (Cr, Cb) olarak ayrılır. Video ve görüntü sıkıştırmasında yaygındır. 



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



#############################################



import cv2  # OpenCV kütüphanesini içe aktar (görüntü işleme için)
import numpy as np  # NumPy kütüphanesini içe aktar (matris işlemleri için)

# Görüntüyü yükle (Dosya yolunu kendi sistemine uygun şekilde ayarla)
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # OpenCV ile görüntüyü oku

# Görüntüyü RGB formatına çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Grayscale dönüşüm
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # HSV dönüşüm
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)  # LAB dönüşüm
image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)  # YCrCb dönüşüm

# Seçmek istediğin bölgenin koordinatları
y1, y2 = 50, 60   # Yükseklik aralığı (küçük bir alan seç)
x1, x2 = 100, 110 # Genişlik aralığı

# Her renk uzayında seçili bölgeyi al
cropped_rgb = image_rgb[y1:y2, x1:x2]
cropped_gray = image_gray[y1:y2, x1:x2]
cropped_hsv = image_hsv[y1:y2, x1:x2]
cropped_lab = image_lab[y1:y2, x1:x2]
cropped_ycrcb = image_ycrcb[y1:y2, x1:x2]

# Matrisleri ekrana yazdır
print("🔹 RGB Matris:")
print(cropped_rgb)

print("\n🔹 Grayscale Matris:")
print(cropped_gray)

print("\n🔹 HSV Matris:")
print(cropped_hsv)

print("\n🔹 LAB Matris:")
print(cropped_lab)

print("\n🔹 YCrCb Matris:")
print(cropped_ycrcb)

#########################################



# ! Histogram, bir görüntüdeki piksellerin yoğunluk dağılımını gösteren bir grafiktir. X-ekseni piksel değerlerini (0-255), Y-ekseni ise her piksel değerinin frekansını (kaç kez tekrarlandığını) gösterir. Görüntünün parlaklık ve kontrast durumu hakkında bilgi verir.



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle ve RGB'den Grayscale (gri tonlama) formatına çevir
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # Görüntüyü oku
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çevir

# Histogram hesapla
# cv2.calcHist() fonksiyonu, belirli bir kanalın (bu durumda gri tonlama) histogramını hesaplar.
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])  # Gri tonlama kanalının histogramını hesapla

# Histogramı çiz
plt.figure(figsize=(10,5))  # Grafik boyutunu belirle
plt.plot(hist, color='black')  # Histogramı siyah renk ile çiz
plt.title("Grayscale Histogram")  # Başlık
plt.xlabel("Piksel Değeri (0-255)")  # X ekseninin etiketi
plt.ylabel("Frekans")  # Y ekseninin etiketi
plt.xlim([0, 256])  # X eksenini 0 ile 255 arasında sınırla
plt.grid()  # Izgara çizgilerini ekle
plt.show()  # Histogramı ekranda göster




################################



# Renk kanalları için histogram hesapla
colors = ('b', 'g', 'r')  # OpenCV'de BGR sıralaması var
channel_labels = ['Mavi', 'Yeşil', 'Kırmızı']

# Grafik boyutunu ayarla
# ! figure ; Yeni bir grafik alanı (figure) oluşturur. Bu, grafiklerin yerleştirileceği boş bir alan sağlar.
plt.figure(figsize=(10,5))

# Her bir renk kanalı için histogram hesapla ve çiz
# ! enumerate ; Python'da bir fonksiyondur ve bir iterable (örneğin, liste, demet) üzerinde döngü oluştururken her elemanın yanı sıra o elemanın sırasını (indeksini) da elde etmenizi sağlar.
for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])  # Histogram hesaplama
    plt.plot(hist, color=color, label=channel_labels[i])  # Histogram çizme

    # ! calchist fonksıyonu zole bır ofnksıyonudur ustune gelıp tıklayınca bu kod gelıryo
    """(function) def calcHist(
    images: Sequence,
    channels: Sequence[int],
    mask: Any | None,
    histSize: Sequence[int],
    ranges: Sequence[float],
    hist: Any | None = ...,
    accumulate: bool = ...
    ) -> Any"""


# Başlık ve etiketler ekle
plt.title("Renkli Görüntü Histogramı")  # Başlık
plt.xlabel("Piksel Değeri (0-255)")  # X ekseni etiket
plt.ylabel("Frekans")  # Y ekseni etiket
plt.legend()  # Legend (etiketler)
plt.grid()  # Izgara ekle
plt.show()  # Görselleştir



#####################################3



# ! Klasik histogram eşitleme, bir görüntünün kontrastını artırmak için kullanılan bir tekniktir. Görüntüdeki piksel değerlerinin dağılımını daha dengeli hale getirir. Bu işlem, görüntüdeki parlaklık ve koyuluk farklarını daha belirginleştirerek, daha net ve anlaşılır bir görüntü elde edilmesini sağlar. Genellikle düşük kontrastlı görüntülerde uygulanır.
# ! paraklık resım genelı artırılıyor doye yorumladım gorsellerden



import cv2
import numpy as np
import matplotlib.pyplot as plt

# 📌 Görüntüyü yükle ve gri tonlamaya çevir
image = cv2.imread("C:\\Goruntu\\rices.jpg", cv2.IMREAD_GRAYSCALE)

# 1️⃣ *Klasik Histogram Eşitleme* - Görüntüdeki kontrastı iyileştirme işlemi
equalized = cv2.equalizeHist(image)

# 2️⃣ *CLAHE (Contrast Limited Adaptive Histogram Equalization)* - Görüntüdeki kontrastı yerel olarak iyileştirme işlemi
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  # CLAHE'nin parametreleri belirleniyor
clahe_equalized = clahe.apply(image)  # CLAHE uygulaması

# 3️⃣ *Histogramları Hesapla* - Orijinal ve işlenmiş görüntülerin histogramlarını hesapla
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])  # Orijinal görüntünün histogramı
hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])  # Eşitlenmiş histogram
hist_clahe = cv2.calcHist([clahe_equalized], [0], None, [256], [0, 256])  # CLAHE histogramı

# 🔹 *Sonuçları Görselleştirme* - Görüntüler ve histogramları karşılaştırmak için alt grafikler oluşturuluyor
fig, axes = plt.subplots(3, 2, figsize=(15, 10))  # 3 satır, 2 sütunlu grafik düzeni



# ! axes, Matplotlib'de bir grafik veya görselleştirme düzeni oluşturduğunda kullanılan bir terimdir. Özellikle plt.subplots() fonksiyonuyla birlikte kullanılır. Bu fonksiyon, birden fazla alt grafik (subplot) oluşturmaya yarar ve her bir alt grafik için bir referans olan axes nesnesini döndürür.

"""Örneğin:

fig, axes = plt.subplots(3, 2, figsize=(15, 10))

Bu satır, 3 satır ve 2 sütundan oluşan bir düzen oluşturur. axes ise her bir alt grafik için bir referans sağlar. Burada axes bir 2D dizidir (3x2), her bir alt grafiği (axes[i, j]) düzenin uygun yerine yerleştirmenizi sağlar.

Özetle, axes alt grafiklere erişim sağlamak için kullanılan bir değişkendir."""


# ! cmap ; renk haritasını (color map) belirtmek için kullanılır
# ! cmap: imshow() fonksiyonu ile görüntülerin renk haritasını belirler. Genellikle 2D matris (görüntü) için kullanılır. Örneğin, cmap="gray" gri tonlama için.

# ! color: plot() fonksiyonu ile çizgi grafikleri veya histogramlar gibi tek boyutlu verilerin rengini belirler. color='black' gibi.

# Orijinal Görüntü
axes[0, 0].imshow(image, cmap="gray")  # Orijinal gri tonlama görüntüsü
axes[0, 0].set_title("Orijinal Görüntü")  # Başlık
axes[0, 0].axis("off")  # Eksenleri gizle

# Orijinal Histogram
axes[0, 1].plot(hist_original, color='black')  # Orijinal histogram
axes[0, 1].set_title("Orijinal Histogram")  # Başlık

# Klasik Histogram Eşitleme Sonucu
axes[1, 0].imshow(equalized, cmap="gray")  # Klasik histogram eşitleme sonucu
axes[1, 0].set_title("Klasik Histogram Eşitleme")  # Başlık
axes[1, 0].axis("off")  # Eksenleri gizle

# Klasik Histogram Eşitleme Histogramı
axes[1, 1].plot(hist_equalized, color='black')  # Klasik histogram eşitleme histogramı
axes[1, 1].set_title("Klasik Histogram Eşitleme Histogramı")  # Başlık

# CLAHE Histogram Eşitleme Sonucu
axes[2, 0].imshow(clahe_equalized, cmap="gray")  # CLAHE uygulaması sonucu
axes[2, 0].set_title("CLAHE Histogram Eşitleme")  # Başlık
axes[2, 0].axis("off")  # Eksenleri gizle

# CLAHE Histogramı
axes[2, 1].plot(hist_clahe, color='black')  # CLAHE histogramı
axes[2, 1].set_title("CLAHE Histogramı")  # Başlık

plt.show()  # Görselleştirmeyi göster



####################################### ?????????????????



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü yükle ve BGR'den RGB'ye çevir
image = cv2.imread("C:\\Goruntu\\bus.jpg")  # Görüntü yükleniyor
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR'yi RGB'ye çeviriyoruz
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Görüntüyü gri tonlamaya çeviriyoruz

# 1️⃣ *Gaussian Blur (Gauss Bulanıklaştırma)*
image_gaussian = cv2.GaussianBlur(image_rgb, (15, 15), 0)  # Görüntüyü Gaussian bulanıklaştırma ile işliyoruz

# 2️⃣ *Median Blur (Tuz ve Biber Gürültüsüne Karşı)*
image_median = cv2.medianBlur(image_rgb, 5)  # Görüntüyü median bulanıklaştırma ile işliyoruz

# 3️⃣ *Bilateral Filter (Kenarlardan Ödün Vermeden Gürültü Giderme)*
image_bilateral = cv2.bilateralFilter(image_rgb, 9, 75, 75)  # Bilateral filtre ile kenarları koruyarak bulanıklaştırma

# 4️⃣ *Sobel Kenar Algılama (X ve Y Yönlü)*
sobel_x = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=5)  # X yönlü Sobel kenar algılama
sobel_y = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=5)  # Y yönlü Sobel kenar algılama
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)  # X ve Y yönlü kenarları birleştiriyoruz

# 5️⃣ *Laplacian Kenar Algılama (İkinci Derece Türev)*
laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)  # Laplacian kenar algılama (ikinci türev)

# 6️⃣ *Canny Kenar Algılama (En Popüler)*
canny_edges = cv2.Canny(image_gray, 100, 200)  # Canny kenar algılama

# 7️⃣ *Prewitt Kenar Algılama (Sobel Alternatifi)*
prewitt_x = cv2.filter2D(image_gray, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))  # Prewitt X yönü
prewitt_y = cv2.filter2D(image_gray, -1, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]))  # Prewitt Y yönü
prewitt_combined = cv2.bitwise_or(prewitt_x, prewitt_y)  # Prewitt X ve Y yönlerini birleştiriyoruz

# 🔹 *Tüm Filtreleme ve Kenar Algılama Tekniklerini Görselleştirme*
fig, axes = plt.subplots(3, 3, figsize=(20, 15))  # 3x3'lü bir düzen oluşturuyoruz

# Orijinal Görüntü
axes[0, 0].imshow(image_rgb)  # Orijinal RGB görüntüyü gösteriyoruz
axes[0, 0].set_title("Orijinal Görüntü")  # Başlık
axes[0, 0].axis("off")  # Eksenleri gizliyoruz

# Gaussian Blur
axes[0, 1].imshow(image_gaussian)  # Gaussian bulanıklaştırma görüntüsünü gösteriyoruz
axes[0, 1].set_title("Gaussian Blur (Bulanıklaştırma)")  # Başlık
axes[0, 1].axis("off")  # Eksenleri gizliyoruz

# Median Blur
axes[0, 2].imshow(image_median)  # Median bulanıklaştırma görüntüsünü gösteriyoruz
axes[0, 2].set_title("Median Blur (Gürültü Azaltma)")  # Başlık
axes[0, 2].axis("off")  # Eksenleri gizliyoruz

# Bilateral Filter
axes[1, 0].imshow(image_bilateral)  # Bilateral filtre görüntüsünü gösteriyoruz
axes[1, 0].set_title("Bilateral Filter (Kenarları Korumalı Blur)")  # Başlık
axes[1, 0].axis("off")  # Eksenleri gizliyoruz

# Sobel Kenar Algılama
axes[1, 1].imshow(sobel_combined, cmap="gray")  # Sobel kenar algılama sonuçlarını gri tonlama ile gösteriyoruz
axes[1, 1].set_title("Sobel Kenar Algılama")  # Başlık
axes[1, 1].axis("off")  # Eksenleri gizliyoruz

# Laplacian Kenar Algılama
axes[1, 2].imshow(laplacian, cmap="gray")  # Laplacian kenar algılama sonuçlarını gri tonlama ile gösteriyoruz
axes[1, 2].set_title("Laplacian Kenar Algılama")  # Başlık
axes[1, 2].axis("off")  # Eksenleri gizliyoruz

# Canny Kenar Algılama
axes[2, 0].imshow(canny_edges, cmap="gray")  # Canny kenar algılama sonuçlarını gri tonlama ile gösteriyoruz
axes[2, 0].set_title("Canny Kenar Algılama")  # Başlık
axes[2, 0].axis("off")  # Eksenleri gizliyoruz

# Prewitt Kenar Algılama
axes[2, 1].imshow(prewitt_combined, cmap="gray")  # Prewitt kenar algılama sonuçlarını gri tonlama ile gösteriyoruz
axes[2, 1].set_title("Prewitt Kenar Algılama")  # Başlık
axes[2, 1].axis("off")  # Eksenleri gizliyoruz

# Boş kutu (Görsel uyum için)
axes[2, 2].axis("off")  # Bu kutuyu görsel uyum için gizliyoruz

plt.show()  # Tüm görselleştirmeyi ekranda gösteriyoruz



#########################################################


