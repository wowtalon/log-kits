from http.server import BaseHTTPRequestHandler, HTTPServer
import lib.workflow
import requests

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received webhook request: {post_data.decode('utf-8')}")
        lib.workflow.proc_msg(post_data.decode('utf-8'), "webhook")
        self.send_response(200)
        self.end_headers()


def listen_webhook(port=80):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f"Listening for webhook requests on port {port}...")
    httpd.serve_forever()


def send_webhook(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    print(f"Sent webhook request to {url} with data {data}. Response status: {response.status_code}")
    return response.status_code