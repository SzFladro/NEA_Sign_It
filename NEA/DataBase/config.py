class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.username = None
            cls._instance.main_camera = 0
        return cls._instance

    def get_username(self):
        return self.username

    def set_username(self, new_username):
        self.username = new_username

    def get_main_camera(self):
        return self.main_camera

    def set_main_camera(self, new_camera):
        self.main_camera = new_camera
