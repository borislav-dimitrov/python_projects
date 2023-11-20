class Network:
    def __init__(self, ssid, rssi):
        '''
        Wi-Fi network describing class

        :param ssid: str = Wi-Fi Network Name
        :param rssi: str - Received Signal Strength Indicator
        '''
        self.ssid = ssid
        self.rssi = rssi
