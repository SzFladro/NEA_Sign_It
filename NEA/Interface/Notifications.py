from PySide6.QtCore import (QObject, QRect, QUrl, Qt, QSize)
from PySide6.QtGui import (QImage, QPixmap)
from PySide6.QtWidgets import (QFrame, QWidget, QHBoxLayout, QVBoxLayout, QSizePolicy, QLabel, QPushButton)
from Custom_Widgets.Theme import (QLabelThemed)

'''
    Notification class which stores a message, priority, type which impacts in which order it is displayed

    Attributes:
        message (str): message content of the notification
        priority (int): priority level of the notification
        type (str): type of notification, e.g., "info" or "warning"
'''
class Notification:
    def __init__(cls, message, priority=0, notification_type="info"):
        cls.message = message
        cls.priority = priority
        cls.type = notification_type

'''
    Handles the creation, management and display of the notification

    Attributes:
        UI: Reference to the Main Window instance in which specific widgets will be accessed to display notifications within them
        _existingNotifications (list): List that keeps track of existing notification frames within UI referencing notification objects
        notification_queue (list): list of notification objects
'''
class NotificationHandler():
    _existingNotifications = []
    notification_queue = []

    #sets the UI instance so that NotificationHandler can access the UI
    @classmethod
    def set_ui(cls, ui_instance):
        cls.UI = ui_instance

    '''
        Creates visual notifications within the UI,
        QFrame ceated as a container for the notification in which the icon and notification message are displayed
        Creates an Acknowledge button which allows this specific notification to be deleted once pressed.

        Parameters:
            notification (Notification object): instance of the Notification class contianing the message, priority and type
    '''
    @classmethod
    def createNotification(cls,notification):
        frame = QFrame(cls.UI.Notifications_Panel)
        frame.setObjectName(u"frame")
        frame.setGeometry(QRect(110, 230, 250, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frame.sizePolicy().hasHeightForWidth())
        frame.setSizePolicy(sizePolicy)
        frame.setMinimumSize(QSize(300, 50))
        frame.setMaximumSize(QSize(350, 50))
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        cls.UI.Notifications_Panel.layout().addWidget(frame)
        horizontalLayout = QHBoxLayout(frame)
        horizontalLayout.setSpacing(14)
        horizontalLayout.setObjectName(u"horizontalLayout")
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        notificationiconpriority = QLabelThemed(frame)
        notificationiconpriority.setObjectName(u"notificationiconpriority")
        if (notification.type=="warning"):
            notificationiconpriority.setPixmap(QPixmap(u":/icons/png2svg/warning-icon.svg"))
        else:
            notificationiconpriority.setPixmap(QPixmap(u":/icons/png2svg/info-icon.svg"))

        horizontalLayout.addWidget(notificationiconpriority)

        notification_label = QLabel(frame)
        notification_label.setObjectName(u"notification_label")
        notification_label.setWordWrap(True)
        notification_label.setText(notification.message)
        horizontalLayout.addWidget(notification_label)

        AcknowledgeNotificationbutton = QPushButton(frame)
        AcknowledgeNotificationbutton.setObjectName(u"AcknowledgeNotificationbutton")
        sizePolicy.setHeightForWidth(AcknowledgeNotificationbutton.sizePolicy().hasHeightForWidth())
        AcknowledgeNotificationbutton.setSizePolicy(sizePolicy)
        AcknowledgeNotificationbutton.setText("Acknowledge")
        AcknowledgeNotificationbutton.clicked.connect(lambda: cls.Delete_Notification(notification))

        horizontalLayout.addWidget(AcknowledgeNotificationbutton)
        cls._existingNotifications.append(frame)

    # Clears existing notifications and creates new ones for notification objects within notification queue
    @classmethod
    def NotiCreator(cls):
        cls.clear_notifications()
        for notification in cls.notification_queue:
            cls.createNotification(notification)

    '''
        Adds a notification to the queue which is then sorted based on the notifications:
            Priority,
            Type
        Then updates the UI based on order of notifications
    '''
    @classmethod
    def Queue_Notification(cls, notification):
        cls.notification_queue.append(notification)
        cls.notification_queue.sort(key=lambda n: (n.priority, n.type))
        cls.NotiCreator()

    #Deletes a specific notification from the queue and then from the UI.
    @classmethod
    def Delete_Notification(cls,notification):
        cls.notification_queue.remove(notification)
        cls.NotiCreator()

    #Recursive method of removing Notification objects from the Queue
    @classmethod
    def Dequeue_All_Notification(cls):
        if cls.notification_queue:
            cls.notification_queue.pop(0)
            cls.Dequeue_All_Notification()
        else:
            cls.NotiCreator()

    #Method to make every notification frame invisible and proceed to delete them when the thread has finished executing
    @classmethod
    def clear_notifications(cls):
        for frame in cls._existingNotifications:
                frame.setParent(None)
                frame.deleteLater()
        cls._existingNotifications =[]

    # Starts the creation and display of a notification
    @classmethod
    def trigger_notification(cls, message, priority, type):
        notification = Notification(message, priority, type)
        cls.Queue_Notification(notification)