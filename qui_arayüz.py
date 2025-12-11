import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMainWindow,
    QVBoxLayout, QHBoxLayout, QStackedWidget, QListWidget
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dijital Görüntü İşleme GUI")
        self.setGeometry(100, 100, 900, 600)

        # Ana widget ve ana layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Sol Menü (Sidebar)
        self.menu_list = QListWidget()
        self.menu_list.setFixedWidth(200)
        self.menu_list.addItem("🏠 Ana Sayfa")
        self.menu_list.addItem("📷 Ödev 1: Görüntü Yükle")
        self.menu_list.addItem("🎨 Ödev 2: Filtre Uygula")
        self.menu_list.clicked.connect(self.change_page)

        # Sağ İçerik Alanı (Stacked Widget)
        self.stack = QStackedWidget()
        self.page_home = HomePage()
        self.page_odev1 = Odev1Page()
        self.page_odev2 = Odev2Page()
        
        self.stack.addWidget(self.page_home)
        self.stack.addWidget(self.page_odev1)
        self.stack.addWidget(self.page_odev2)

        # Ana layout'a ekle
        main_layout.addWidget(self.menu_list)
        main_layout.addWidget(self.stack)

    def change_page(self):
        index = self.menu_list.currentRow()
        self.stack.setCurrentIndex(index)


class HomePage(QWidget):
    """Ana sayfa bilgilerini içeren sınıf."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel("📚 Dijital Görüntü İşleme Arayüzü\n👤 Emine Hüsülüoğullari - 📌 221229016")
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
        self.setLayout(layout)


class Odev1Page(QWidget):
    """Ödev 1 - Görüntü Yükleme Sayfası"""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("📷 Görüntü Yükleme Sayfası")
        self.label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.label)

        self.image_label = QLabel("Görüntü Seçilmedi")
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        self.btn_yukle = QPushButton("🖼 Görüntü Yükle")
        self.btn_yukle.setStyleSheet("background-color: #FF69B4; color: white; padding: 10px; border-radius: 5px;")
        self.btn_yukle.clicked.connect(self.yukle_goruntu)
        layout.addWidget(self.btn_yukle)

        self.setLayout(layout)

    def yukle_goruntu(self):
        dosya_adi, _ = QFileDialog.getOpenFileName(self, "Görüntü Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg)")
        if dosya_adi:
            self.image_label.setPixmap(QPixmap(dosya_adi).scaled(400, 400, Qt.KeepAspectRatio))


class Odev2Page(QWidget):
    """Ödev 2 - Filtre Uygulama Sayfası"""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("🎨 Filtre Uygulama Sayfası")
        self.label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(self.label)

        self.btn_filt = QPushButton("🖌 Siyah-Beyaz Filtre Uygula")
        self.btn_filt.setStyleSheet("background-color: #800080; color: white; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.btn_filt)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
