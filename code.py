import psutil
import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
import os
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

LOG_FILE = "PROJECTS/windows-disk-kullanimi-script/disk_usage_log.json"

def save_to_json(disk_data):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            data = json.load(file)
    else:
        data = {}
    
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data[timestamp] = disk_data

    with open(LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Disk kullanımı JSON dosyasına kaydedildi!")

def log_disk_usage():
    disk_data = {drive: psutil.disk_usage(drive).percent for drive in drives}
    save_to_json(disk_data)

log_disk_usage()

def check_disk_usage():
    usage_info = "\n".join([f"{drive}: {psutil.disk_usage(drive).percent} %" for drive in drives])
    messagebox.showinfo("Disk kullanımı", usage_info)

root = tk.Tk()
root.title("Disk Kullanımı İzleme")

label = tk.Label(root, text="Disk kullanımını kontrol etmek için butona basın.", padx=20, pady=10)
label.pack()

btn_check = tk.Button(root, text="Kontrol Et", command=check_disk_usage)
btn_check.pack()

root.mainloop

load_dotenv()

# SMTP Ayarları

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

disk_thresholds = {}
notified_disks = set()

print("Disk kullanım eşiği belirleme:")
drives = [disk.device for disk in psutil.disk_partitions()]
usage_data = {drive: [] for drive in drives}
timestamps = []

for drive in drives:
    while True:
        try:
            threshold = int(input(f"{drive} için eşik değerini (%) giriniz: "))
            if 0 <= threshold <=100:
                disk_thresholds[drive] = threshold
                break
            else:
                print("Lütfen 0 ile 100 arasında bir değer girin.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")
print("\nDisk Kullanımı İzleme başladı...")

def update_graph(i):
    global timestamps
    timestamps.append(datetime.now().strftime("%H: %M: %S"))
    for drive in drives:
        usage = psutil.disk_usage(drive).percent
        usage_data[drive].append(usage)
    
    plt.clf()

    for drive in drives:
        plt.plot(timestamps, usage_data[drive], label=f"{drive} Kullanımı (%)")
    
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Zaman")
    plt.ylabel("Kullanım (%)")
    plt.title("Gerçek Zamanlı Disk Kullanımı")
    plt.legend()
    plt.tight_layout()

    fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_graph, interval=5000)

    print("Gerçek Zamanlı grafik başlatıldı...")
    plt.show()

def send_email(disk, usage, threshold):
    subject = f"Dikkat! {disk} Disk Kullanımı % {usage}!"
    body = f"{disk} disk kullanımınız {threshold} % eşik değerini geçti. Mevcut kullanım: {usage}%"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, EMAIL_RECEIVER, msg.as_string())
        print(f"E-posta gönderilemedi: {EMAIL_RECEIVER}")
    
    except Exception as e:
        print(f"E-posta gönderilemedi: {e}")

while True:
    print("\nDisk Kullanımı kontrol ediliyor...")
    for disk, threshold in disk_thresholds.items():
        usage = psutil.disk_usage(disk).percent
        timestamp = datetime.now()

        print(f"{timestamp} - {disk} - Kullanım: {usage} %")

        if usage > threshold and disk not in notified_disks:
            print(f"Uyarı! {disk} diski {threshold} % sınırını aştı! ({usage} %)")
            send_email(disk, usage, threshold)
            notified_disks.add(disk)
    time.sleep(10)
