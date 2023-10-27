import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image

class DigitalLibrary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Dijital Kütüphane')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Arka plan resmini yükle
        background = QLabel(self)
        pixmap = QPixmap("arkaplan.jpg")
        background.setPixmap(pixmap)
        self.layout.addWidget(background)

        # Not ekleme bölümü
        self.notes = []  # Notları bir liste içinde saklayın

        self.add_button = QPushButton('Not Ekle')
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

    def add_note(self):
        # Her "Not Ekle" düğmesine basıldığında yeni bir not yazma yeri ekleyin
        note_text = QTextEdit(self)
        self.layout.addWidget(note_text)

        # Kaydet butonu
        save_button = QPushButton('Kaydet', self)
        save_button.clicked.connect(lambda: self.save_notes(note_text.toPlainText()))
        self.layout.addWidget(save_button)

    def save_notes(self, note_text):
        if note_text:
            file_dialog = QFileDialog.getSaveFileName(self, 'Notları Kaydet', '', 'Metin Dosyası (*.txt)')
            file_name = file_dialog[0]
            if file_name:
                with open(file_name, 'a') as file:
                    file.write(note_text + '\n')
                QMessageBox.information(self, 'Kaydedildi', 'Notlar başarıyla kaydedildi.')

def main():
    app = QApplication(sys.argv)
    window = DigitalLibrary()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
