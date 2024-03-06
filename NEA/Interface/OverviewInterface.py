from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLayout, QLineEdit, QMainWindow, QProgressBar,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget, QLabel, QPushButton)
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import (QVideoWidget)
import http.client as httplib

from Interface import Notifications, Live
from DataBase import SQLQueries, config

notificationhandler = Notifications.NotificationHandler
config_user = config.Config()
WordSigning = Live.WordLive

class InterfaceOverview:
    UI = None
    wordclass = None
    video_player = None


    @classmethod
    def internet_access(cls) -> bool:
        conn = httplib.HTTPSConnection("1.0.0.2", timeout=5)
        try:
            conn.request("HEAD", "/")
            return True
        except Exception:
            return False
        finally:
            conn.close()

    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance

    @classmethod
    def set_wordinstance(cls, word_instance):
        cls.wordclass = word_instance

    @classmethod
    def get_attempts(cls):
        username = config_user.get_username()
        if username != None:
            attempt_no, attempt_date = SQLQueries.AttemptGetter(username,cls.wordclass.name)
            if attempt_no != 0:
                cls.UI.NoAttemptsOverviewLabel.setText(str(attempt_no))
                cls.UI.LatestDate.setText(attempt_date)
            else:
                cls.UI.NoAttemptsOverviewLabel.setText(str(attempt_no))
                cls.UI.LatestDate.setText("None")
        else:
            cls.UI.NoAttemptsOverviewLabel.setText("Create an account")
            cls.UI.LatestDate.setText("to save progress")
        return None

    @classmethod
    def overviewInterface(cls):
        cls.UI.MainWidget.setCurrentWidget(cls.UI.Overview)
        cls.UI.WordOverviewlabel.setText(f"{cls.wordclass.name}")
        cls.UI.CategoryOverviewLabel.setText(f"{cls.wordclass.category}")
        cls.get_attempts()
        if cls.internet_access():
            downloadlink = cls.wordclass.download_link
            cls.loadvideo(downloadlink)
        else:
            notificationhandler.trigger_notification(("Can't load video, No Internet Connection"),1,"warning")
            cls.UI.ExpandableSideMenu.expandMenu()


    @classmethod
    def GoToWordSign(cls):
        WordSigning.set_word(cls.wordclass)
        cls.UI.MainWidget.setCurrentWidget(cls.UI.Live_pg)
        WordSigning.initialise_mode()

    @classmethod
    def loadvideo(cls, download_link):
        if cls.video_player is not None:
            cls.video_player.stop()
            cls.UI.PlayVideoButton.setText("Play")
        else:
            cls.UI.StartSigningButton.clicked.connect(cls.GoToWordSign)
            cls.video_player = QMediaPlayer(None)
            videoWidget = QVideoWidget()
            cls.video_player.setVideoOutput(videoWidget)
            cls.UI.VideoPlayingWidget.layout().addWidget(videoWidget)
            cls.video_player.durationChanged.connect(cls.set_duration)
            cls.video_player.positionChanged.connect(cls.position_changed)
            cls.UI.PlayVideoButton.clicked.connect(cls.play_pause_video)
            cls.UI.VideoSeekerSlider.sliderMoved.connect(cls.set_position)
            notificationhandler.trigger_notification(("Data Rates may apply\n Proceed with caution"),1,"warning")
            cls.UI.ExpandableSideMenu.expandMenu()
        cls.video_player.setSource(QUrl.fromUserInput(download_link))


    @classmethod
    def play_pause_video(cls):
        if cls.video_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            cls.video_player.pause()
            cls.UI.PlayVideoButton.setText("Play")
           
        else:
            cls.UI.PlayVideoButton.setText("Pause")
            cls.video_player.play()

    @classmethod
    def set_duration(cls, duration):
        cls.UI.VideoSeekerSlider.setRange(0, duration)
        cls.UI.Vidlengthlabel.setText(f"/ {duration / 1000 // 60}:{duration / 1000 % 60:.0f}")

    @classmethod
    def set_position(cls,position):
        cls.video_player.setPosition(position)

    @classmethod
    def position_changed(cls,position):
        cls.UI.VideoSeekerSlider.setValue(position)
        cls.UI.DurationWatchedlabel.setText(f"{position / 1000 // 60}:{position / 1000 % 60:.0f}")

    @classmethod
    def closeEvent(cls,event):
        if cls.video_player is not None:
            cls.video_player.stop()
            cls.UI.VideoPlayingWidget.setParent(None)
            cls.video_player.deleteLater()  
            cls.video_player = None
        event.accept()

