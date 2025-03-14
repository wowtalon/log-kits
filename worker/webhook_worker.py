from worker.base_worker import BaseWorker
import requests

class WebhookWorker(BaseWorker):
    def __init__(self, config):
        super().__init__()
        self.webhook_url = config['target']['url']
        self.key = config['target']['key']

    def process_job(self, data):
        # Implement the logic to process the event and send it to the webhook URL
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.key}
        response = requests.post(self.webhook_url, json=data, headers=headers)
        print(f"Sent webhook request to {self.webhook_url} with data {data}. Response status: {response.status_code}")
        return response.status_code
    