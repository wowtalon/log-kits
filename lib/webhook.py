from http.server import BaseHTTPRequestHandler, HTTPServer
import lib.workflow
import requests
import secrets

class WebhookHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.server_version = "log-kits-webhook"
        auth_header = self.headers.get('Authorization')
        if auth_header is None or not auth_header.startswith('Bearer '):
            self.send_response(401)
            self.end_headers()
            return
        token = auth_header.split(' ')[1]
        # Validate the token here if necessary
        if not self.validate_bearer_token(token):
            self.send_response(401)
            self.end_headers()
            return
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received webhook request: {post_data.decode('utf-8')}")
        lib.workflow.proc_msg(post_data.decode('utf-8'), "webhook")
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "ok"}')

    def generate_bearer_token(self):
        return secrets.token_urlsafe(32)

    def validate_bearer_token(self, token):
        # Implement your token validation logic here
        # For example, check if the token exists in a database or matches a predefined value
        return True


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