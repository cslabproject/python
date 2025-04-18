class Television:
    '''
    A class representing details for a television.
    '''

    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0
    MAX_CHANNEL:int = 3
    
    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL) -> None:
        '''
        Method to initialize an object and set default values.
        :param status: Television's ON/OFF status as a boolean (T/F).
        :param muted: Television's MUTED/UNMUTED status as a boolean (T/F).
        :param volume: Television's volume as an integer.
        :param channel: Television's channel as an integer.
        '''
        self.__status:bool = status
        self.__muted:bool = muted
        self.__volume:int = volume
        self.__channel:int = channel

    
    def power(self) -> None:
        '''
        Method to change the ON/OFF (T/F) status of Television
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False


    def mute(self) -> None:
        '''
        Method to change the MUTED/UNMUTED (T/F) status of Television if Television status is ON 
        '''
        global unmuted_volume #global variable keeps track of volume before being muted to be able to set it back after unmuting
        
        if self.__status == True:

            if self.__muted == False:
                unmuted_volume = self.__volume
                self.__muted = True
                self.__volume = self.MIN_VOLUME

            elif self.__muted == True:
                self.__muted = False
                self.__volume = unmuted_volume


    def channel_up(self) -> None:
        '''
        Method to increase the channel value of Television if Television status is ON. Will revert to the minimum value if maximum is exceeded
        '''
        if self.__status == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1


    def channel_down(self) -> None:
        '''
        Method to decrease the channel value of Television if Television status is ON. Will revert to the maximum value if minimum is exceeded.
        '''
        if self.__status == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1


    def volume_up(self) -> None:
        '''
        Method to increase the volume value of Television if Television status is ON. Will not increase past maximum value. Will unmute before applying changes.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.mute()             #Unmutes volume and sets it back to what it was before being muted to allow it to be modified.
            
            if self.__volume == self.MAX_VOLUME:
                self.__volume == self.MAX_VOLUME
            else:
                self.__volume += 1


    def volume_down(self) -> None:
        '''
        Method to decrease the volume value of Television if Television status is ON. Will not decrease past minimum value. Will unmute before applying changes.
        '''
        if self.__status == True:
            if self.__muted == True:
                self.mute()            #Unmutes volume and sets it back to what it was before being muted to allow it to be modified.
            
            if self.__volume == self.MIN_VOLUME:
                self.__volume == self.MIN_VOLUME
            else:
                self.__volume -= 1


    def __str__(self) -> str:
        '''
        Method to specify how a Television object is printed.
        :return: A string in the format (values in brackets are variable placeholders): Power = [status], Channel = [channel], Volume = [volume]
        '''
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'