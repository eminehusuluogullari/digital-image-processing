# -- coding: utf-8 --
"""
Görüntü İşleme Ödevi 2 - Temiz Arayüzlü Sürüm
- Kullanıcıdan büyütme/küçültme tercihi alınır
- Döndürme açısı girilir
- Zoom işlemleri ayrı butonlarla yapılır
- Sonuçlar tek tek gösterilir
"""

from tkinter import Tk, Label, Entry, Button, Canvas, filedialog, StringVar, OptionMenu
from PIL import Image, ImageTk
import math

# -------------------- Yardımcı Fonksiyonlar --------------------

def image_to_matrix(image):
    pixels = list(image.getdata())
    width, height = image.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]

def matrix_to_image(matrix):
    height = len(matrix)
    width = len(matrix[0])
    flat_pixels = [pixel for row in matrix for pixel in row]
    image = Image.new("RGB", (width, height))
    image.putdata(flat_pixels)
    return image

def get_pixel(matrix, y, x, c):
    h = len(matrix)
    w = len(matrix[0])
    y = min(max(0, y), h - 1)
    x = min(max(0, x), w - 1)
    return matrix[y][x][c]

def cubic_weight(t):
    t = abs(t)
    if t <= 1:
        return 1 - 2 * t ** 2 + t ** 3
    elif t < 2:
        return 4 - 8 * t + 5 * t ** 2 - t ** 3
    else:
        return 0

# -------------------- Interpolasyonlar --------------------

def resize_nearest(matrix, scale):
    h, w = len(matrix), len(matrix[0])
    new_h, new_w = int(h * scale), int(w * scale)
    return [[matrix[int(i/scale)][int(j/scale)] for j in range(new_w)] for i in range(new_h)]

def resize_bilinear(matrix, scale):
    h, w = len(matrix), len(matrix[0])
    new_h, new_w = int(h * scale), int(w * scale)
    result = []
    for i in range(new_h):
        row = []
        for j in range(new_w):
            x = j / scale
            y = i / scale
            x0, y0 = int(x), int(y)
            x1, y1 = min(x0 + 1, w - 1), min(y0 + 1, h - 1)
            dx, dy = x - x0, y - y0
            pixel = []
            for c in range(3):
                top = (1 - dx) * matrix[y0][x0][c] + dx * matrix[y0][x1][c]
                bottom = (1 - dx) * matrix[y1][x0][c] + dx * matrix[y1][x1][c]
                val = int((1 - dy) * top + dy * bottom)
                pixel.append(val)
            row.append(tuple(pixel))
        result.append(row)
    return result


def resize_bicubic(matrix, scale):
    h, w = len(matrix), len(matrix[0])
    new_h, new_w = int(h * scale), int(w * scale)
    result = []
    for i in range(new_h):
        row = []
        for j in range(new_w):
            x = j / scale
            y = i / scale
            x_int = int(x)
            y_int = int(y)
            pixel = []
            for c in range(3):
                val = 0
                for m in range(-1, 3):
                    for n in range(-1, 3):
                        weight = cubic_weight(m - (y - y_int)) * cubic_weight((x - x_int) - n)
                        val += get_pixel(matrix, y_int + m, x_int + n, c) * weight
                pixel.append(min(max(int(val), 0), 255))
            row.append(tuple(pixel))
        result.append(row)
    return result

# -------------------- Zoom ve Döndürme --------------------
def rotate_image(matrix, angle_deg):
    angle = math.radians(angle_deg)  # Dereceyi radiyana dönüştürme
    cos_t = math.cos(angle)
    sin_t = math.sin(angle)
    h, w = len(matrix), len(matrix[0])
    cx, cy = w // 2, h // 2
    result = [[(255,255,255) for _ in range(w)] for _ in range(h)]  # Boş bir sonuç matrisi
    for i in range(h):
        for j in range(w):
            x = j - cx
            y = i - cy
            nx = int(cos_t * x - sin_t * y + cx)
            ny = int(sin_t * x + cos_t * y + cy)
            if 0 <= ny < h and 0 <= nx < w:
                result[i][j] = matrix[ny][nx]
    return result


def zoom_in(matrix, factor):
    h, w = len(matrix), len(matrix[0])
    crop_h = int(h / factor)
    crop_w = int(w / factor)
    start_y = (h - crop_h) // 2
    start_x = (w - crop_w) // 2

    cropped = []
    for i in range(start_y, start_y + crop_h):
        row = matrix[i][start_x:start_x + crop_w]
        cropped.append(row)

    print(f"Cropped boyutu: {len(cropped)} x {len(cropped[0])}")  # kontrol et
    return resize_bilinear(cropped, factor)


