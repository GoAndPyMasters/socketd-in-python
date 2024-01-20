from vidstream import *
import tkinter as tk
import socket
import threading
import requests
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        ip_address = socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', bytes(ifname[:15], 'utf-8'))
        )[20:24])
        return ip_address
    except IOError:
        return None

# Example: Get the IP address of the 'eth0' interface
local_ip_address = get_ip_address('wlp4s0')


# local_ip_address = socket.gethostbyname(socket.gethostname())
# public_ip_address = requests.get('https://api.ipify.org').text
# server = StreamingServer(local_ip_address, 9999)
# print(local_ip_address)

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    
    t1.start()
    t2.start()


def start_camera_stream():
    Camera_client =  CameraClient(local_ip_address, 7777)
    t3 = threading.Thread(target=Camera_client.start_stream)
    t3.start()


def start_screen_sharing():
    screen_client =  ScreenShareClient(local_ip_address, 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()
    
def start_screen_sharing():
    screen_client =  ScreenShareClient(local_ip_address, 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_sender():
    audio_sender =  ScreenShareClient(local_ip_address, 6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()
# GUI
window = tk.Tk()
window.title("AIFIST call v0.0.1 Alpha")

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

entry_target_ip = tk.Entry(window)  # Use Entry for user input
entry_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)


btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)


btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)


btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_sender)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()