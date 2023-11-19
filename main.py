import os

from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *

app = QApplication([ ])


window = QWidget()
folder = QPushButton("Папка")
list = QListWidget()
photo = QLabel("фото")
left = QPushButton("Вліво")
right = QPushButton("Вправо")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
chb = QPushButton("Ч/Б")

mainline = QHBoxLayout()
line = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
mainline.addLayout(line)
mainline.addLayout(line2)

line.addWidget(folder)
line.addWidget(list)
line2.addWidget(photo)
line2.addLayout(line3)
line3.addWidget(left)
line3.addWidget(right)
line3.addWidget(mirror)
line3.addWidget(sharpness)
line3.addWidget(chb)

app.setStyleSheet("""
        QWidget{
            background:#EAD4FD;
        }
        QPushButton
        {

            background-color:#E7D4FD;
            font-size: 11px;
            color: grey;
            font-family: Courier New;
            border-style: dotted;
            border-width: 1px;
            border-color: black;
            border-radius: 4px;
            

            }
        """)
class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filname = None
    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)

    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)
        photo.setPixmap(pixel)
    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()
    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()
    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.showImage()

    def sharpness(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.showImage()

    def chb (self):
        self.image = self.image.convert("L")
        self.showImage()


work = WorkPhoto()
chb.clicked.connect(work.chb)
sharpness.clicked.connect(work.sharpness)
mirror.clicked.connect(work.mirror)
left.clicked.connect(work.rotate_left)
right.clicked.connect(work.rotate_right)
def open_folder():
    work.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(work.folder)
    list.clear()
    list.addItems(files)
def rotate_left(self):
    self.image = self.image.transpose(Image.ROTATE_90)
    self.showImage()


def showChosenImage():
    work.filename = list.currentItem().text()
    work.load()
    work.showImage()
def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


list.currentRowChanged.connect(showChosenImage)
folder.clicked.connect(open_folder)
window.setLayout(mainline)
window.show()
app.exec()
