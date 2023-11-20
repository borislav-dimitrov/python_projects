import serial
import time

from .commands import GET_NETWORKS, GET_STATUS
from networking import Network


class CommunicationManager:
    def __init__(self, port='COM4', baud_rate=9600, timeout=.1):
        self.port = serial.Serial(port=port, baudrate=baud_rate, timeout=timeout)
        self.nearby_networks_amt = 0
        self.nearby_networks = []

    @property
    def check_connection_status(self):
        '''Check the serial port status'''
        if self.port.isOpen():
            return True
        return False

    def close_connection(self):
        '''Close the port connection'''
        if self.check_connection_status:
            self.port.close()

    def write(self, content):
        '''
        Write(send) something to the device serial port.

        :param content: str - content to be written/sent
        :return: None
        '''
        self.port.write(bytes(content, 'utf-8'))

    def read(self):
        '''
        Read from the device serial port.
        :return: str
        '''
        return self.port.readline().decode(encoding='utf-8', errors='replace')

    def write_read(self, content):
        '''
        Write(send) something to the device serial port and read the answer.

        :param content: str - content to be written/sent
        :return: str
        '''
        self.write(content)
        time.sleep(0.05)
        return self.read()

    @property
    def available_networks(self, timeout=10):
        '''Get the available networks'''
        self.nearby_networks_amt = 0
        self.nearby_networks = []

        self.write(GET_NETWORKS)
        result = ""

        start = time.time()
        while not result:
            result = self.read()
            now = time.time()
            if now - start > timeout:
                break

        self._process_network_results(result)

        return self.nearby_networks

    @property
    def status(self):
        '''Get the status of the device'''
        return self.write_read(GET_STATUS)

    def _process_network_results(self, results):
        '''Process the received network results'''
        if '|' in results:
            self.nearby_networks_amt = int(results.split('|')[0])
            for network in results.split('|')[1:]:
                if network == '\r\n':
                    continue
                ssid, rssi = network.split(',')
                self.nearby_networks.append(Network(ssid.strip(), rssi.strip()))
