from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume_interface = cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(volume):
    volume_interface.SetMasterVolumeLevelScalar(volume, None)

def quit_volume():
    pass
# Example usage: Set volume to 50% (0.5)

if __name__ == '__main__':
    set_volume(0.5)
