import time
from plyer import notification

def send_notification(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 10
    )

if __name__ == "__main__":
    while True:
        title = "Urgent Notification"
        message = "Drink Water!"

        send_notification(title,message)
        time.sleep(3600)