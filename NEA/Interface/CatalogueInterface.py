from PySide6.QtCore import (QCoreApplication, QUrl, Qt)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy)

from Interface import OverviewInterface 

OverviewUI = OverviewInterface.InterfaceOverview

'''
    Handles the creation and management of UI frames for each word instance within the catalogue

    Attributes:
        _existingFrames (list): list storing references to existing frames
        UI (object): reference to main window instance
'''
class InterfaceCatalogue:
    _existingFrames = [] 
    UI=None

    #sets the UI instance for the InterfaceCatalogue class
    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance
        OverviewUI.set_ui(ui_instance)

    '''
        Method that creates and adds frames to the catalogue grid layout within the scrollable area CatalogueWidget,
        first fills row until no frames can fit on the available screen (based on resolution of screen) then goes to next column

        Creates a label for the name of the word_instance, a button which passes the word_instance to overview

        Parameters:
            word_instance (object): properties of the particular word_instance are displayed within the frame
            row_number (int): references the row within the grid layout bound within the screen's resolution
            column_number (int): references the column within the grid layout for the frame to appear
    '''
    @classmethod
    def createWidgets(cls,word_instance, row_number, column_number):
        frame = QFrame(cls.UI.CatalogueWidget)
        frame.setObjectName(u"frame")
        frame.setMinimumSize(100, 100)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        cls.UI.gridLayout.addWidget(frame, row_number, column_number, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

        vertical_layout = QVBoxLayout(frame)

        word_frame = QFrame(frame)
        word_frame.setObjectName(u"WordFrame")
        word_frame.setFrameShape(QFrame.StyledPanel)
        word_frame.setFrameShadow(QFrame.Raised)
        vertical_layout_2 = QVBoxLayout(word_frame)

        word_label = QLabel(word_frame)
        word_label.setObjectName(u"WordLabel")
        word_label.setText(word_instance.name)
        vertical_layout_2.addWidget(word_label)
        vertical_layout.addWidget(word_frame, 0, Qt.AlignTop)

        image_frame = QFrame(frame)
        image_frame.setObjectName(u"ImageFrame")
        size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(image_frame.sizePolicy().hasHeightForWidth())
        image_frame.setSizePolicy(size_policy)
        image_frame.setFrameShape(QFrame.StyledPanel)
        image_frame.setFrameShadow(QFrame.Raised)
        vertical_layout.addWidget(image_frame)

        button_frame = QFrame(frame)
        button_frame.setObjectName(u"ButtonFrame")
        button_frame.setFrameShape(QFrame.StyledPanel)
        button_frame.setFrameShadow(QFrame.Raised)
        vertical_layout_3 = QVBoxLayout(button_frame)

        go_to_button = QPushButton(button_frame)
        go_to_button.setObjectName(u"GoToButton")
        go_to_button.setText("GoToOverview")
        go_to_button.clicked.connect(lambda: cls.goto_overview(word_instance))
        vertical_layout_3.addWidget(go_to_button, 0, Qt.AlignRight)

        vertical_layout.addWidget(button_frame, 0, Qt.AlignBottom)

        cls._existingFrames.append(frame)

    '''
        Creates frames for each word instance within results adding them to the UI,
        Calculating how many frames will fit for a given screen resolution, filling row then column of screen

        Parameters:
            window (object): corresponds to the main window instance where the frames will be displayed
            results (list): List of word instances to be displayed
    '''
    @classmethod
    def frame_creator(cls, window,results):
        window_size = window.size()
        window_width = window_size.width()
        window_height = window_size.height()
        x_max = window_width // 300
        y_max = window_height // 200
        x = 0
        y = 0
        cls.clear_frames()

        for instance in results:
            cls.createWidgets(instance, y, x)
            if x == x_max:
                y += 1
                x = 0
            else:
                x += 1

    '''
        method that clears all existing frames from the UI 
        Removes them from scrollable area (making them invisible) then deletes them
    '''
    @classmethod
    def clear_frames(cls):
        for frame in cls._existingFrames:
            frame.setParent(None)
            frame.deleteLater()
        cls._existingFrames =[]

    '''
        Method that navigates to the overview interface of a specific word

        Parameters:
            word (object): the word instance for which the overview is to be displayed
    '''
    @classmethod
    def goto_overview(cls, word):
        OverviewUI.set_wordinstance(word)
        OverviewUI.overviewInterface()




