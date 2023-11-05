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

window.setLayout(mainline)
window.show()
app.exec()
