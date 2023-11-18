class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0

    def __init__(self):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self) :
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    
    def volume_up(self):
        if self.__status and self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status and self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
        
    def __str__(self):
        '''
        :return: status of power, channel, and volume
        if TV is muted, then volume is 0
        '''
        if self.__muted == True:
            return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [0]'
        
        return f'Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}]'
    