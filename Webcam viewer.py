import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class WebcamViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

        # Open the webcam
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 30)  # Update every 30 milliseconds

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.video_label = QLabel()
        layout.addWidget(self.video_label)

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            # Convert the frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to QImage
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            pixmap = QPixmap.fromImage(q_img)

            # Set the QPixmap to the QLabel
            self.video_label.setPixmap(pixmap)
            self.video_label.setAlignment(Qt.AlignCenter)

    def closeEvent(self, event):
        # Release the webcam when closing the application
        self.cap.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    viewer = WebcamViewer()
    viewer.show()
    app.exec()
