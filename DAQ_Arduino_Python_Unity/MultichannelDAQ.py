import socket
import numpy as np
import matplotlib.pyplot as plt
import serial, time, threading
import matplotlib.animation as animation
import csv

# 在程序开始时打开文件（追加模式）
csv_file = open("C:/Users/zhipe/Desktop/Data/data_log.csv", "a", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Time", "Channel1", "Channel2"])  # 写表头

host, port = "127.0.0.1", 25001

# SOCK_STREAM means TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)

data_ch1 = []
data_ch2 = []
times = []
sock.connect((host, port))

start_time=time.time()

# 串口读取线程
def read_serial():
    while True:
        line = ser.readline().decode(errors="ignore").strip()
        t=time.time()
        if line:
            # line = line.strip()   # 去掉前后空格、\r、\n
            values = [float(v) for v in line.split(",")]
            times.append(t-start_time)
            data_ch1.append(values[0])   # 只取第一个通道
            data_ch2.append(values[1])
            if len(data_ch1) > 500:     # 限制缓存长度
                    data_ch1.pop(0)
                    data_ch2.pop(0)
                    times.pop(0)
            try:
                # 记录时间戳 + 数据到 CSV
                # timestamp = time.time()
                csv_writer.writerow([times[0], values[0], values[1]])
                csv_file.flush()   # 确保实时写入

                sock.sendall(str(values[0]).encode())
                response = sock.recv(1024).decode("utf-8")
            except Exception as e:
                print("Socket error:", e)
                break            
            

threading.Thread(target=read_serial, daemon=True).start()

# 绘图更新
def update(frame):
    plt.cla()
    plt.plot(times,data_ch1)
    plt.plot(times,data_ch2)
    plt.title("Arduino Real-time Data (Channel 1)")

ani = animation.FuncAnimation(plt.gcf(), update, interval=200)
plt.show()
sock.close()   # 只在退出时关闭
ser.close()
csv_file.close()