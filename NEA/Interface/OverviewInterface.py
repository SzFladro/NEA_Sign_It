from PySide6.QtCore import (Qt, QUrl, QObject)
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import (QVideoWidget)
import http.client as httplib

from Interface import Notifications, Live
from DataBase import SQLQueries, config

notificationhandler = Notifications.NotificationHandler
config_user = config.Config()
WordSigning = Live.WordLive

'''
    Class managng the overview interface handling user interactions and video playback for a specific word
    
    Attributes:
        UI: reference to the Main Window instance
        wordclass: the current word instance being viewed
        video_player: instance of the video_player, used for streaming videos.
'''
class InterfaceOverview:
    UI = None
    wordclass = None
    video_player = None

    '''
        Checks internet access by attempting to connect to a server

        Returns:
            bool: True if internet access is avaialable 
    '''
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

    #Sets up the UI so that attributes of the Main Window can be accessed
    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance

    #sets word instance for the class
    @classmethod
    def set_wordinstance(cls, word_instance):
        cls.wordclass = word_instance

    '''
        Checks if a user is logged in, Retrieves and displays their attempt and the latest attempt date assigned to their account updating UI 
        Otherwise, it notifies the user to create an account to save progress
    '''
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

    '''
        Sets up the overview screen for the corresponding word
        checks wether a user has an internet connection before retrieving the download_link assigned to the word
    '''
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

    #Passes the word instance to Live mode once the Sign It button is pressed
    @classmethod
    def GoToWordSign(cls):
        WordSigning.set_word(cls.wordclass)
        cls.UI.MainWidget.setCurrentWidget(cls.UI.Live_pg)
        WordSigning.initialise_mode()

    '''
        Creates an instance of the videoplayer, assigning event listeners (once) which will control video playback
        It streams the representation of the word from the web and plays it within the UI
    '''
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

    # Plays or pauses the video when the user presses the button
    @classmethod
    def play_pause_video(cls):
        if cls.video_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            cls.video_player.pause()
            cls.UI.PlayVideoButton.setText("Play")
           
        else:
            cls.UI.PlayVideoButton.setText("Pause")
            cls.video_player.play()

    #Sets the range of the seeker to the duration and updates the UI label for the time remaining of video
    @classmethod
    def set_duration(cls, duration):
        cls.UI.VideoSeekerSlider.setRange(0, duration)
        cls.UI.Vidlengthlabel.setText(f"/ {duration / 1000 // 60}:{duration / 1000 % 60:.0f}")

    #Sets the position of the video player in accordance to the seeker
    @classmethod
    def set_position(cls,position):
        cls.video_player.setPosition(position)

    #Updates the UI label based on the changing position of the video
    @classmethod
    def position_changed(cls,position):
        cls.UI.VideoSeekerSlider.setValue(position)
        cls.UI.DurationWatchedlabel.setText(f"{position / 1000 // 60}:{position / 1000 % 60:.0f}")

    #Handles the close event for the class stopping the video player before closing the application
    @classmethod
    def closeEvent(cls,event):
        if cls.video_player is not None:
            cls.video_player.stop()
            cls.UI.VideoPlayingWidget.setParent(None)
            cls.video_player.deleteLater()  
            cls.video_player = None
        event.accept()

