import socket
import tkinter as tk
import ssl

HOST = '127.0.0.1'
PORT = 12345  


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.check_hostname = False
ssl_context.load_verify_locations(r"keys/server_cert.pem")

ssl_client_socket = ssl_context.wrap_socket(s, server_hostname=None)
ssl_client_socket.connect((HOST, PORT))

def Drop_button_clicked():
   
    SendData = entry.get()
    ssl_client_socket.send(SendData.encode('utf8'))
    print("Drop Button Clicked")


window = tk.Tk()
window.title("Player 1")
window.geometry("220x100")

entry = tk.Entry(window, width=30)
entry.pack(padx=10, pady=10)

#Drop Button
Drop_button = tk.Button(window, text="Drop", command=Drop_button_clicked)
Drop_button.pack(padx=10, pady=10)

window.mainloop()
    
       