from lib.config import config
# from lib.syslog import send_syslog
# from lib.webhook import send_webhook
import base64
import json
import lib.syslog
import lib.webhook

def proc_msg(msg, type):
    for workflow in config['workflows']:
        if workflow['steps'][0]['type'] == type:
            for idx,step in enumerate(workflow['steps']):
                if idx == 0:
                    continue
                if step['type'] == 'syslog':
                    host, port = step['target'].split(':', 1)
                    lib.syslog.send_syslog(msg, host, int(port))
                elif step['type'] == 'webhook':
                    lib.webhook.send_webhook(step['target'], msg)
                elif step['type'] == 'base64':
                    if step['command'] == 'encode':
                        msg = base64.b64encode(msg.encode('utf-8')).decode('utf-8')
                    elif step['command'] == 'decode':
                        msg = base64.b64decode(msg).decode('utf-8')
                    else:
                        print(f"Unknown base64 action: {step['command']}")
                        break
                elif step['type'] == 'json':
                    keys = step['command'].split('.')
                    try:
                        msg = json.loads(msg)
                        for key in keys:
                            msg = msg[key]
                    except Exception as e:
                        print(f"Error processing JSON: {e}")
                        break
                else:
                    print(f"Unknown step type: {step['type']}")
                    break
            break