def zoom_out(matrix, factor):
    small = resize_bilinear(matrix, 1 / factor)
    h, w = len(matrix), len(matrix[0])
    sh, sw = len(small), len(small[0])
    result = [[(255,255,255) for _ in range(w)] for _ in range(h)]
    oy, ox = (h - sh)//2, (w - sw)//2
    for i in range(sh):
        for j in range(sw):
            result[oy+i][ox+j] = small[i][j]
    return result

from tkinter import Toplevel
def show_image(matrix, title):
    img = matrix_to_image(matrix)
    print("Görsel boyutu:", img.size)  # Boyutu kontrol et

    top = Toplevel(app)
    top.title(title)

    tkimg = ImageTk.PhotoImage(img)
    top.tkimg = tkimg  # Referansı tut

    canvas = Canvas(top, width=img.width, height=img.height, bg="gray")
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=tkimg)

    top.mainloop()



def apply_resize():
    try:
        scale = float(scale_var.get())
        matrix = image_to_matrix(loaded_image.convert("RGB"))
        interp = interp_var.get()
        if interp == "nearest":
            resized = resize_nearest(matrix, scale)
        elif interp == "bilinear":
            resized = resize_bilinear(matrix, scale)
        elif interp == "bicubic":
            resized = resize_bicubic(matrix, scale)
        else:
            resized = resize_nearest(matrix, scale)
        show_image(resized, f"{scale}x {interp} ile yeniden boyutlandırma")
    except Exception as e:
        print("Hata:", e)

def apply_rotate():
    try:
        angle = float(angle_var.get())
        matrix = image_to_matrix(loaded_image.convert("RGB"))
        rotated = rotate_image(matrix, angle)
        show_image(rotated, f"{angle}° döndürme")
    except:
        print("Geçersiz açı!")

def apply_zoom_in():
    matrix = image_to_matrix(loaded_image.convert("RGB"))
    result = zoom_in(matrix, 2)

    print(f"Zoom sonrası boyut: {len(result)}x{len(result[0])}")  # matrisi gerçekten oluşturmuş mu?

    for row in result[:2]:  # ilk 2 satırı yaz
        print(row[:5])  # ilk 5 piksel

    show_image(result, "Zoom In (2x)")


def apply_zoom_out():
    matrix = image_to_matrix(loaded_image.convert("RGB"))
    result = zoom_out(matrix, 2)  # 2x zoom out
    show_image(result, "Zoom Out (0.5x)")  # Yeni resmi ekranda gösteriyoruz.




def load_image():
    global loaded_image
    path = filedialog.askopenfilename(filetypes=[("Görüntü Dosyaları", ".png;.jpg;.jpeg;.bmp")])
    if path:
        loaded_image = Image.open(path)
        img = loaded_image.resize((250, 250))  # Görseli küçük boyuta getiriyoruz
        tkimg = ImageTk.PhotoImage(img)  # Tkinter için uygun formata çeviriyoruz
        
        image_label.config(image=tkimg)  # Label üzerine görseli ekliyoruz
        image_label.image = tkimg  # Referansı kaydederek görselin kaybolmasını engelliyoruz


# -------------------- Arayüz --------------------


app = Tk()
app.title("Ödev 2 - Görüntü İşleme")

loaded_image = None

Button(app, text="📂 Resim Seç", command=load_image).pack()
image_label = Label(app)
image_label.pack(pady=5)

Label(app, text="📏 Ölçek Faktörü (örn: 2.0 büyütme, 0.5 küçültme):").pack()
scale_var = StringVar(value="2.0")
Entry(app, textvariable=scale_var).pack()

Label(app, text="🎚 Interpolasyon Yöntemi:").pack()
interp_var = StringVar(value="bilinear")
OptionMenu(app, interp_var, "nearest", "bilinear", "bicubic").pack()

Button(app, text="📐 Büyüt/Küçült", command=apply_resize).pack(pady=5)

Label(app, text="↻ Döndürme Açısı (°):").pack()
angle_var = StringVar(value="45")
Entry(app, textvariable=angle_var).pack()

Button(app, text="↻ Döndür", command=apply_rotate).pack(pady=5)

Label(app, text="🔍 Zoom İşlemleri:").pack()
Button(app, text="🔎 Zoom In", command=apply_zoom_in).pack()
Button(app, text="🔍 Zoom Out", command=apply_zoom_out).pack()

app.mainloop()