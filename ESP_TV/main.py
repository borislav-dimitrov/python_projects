import sys

from communication import CommunicationManager


def main(args):
    c_mgr = CommunicationManager()
    # for network in c_mgr.available_networks:
    #     print(network.ssid, network.rssi)
    print()
    print(c_mgr.status)

    print(c_mgr.check_connection_status)
    c_mgr.close_connection()
    print(c_mgr.check_connection_status)


if __name__ == '__main__':
    main(sys.argv)
