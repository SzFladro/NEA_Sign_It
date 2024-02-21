import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
import mediapipe as mp

class FingerTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(33)  # 30 fps

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.video_label)

        self.setWindowTitle("Finger Tracker with Hand Detection")
        self.setGeometry(100, 100, 800, 600)

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)

            # Convert the frame to RGB for mediapipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with mediapipe hands
            results = self.hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw landmarks and lines on the frame
                    self.draw_landmarks(frame, hand_landmarks)

            # Convert the frame to QImage
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # Convert QImage to QPixmap and set it to the label
            pixmap = QPixmap.fromImage(q_img)
            self.video_label.setPixmap(pixmap)

    def draw_landmarks(self, frame, landmarks):
        h, w, c = frame.shape

        # Draw landmarks on the frame
        for landmark in landmarks.landmark:
            x, y = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

        # Draw lines connecting consecutive landmarks
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),
            (0, 5), (5, 6), (6, 7), (7, 8),
            (0, 9), (9, 10), (10, 11), (11, 12),
            (0, 13), (13, 14), (14, 15), (15, 16),
            (0, 17), (17, 18), (18, 19), (19, 20)
        ]

        for connection in connections:
            cv2.line(frame, (int(landmarks.landmark[connection[0]].x * w),
                             int(landmarks.landmark[connection[0]].y * h)),
                     (int(landmarks.landmark[connection[1]].x * w),
                      int(landmarks.landmark[connection[1]].y * h)),
                     (0, 255, 0), 2)

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FingerTrackerApp()
    window.show()
    sys.exit(app.exec_())
