from datetime import datetime
class log:
    text=""
    time_formet="[%Y/%m/%d %H:%M:%S]  "
    def __init__(self,time_mode:str = "default") -> None:
        super().__init__()
        self.set_time_mode(time_mode)
        self.text+="⚙️[ Log System ]\n"
    def println(self,content:str="\n"):
        self.text+=datetime.now().strftime(self.time_formet)+" "
        self.text+=content
        self.text+="\n"
    def print(self,content:str="\n"):
        self.text+=datetime.now().strftime(self.time_formet)+" "
        self.text+=content
    def show(self):
        return self.text
    def set_time_mode(self,mode:str):
        if(mode=="off"):
            self.time_formet=""
        elif(mode=="default"):
            self.time_formet="[%Y/%m/%d %H:%M:%S]"
        elif(mode=="time_only"):
            self.time_formet="[%H:%M:%S]"
        elif(mode=="day_only"):
            self.time_formet="[%Y/%m/%d]"