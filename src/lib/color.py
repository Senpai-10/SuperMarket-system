class color:
       def __init__(self):
           self.reset = "\33[0m"

       def bold(self, msg): return "\33[1m" + msg + self.reset
       def italic(self, msg): return "\33[3m" + msg + self.reset
       def url(self, msg): return "\33[4m" + msg + self.reset
       def blink(self, msg): return "\33[5m" + msg + self.reset
       def blink2(self, msg): return "\33[6m" + msg + self.reset
       def selected(self, msg): return "\33[7m" + msg + self.reset
       def white(self, msg): return "\33[97m" + msg + self.reset
       def black(self, msg): return "\33[30m" + msg + self.reset
    
       def darkRed(self, msg): return "\33[31m" + msg + self.reset
       def darkGreen(self, msg): return "\33[32m" + msg + self.reset
       def darkYellow(self, msg): return "\33[33m" + msg + self.reset
       def darkBlue(self, msg): return "\33[34m" + msg + self.reset
       def darkViolet(self, msg): return "\33[35m" + msg + self.reset
       def darkBeige(self, msg): return "\33[36m" + msg + self.reset
       def darkWhite(self, msg): return "\33[37m" + msg + self.reset
    
       def lightGrey(self, msg): return "\33[90m" + msg + self.reset
       def lightRed(self, msg): return "\33[91m" + msg + self.reset
       def lightGreen(self, msg): return "\33[92m" + msg + self.reset
       def lightYellow(self, msg): return "\33[93m" + msg + self.reset
       def lightBlue(self, msg): return "\33[94m" + msg + self.reset
       def lightViolet(self, msg): return "\33[95m" + msg + self.reset
       def lightBeige(self, msg): return "\33[96m" + msg + self.reset
    
       def bgBlack(self, msg): return "\33[40m" + msg + self.reset
       def bgRed(self, msg): return "\33[41m" + msg + self.reset
       def bgGreen(self, msg): return "\33[42m" + msg + self.reset
       def bgYellow(self, msg): return "\33[43m" + msg + self.reset
       def bgBlue(self, msg): return "\33[44m" + msg + self.reset
       def bgViolet(self, msg): return "\33[45m" + msg + self.reset
       def bgBeige(self, msg): return "\33[46m" + msg + self.reset
       def bgWhite(self, msg): return "\33[47m" + msg + self.reset
    
       def bgLightGrey(self, msg): return "\33[100m" + msg + self.reset
       def bgLightRed(self, msg): return "\33[101m" + msg + self.reset
       def bgLightGreen(self, msg): return "\33[102m" + msg + self.reset
       def bgLightYellow(self, msg): return "\33[103m" + msg + self.reset
       def bgLightBlue(self, msg): return "\33[104m" + msg + self.reset
       def bgLightViolet(self, msg): return "\33[105m" + msg + self.reset
       def bgLightBeige(self, msg): return "\33[106m" + msg + self.reset
       def bgLightWhite(self, msg): return "\33[107m" + msg + self.reset
