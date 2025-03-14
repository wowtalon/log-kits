from worker.base_worker import BaseWorker
import json

class JsonWorker(BaseWorker):

    def __init__(self, config):
        super().__init__()
        self.keys = config['command'].split('.')

    def process_job(self, data):
        try:
            json_data = json.loads(data)
            # Add your processing logic here
            for key in self.keys:
                json_data = json_data[key]
            return json_data
        except json.JSONDecodeError as e:
            self.log_error(f"Failed to decode JSON: {e}")
            return None