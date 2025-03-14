import importlib
from lib.config import config

def proc_msg(msg, type):
    for workflow in config['workflows']:
        if workflow['steps'][0]['worker'] == type and workflow['enabled']:
            for idx,step in enumerate(workflow['steps']):
                if idx == 0:
                    continue
                worker_name = ''.join([word.capitalize() for word in step['worker'].split('_')]) + 'Worker'
                try:
                    module = importlib.import_module(f'worker.{step["worker"]}_worker')
                    worker = getattr(module, worker_name)(step)
                    msg = worker.process_job(msg)
                except Exception as e:
                    print(f'Error processing {step["worker"]}: {e}')
                    break
            break
