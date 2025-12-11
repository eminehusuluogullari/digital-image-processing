import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow, QAction, QMenu, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

# Görüntü işleme penceresini tanımlayan sınıf
class ImageProcessingWindow(QMdiSubWindow):
    def __init__(self, image, parent=None):
        super().__init__(parent)

        # Görüntüyü gösterecek QLabel widget'ı
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)  # Resmin ortalanması
        self.image_label.setPixmap(QPixmap.fromImage(image))  # QImage'i QPixmap'e dönüştürüp etikette gösterme

        # Histogram ve kanalların etiketlerini ekleyelim
        self.histogram_label = QLabel("Histogram")  # Histogram etiketi
        self.channels_label = QLabel("Kanallar")  # Kanallar etiketi
        
        # Layout düzeni oluşturma (dikey olarak sıralama)
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)  # Görüntü etiketi
        layout.addWidget(self.histogram_label)  # Histogram etiketi
        layout.addWidget(self.channels_label)  # Kanallar etiketi

        # Layout'u bir widget'a ekleyip, bu widget'ı sub pencereye set ediyoruz
        widget = QWidget()
        widget.setLayout(layout)
        self.setWidget(widget)

# Ana pencere sınıfı
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # MDI (Multiple Document Interface) alanı oluşturuyoruz
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)  # MDI alanını ana pencereye merkezi widget olarak set ediyoruz

        self.create_actions()  # Menülerdeki eylemleri oluşturuyoruz
        self.create_menus()  # Menülerimizi oluşturuyoruz

        self.setWindowTitle("Görüntü İşleme Uygulaması")  # Pencere başlığı
        self.setGeometry(100, 100, 800, 600)  # Pencerenin boyutlarını ve konumunu ayarlıyoruz

    def create_actions(self):
        # "Yeni" seçeneği için bir eylem oluşturuyoruz
        self.new_action = QAction("Yeni", self)
        self.new_action.setShortcut("Ctrl+N")  # Kısayol tuşu
        self.new_action.triggered.connect(self.new_image_processing_window)  # Yeni pencereyi açmak için fonksiyon bağlantısı

        # Diğer eylemleri burada ekleyebilirsiniz... 

    def create_menus(self):
        # Dosya menüsünü oluşturuyoruz
        self.file_menu = self.menuBar().addMenu("Dosya")
        self.file_menu.addAction(self.new_action)  # "Yeni" eylemini Dosya menüsüne ekliyoruz

        # Noktasal İşlemler menüsünü oluşturuyoruz
        self.point_operations_menu = self.menuBar().addMenu("Noktasal İşlemler")
        # Noktasal İşlemler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        # Sayısal İşlemler menüsünü oluşturuyoruz
        self.digital_operations_menu = self.menuBar().addMenu("Sayısal İşlemler")
        # Sayısal İşlemler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        # Filtreler menüsünü oluşturuyoruz
        self.filters_menu = self.menuBar().addMenu("Filtreler")
        # Filtreler menüsü altındaki eylemleri burada ekleyebilirsiniz...

        # Matris İşlemleri menüsünü oluşturuyoruz
        self.matrix_operations_menu = self.menuBar().addMenu("Matris İşlemleri")
        # Matris İşlemleri menüsü altındaki eylemleri burada ekleyebilirsiniz...

    def new_image_processing_window(self):
        # Yeni bir görüntü işleme penceresi açılacak
        image = QImage(640, 480, QImage.Format_RGB32)  # 640x480 boyutlarında bir QImage oluşturuyoruz
        image.fill(Qt.white)  # Görüntüyi beyazla dolduruyoruz (örnek bir başlangıç görüntüsü)
        
        # Görüntü işleme penceresini oluşturuyoruz ve MDI alanına ekliyoruz
        image_processing_window = ImageProcessingWindow(image)
        self.mdi_area.addSubWindow(image_processing_window)  # MDI alanına pencereyi ekliyoruz
        image_processing_window.show()  # Pencereyi gösteriyoruz

# Uygulamayı başlatıyoruz
if __name__ == "__main__":
    app = QApplication(sys.argv)  # PyQt5 uygulamasını başlatıyoruz
    main_window = MainWindow()  # Ana pencereyi oluşturuyoruz
    main_window.show()  # Ana pencereyi gösteriyoruz
    sys.exit(app.exec_())  # Uygulama çalışmaya devam ederken olay döngüsüne giriyoruz
