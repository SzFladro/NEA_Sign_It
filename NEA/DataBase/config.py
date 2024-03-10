'''
    Singleton class (only one instance created) for managing configuration settings such as username, main camera index 
    Allows these properties to be accessible/editable throughout the entire program

    Attributes:
        _instance (Config): Singleton instance of the Config class
        username (str): Currently signed in User's Username
        main_camera (int): Index of the selected main camera to be used
    
'''
class Config:
    _instance = None

    # Creates a new instance of the Config class if it doesn't already exist
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.username = None
            cls._instance.main_camera = 0
        return cls._instance

    # Retrieves stored username (str)
    def get_username(self):
        return self.username

    # Sets username to new value
    def set_username(self, new_username):
        self.username = new_username

    # Retrieves the index of the set main_camera 
    def get_main_camera(self):
        return self.main_camera

    # Sets index of the main camera to the one to be used
    def set_main_camera(self, new_camera):
        self.main_camera = new_camera
