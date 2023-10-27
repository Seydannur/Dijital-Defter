"""import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QTextEdit

class DigitalNotebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Dijital Defter')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.note_list = QListWidget()
        self.layout.addWidget(self.note_list)

        self.note_text = QTextEdit()
        self.layout.addWidget(self.note_text)

        self.add_button = QPushButton('Not Ekle')
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Notu Sil')
        self.delete_button.clicked.connect(self.delete_note)
        self.layout.addWidget(self.delete_button)

        self.notes = []

    def add_note(self):
        note = self.note_text.toPlainText()
        if note:
            self.notes.append(note)
            self.note_list.addItem(note)
            self.note_text.clear()

    def delete_note(self):
        selected_item = self.note_list.currentItem()
        if selected_item:
            note = selected_item.text()
            self.note_list.takeItem(self.note_list.row(selected_item))
            self.notes.remove(note)

def main():
    app = QApplication(sys.argv)
    window = DigitalNotebook()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
"""
'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit

class DigitalNotebook(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Dijital Defter')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.note_text = QTextEdit()
        self.layout.addWidget(self.note_text)

        self.add_button = QPushButton('Not Ekle')
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        self.notes = []

    def add_note(self):
        note = self.note_text.toPlainText()
        if note:
            self.notes.append(note)
            self.update_notes_text()
            self.note_text.clear()

    def update_notes_text(self):
        notes_text = "\n".join(self.notes)
        self.note_text.setPlainText(notes_text)

def main():
    app = QApplication(sys.argv)
    window = DigitalNotebook()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''
"""import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QPixmap  # QPixmap'ı içe aktarın
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
        self.note_text = QTextEdit()
        self.layout.addWidget(self.note_text)

        self.add_button = QPushButton('Not Ekle')
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        self.notes = []

    def add_note(self):
        note = self.note_text.toPlainText()
        if note:
            self.notes.append(note)
            self.update_notes_text()
            self.note_text.clear()

    def update_notes_text(self):
        notes_text = "\n".join(self.notes)
        self.note_text.setPlainText(notes_text)

def main():
    app = QApplication(sys.argv)
    window = DigitalLibrary()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
"""

'''import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
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
        note_text = QTextEdit()
        self.layout.addWidget(note_text)

    def update_notes_text(self):
        notes_text = "\n".join(self.notes)
        self.note_text.setPlainText(notes_text)

def main():
    app = QApplication(sys.argv)
    window = DigitalLibrary()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
'''
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
