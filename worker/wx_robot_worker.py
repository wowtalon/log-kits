from worker.base_worker import BaseWorker
import requests

class WxRobotWorker(BaseWorker):
    def __init__(self, config):
        super().__init__()
        self.target = config['target']

    def process_job(self, msg):
        print('Processing job in WxRobotWorker')
        url = self.target
        data = {"msgtype": "text", "text": {"content": msg}}

        response = requests.post(url, json=data)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return msg