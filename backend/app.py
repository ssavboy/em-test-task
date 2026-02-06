from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import sys
from datetime import datetime

UTF8 = 'utf-8'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


class HealthHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/health':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = '{"status": "healthy", "timestamp": "%s"}' % datetime.now().isoformat()
            self.wfile.write(response.encode(UTF8))
            logger.info('Health check OK')
            return
    
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', f'text/plain; charset={UTF8}')
            self.end_headers()
            response = 'Hello from Effective Mobile!'
            self.wfile.write(response.encode(UTF8))
            logger.info('Request to / from %s', self.client_address[0])
            return
        
        self.send_response(404)
        self.send_header('Content-Type', f'text/plain; charset={UTF8}')
        self.end_headers()
        self.wfile.write(b'Not found')
        logger.warning('404 for path %s', self.path)
    
    def log_message(self, format, *args):
        logger.info('%s - %s' % (self.client_address[0], format % args))


def run_server(port=8080, host='0.0.0.0'):
    server_address = (host, port)
    httpd = HTTPServer(server_address, HealthHTTPRequestHandler)
    
    logger.info('='*60)
    logger.info('Starting HTTP server on %s:%d', host, port)
    logger.info('='*60)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info('\nShutting down server...')
        httpd.shutdown()
        sys.exit(0)


if __name__ == '__main__':
    run_server()