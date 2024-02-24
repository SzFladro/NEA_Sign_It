import sys
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
    QVBoxLayout, QWidget)
from PySide6.QtMultimedia import QMediaDevices

#importing UI
from DataBase import config, Account, WordClass
from src.ui_SignItInterface import *
from Interface import CatalogueInterface, Notifications, OverviewInterface, Live

# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings

config_user = config.Config()
Words = WordClass.Word
Words.add_wordfromDB()
CatInterface = CatalogueInterface.InterfaceCatalogue
notificationhandler = Notifications.NotificationHandler
LiveUI = Live.LiveInterface
OverviewUI = OverviewInterface.InterfaceOverview


########################################################################
## MAIN WINDOW CLASS
########################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################

        loadJsonStyle(self, self.ui, jsonFiles = {"json-styles\dashboard_style.json"
        })
        ########################################################################


        QAppSettings.updateAppSettings(self)
        ########################################################################
        self.setWindowTitle("SignIt")
        self.show()
        self.showMaximized() 
        self.ui.MainWidget.setCurrentWidget(self.ui.Translator)
        self.populate_comboboxes()
        self.get_wordsbasedonsearch(None)
        CatInterface.set_ui(self.ui)
        notificationhandler.set_ui(self.ui)
        LiveUI.set_ui(self.ui)

        #event listeners
        self.ui.SettingsButton.clicked.connect(lambda: self.show_settingsMenu())
        self.ui.CatalogueSearchBar.textChanged.connect(self.get_wordsbasedonsearch)
        self.ui.CatalogueCategoryselector.currentIndexChanged.connect(lambda: self.get_wordsbasedonsearch(None))
        self.ui.CameraSettingComboBox.currentIndexChanged.connect(lambda: self.change_camera())
        self.ui.ProfileButton.clicked.connect(lambda: self.show_accountMenu())
        self.ui.CameraRescan.clicked.connect(lambda: self.populate_cameras())
        self.ui.Login_Button.clicked.connect(lambda: self.loguserin())
        self.ui.SignUpbutton.clicked.connect(lambda: self.signupuser())
        self.ui.LogoutButton.clicked.connect(lambda: self.logoutuser())
        self.ui.LiveButton.clicked.connect(lambda: self.gotoWritingLive())
        self.ui.AcknowledgeNotifications.clicked.connect(lambda: notificationhandler.Dequeue_All_Notification())
        self.ui.StartLiveTranslationbutton.clicked.connect(lambda: self.gotoWritingLive())
        self.ui.StartSpellingBeeButton.clicked.connect(lambda: self.gotoSpellingBee())

    def gotoSpellingBee(self):
        Spellingtext = self.ui.SpellingBeeWordEntry.text()
        if Spellingtext and (' ' not in Spellingtext):
            self.ui.SpellingBeenotificationlabel.setText("")
            Live.SpellingBee.initialise_mode(Spellingtext)
            self.ui.MainWidget.setCurrentWidget(self.ui.Live_pg)
        else:
            self.ui.SpellingBeenotificationlabel.setText("Enter a word or one which has no spaces to start")
            

    def gotoWritingLive(self):
        Live.WritingLive.initialise_mode()
        self.ui.MainWidget.setCurrentWidget(self.ui.Live_pg)

    def change_camera(self):
        main_camera = self.ui.CameraSettingComboBox.currentText()
        if main_camera and main_camera != "Select Main Camera":
            config_user.set_main_camera(main_camera)
            notificationhandler.trigger_notification((f"Main Camera set to: {main_camera}"),0,"info")

    def populate_cameras(self):
        self.ui.CameraSettingComboBox.clear()
        self.ui.CameraSettingComboBox.addItem("Select Main Camera")
        available_cameras= QMediaDevices.videoInputs()
        if available_cameras:
            for cameras in available_cameras:
                self.ui.CameraSettingComboBox.addItem(cameras.description())
        else:
            notificationhandler.trigger_notification(("No Camera found"),0,"info")
      
    def populate_comboboxes(self):
        Worditems4combobox = Words.get_categories()
        self.ui.CatalogueCategoryselector.addItems(Worditems4combobox)
        return None

    def get_wordsbasedonsearch(self,searchword):
        search_category = self.ui.CatalogueCategoryselector.currentText()
        if(search_category == "All"):
            results = Words.search(word_name= searchword)
        else:
            results = Words.search(word_name= searchword, category= search_category)
        CatInterface.set_ui(self.ui)
        CatInterface.frame_creator(self,results)

    def show_accountMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Account")
        user_name = config_user.get_username()
        if user_name == None:
            self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)
            self.ui.PassSignupEdit.textChanged.connect(self.update_passwordstrength)
        else:
            self.loginHandler(user_name)

    def show_settingsMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Settings")
        self.ui.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)

    def loginHandler(self,username):
       self.ui.usernameLoggedinlabel.setText(username)
       self.ui.OptionsWidget.setCurrentWidget(self.ui.LoggedInPage)
        
    def loguserin(self):
        username = self.ui.UsernameLoginEdit.text()
        if username:
            password = self.ui.PassLoginEdit.text()
            msg = Account.Login(username,password)
            if msg:
                notificationhandler.trigger_notification((f"Successfully Logged in as {username}"),0,"info")
                self.loginHandler(username)
            else:
                notificationhandler.trigger_notification("Incorrect Password",0,"info")
        else:
            notificationhandler.trigger_notification(("Enter a Valid Username"),0,"info")

    def logoutuser(self):
        config_user.set_username(None)
        notificationhandler.trigger_notification("Logged User Out",0,"info")
        self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)
    
    def signupuser(self):
        username = self.ui.UsernameSignupEdit.text()
        if username:
            password = self.ui.PassSignupEdit.text()
            confirm_Password = self.ui.ConfirmPassEdit.text()
            if password == confirm_Password:
                if self.ui.Strengthmeter.value()>50:
                    msg = Account.create_User(username,password)
                    if msg:
                        self.ui.OptionsWidget.setCurrentWidget(self.ui.LoggedInPage)
                    else:
                        notificationhandler.trigger_notification("Username is already taken",1,"info")
                else:
                    notificationhandler.trigger_notification("Password isn't Strong enough",0,"info")

            else:
                notificationhandler.trigger_notification("passwords don't match",0,"info")
        else:
            notificationhandler.trigger_notification(("Username can't be blank"),0,"info")

    def update_passwordstrength(self,password):
        score, rating = Account.password_strength(password)
        self.ui.Strengthmeter.setValue(score*25)
        self.ui.Strengthmeter.setFormat(f"Strength: {rating}")

    def closeEvent(self,event):
        OverviewUI.closeEvent(event)
        
     
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())