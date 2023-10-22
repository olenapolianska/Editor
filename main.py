from PyQt5.QtWidgets import *

app = QApplication([ ])
window = QWidget()
folder = QPushButton("Папка")
list = QListWidget()
photo = QLabel("фото")
QPushButton

mainline = QHBoxLayout()
line = QVBoxLayout()
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line2.addLayout(line3)
mainline.addLayout(line)
mainline.addLayout(line2)

line.addWidget(folder)
line.addWidget(list)
line2.addWidget(photo)



window.setLayout(mainline)
window.show()
app.exec()
