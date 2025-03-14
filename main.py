from lib.syslog import listen_syslog
from lib.webhook import listen_webhook
import threading




if __name__ == "__main__":
    syslog_thread = threading.Thread(target=listen_syslog, args=(5514,))
    webhook_thread = threading.Thread(target=listen_webhook, args=(8080,))

    syslog_thread.start()
    webhook_thread.start()

    syslog_thread.join()
    webhook_thread.join()