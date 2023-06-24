from PyQt6.QtWidgets import *
import time

time.sleep(2)

app = QApplication([])
label = QLabel('Hello World I am back!')
label.show()
app.exec()
