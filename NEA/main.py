#importing modules and classes
from DataBase import config, Account, WordClass
from src.ui_SignItInterface import *
from Interface import CatalogueInterface, Notifications, OverviewInterface, Live

# importing necessary libraries 
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from PySide6.QtMultimedia import QMediaDevices
import cv2
import sys
import numpy as np
import mediapipe as mp
import tensorflow as tf

# initialising interface objects
config_user = config.Config()
Words = WordClass.Word
Words.add_wordfromDB()
CatInterface = CatalogueInterface.InterfaceCatalogue
notificationhandler = Notifications.NotificationHandler
LiveUI = Live.LiveInterface
OverviewUI = OverviewInterface.InterfaceOverview

'''
    MainWindow class that represents the application's primary UI (Main Window)

    Attributes:
        ui (Ui_MainWindow object): instance of the UI class 
'''
class MainWindow(QMainWindow):

    #Initialises the main window
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # applies a json stylesheet to customises the UI
        loadJsonStyle(self, self.ui, jsonFiles = {"json-styles\dashboard_style.json"
        })
 
        QAppSettings.updateAppSettings(self)

        #setts properties for the main window
        self.setWindowTitle("SignIt")
        self.show()
        self.showMaximized() 
        self.ui.MainWidget.setCurrentWidget(self.ui.Translator)
        self.populate_comboboxes()
        self.get_wordsbasedonsearch(None)
        CatInterface.set_ui(self.ui)
        notificationhandler.set_ui(self.ui)
        LiveUI.set_ui(self.ui)

        #Creates one instance of event listeners for ui interactions
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

        #Overrides echo mode so that password isn't visible when typing (fixes bug)
        self.ui.ConfirmPassEdit.setEchoMode(QLineEdit.Password)
        self.ui.PassSignupEdit.setEchoMode(QLineEdit.Password)
        self.ui.PassLoginEdit.setEchoMode(QLineEdit.Password)

    '''
        Transistions to the spelling bee mode

        Validates input and initialises spelling bee if a criteria is met:
            The inputted text can't be empty,
            It can't contain spaces
    '''
    def gotoSpellingBee(self):
        Spellingtext = self.ui.SpellingBeeWordEntry.text()
        if Spellingtext and (' ' not in Spellingtext):
            self.ui.SpellingBeenotificationlabel.setText("")
            Live.SpellingBee.initialise_mode(Spellingtext)
            self.ui.MainWidget.setCurrentWidget(self.ui.Live_pg)
        else:
            self.ui.SpellingBeenotificationlabel.setText("Enter a word or one which has no spaces to start")
            
    #Transitions and Initialises Writing Live mode
    def gotoWritingLive(self):
        Live.WritingLive.initialise_mode()
        self.ui.MainWidget.setCurrentWidget(self.ui.Live_pg)

    '''
        Handles the change of the main camera within the CameraSettingComboBox

        Updating the main camera setting within config based on user selection
    '''
    def change_camera(self):
        main_camera = self.ui.CameraSettingComboBox.currentText()
        if main_camera and main_camera != "Select Main Camera":
            config_user.set_main_camera(main_camera)
            notificationhandler.trigger_notification((f"Main Camera set to: {main_camera}"),0,"info")

    '''
        Retrieves available cameras connected to device and populates the camera selection combobox in the UI
    '''
    def populate_cameras(self):
        self.ui.CameraSettingComboBox.clear()
        self.ui.CameraSettingComboBox.addItem("Select Main Camera")
        available_cameras= QMediaDevices.videoInputs()
        if available_cameras:
            for cameras in available_cameras:
                self.ui.CameraSettingComboBox.addItem(cameras.description())
        else:
            notificationhandler.trigger_notification(("No Camera found"),0,"info")
      
    '''
        Retrieves word categories and populates the category combobox within the UI
    '''
    def populate_comboboxes(self):
        Worditems4combobox = Words.get_categories()
        self.ui.CatalogueCategoryselector.addItems(Worditems4combobox)
        return None


    '''
        Retrieves and displays words based on input of CatalogueSearchBar, search criteria with each key-stroke

        Parameters:
            searchword (str): the keyword to be searched corresponding to current input of the search bar
    '''
    def get_wordsbasedonsearch(self,searchword):
        search_category = self.ui.CatalogueCategoryselector.currentText()
        if(search_category == "All"):
            results = Words.search(word_name= searchword)
        else:
            results = Words.search(word_name= searchword, category= search_category)
        CatInterface.set_ui(self.ui)
        CatInterface.frame_creator(self,results)

    #Displays the account menu within the UI
    def show_accountMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Account")
        user_name = config_user.get_username()
        if user_name == None:
            self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)
            self.ui.PassSignupEdit.textChanged.connect(self.update_passwordstrength)
        else:
            self.loginHandler(user_name)

    #Displays the settings menu within the UI
    def show_settingsMenu(self):
        self.ui.ExpandableSideMenu.expandMenu()
        self.ui.Sidemenulabel.setText("Settings")
        self.ui.OptionsWidget.setCurrentWidget(self.ui.SettingsPage)

    '''
        Handles user login
            
        Parameters:
            username (str): the username of the logged in user
    '''
    def loginHandler(self,username):
       self.ui.usernameLoggedinlabel.setText(username)
       self.ui.OptionsWidget.setCurrentWidget(self.ui.LoggedInPage)
        
    '''
        Allows the user with the correct entered credentials to login
        Retrieves the username username and password for the UI login fields,
        If a username is provided then Account.Login validates the credentials for the account
        Displaying notifications depending on outcome (Successfully logged in, incorrect password, or no username provided)
    ''' 
    def loguserin(self):
        username = self.ui.UsernameLoginEdit.text()
        password = self.ui.PassLoginEdit.text()
        if username:
            msg = Account.Login(username, password)
            if msg == "Login":
                notificationhandler.trigger_notification((f"Successfully Logged in as {username}"), 0, "info")
                self.loginHandler(username)
            elif msg == "Wrong":
                notificationhandler.trigger_notification("Incorrect Password", 0, "info")
        else:
            notificationhandler.trigger_notification("Enter a username", 0, "info")

    #Allows the username to logout, updating UI on change, resetting username
    def logoutuser(self):
        config_user.set_username(None)
        notificationhandler.trigger_notification("Logged User Out",0,"info")
        self.ui.OptionsWidget.setCurrentWidget(self.ui.Account_pg)
    
    '''
        Signs a user up if a certain criteria is met:
            Username is entered which isn't assigned to created account
            Password matches the one within the confirm password box
            The strenght is above 50% based on further criteria
    '''
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

    #Retrieves the current input within password entry calculating a value for passwordstrength
    def update_passwordstrength(self,password):
        score, rating = Account.password_strength(password)
        self.ui.Strengthmeter.setValue(score*25)
        self.ui.Strengthmeter.setFormat(f"Strength: {rating}")

    #Handles when the main window is closed
    def closeEvent(self,event):
        OverviewUI.closeEvent(event)
        LiveUI.closeEvent(event)
        
#execution of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())