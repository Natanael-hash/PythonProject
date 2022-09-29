from ossaudiodev import SOUND_MIXER_ALTPCM
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title = "Oil change",
        message = "The oil has reached the limit of 10,000 km",
        app_icon = None, 
        timeout = 10
        
        
    )