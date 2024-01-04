import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from google.cloud import firestore  # Install using `pip install google-cloud-firestore`
from google.cloud import storage     # Install using `pip install google-cloud-storage`

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.setup_ui()

        # Initialize Firestore
        self.db = firestore.Client()

        # Initialize Storage
        self.storage_client = storage.Client()

    def setup_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.video_id_entry = QLineEdit()
        layout.addWidget(self.video_id_entry)

        play_button = QPushButton("Play Video", self)
        play_button.clicked.connect(self.play_video)
        layout.addWidget(play_button)

        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

    def play_video(self):
        video_id = self.video_id_entry.text()

        if video_id:
            try:
                # Retrieve video metadata from Firestore
                video_ref = self.db.collection('videos').document(video_id)
                video_data = video_ref.get().to_dict()

                if video_data:
                    # Extract download URL from metadata
                    video_blob_name = video_data.get('blob_name')

                    if video_blob_name:
                        # Download video from Firebase Storage
                        bucket = self.storage_client.get_bucket('your-storage-bucket-name')
                        video_blob = bucket.blob(video_blob_name)
                        video_url = video_blob.generate_signed_url(expiration=300, method='GET')

                        # Load the video using the QWebEngineView
                        html_content = f"""
                            <html>
                            <head>
                                <style>
                                    body, html {{ margin: 0; padding: 0; width: 100%; height: 100%; overflow: hidden; }}
                                    video {{ width: 100%; height: 100%; }}
                                </style>
                            </head>
                            <body>
                                <video controls>
                                    <source src="{video_url}" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>
                            </body>
                            </html>
                        """
                        self.webview.setHtml(html_content)
                    else:
                        print("Blob name not found in Firestore.")
                else:
                    print("Video data not found in Firestore.")
            except Exception as e:
                print(f"Error retrieving video from Firestore: {e}")
        else:
            print("Please enter a valid video ID.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
