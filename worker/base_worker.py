class BaseWorker:
    def __init__(self):
        pass

    def _command(self):
        pass

    def process_job(self, job):
        raise NotImplementedError("Subclasses must implement this method")