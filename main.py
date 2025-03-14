from lib.syslog import listen_syslog
from lib.webhook import listen_webhook
import threading
import os




if __name__ == "__main__":
    WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT", 8080))
    SYSLOG_PORT = int(os.getenv("SYSLOG_PORT", 5514))
    syslog_thread = threading.Thread(target=listen_syslog, args=(SYSLOG_PORT,))
    webhook_thread = threading.Thread(target=listen_webhook, args=(WEBHOOK_PORT,))

    syslog_thread.start()
    webhook_thread.start()

    syslog_thread.join()
    webhook_thread.join()