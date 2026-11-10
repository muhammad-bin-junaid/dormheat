#!/usr/bin/env python3
"""HTTP server that serves .html files for extensionless URLs.

Usage: python3 serve.py
Then open http://localhost:8000 in your browser.
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
    
    def do_GET(self):
        url_path = self.path.split('?')[0].rstrip('/')
        rel_path = url_path.lstrip('/')
        
        # Serve static files directly
        ext = os.path.splitext(url_path)[1].lower()
        if ext in ('.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.gif', 
                   '.svg', '.woff', '.woff2', '.ttf', '.eot', '.mp4', 
                   '.json', '.xml', '.txt', '.ico', '.webp') or url_path in ('', '/'):
            return super().do_GET()
        
        # Try adding .html extension
        if os.path.isfile(os.path.join(BASE_DIR, rel_path + '.html')):
            self.path = url_path + '.html'
            return super().do_GET()
        
        # Try directory index
        if os.path.isfile(os.path.join(BASE_DIR, rel_path, 'index.html')):
            self.path = url_path + '/index.html'
            return super().do_GET()
        
        # Fall through to default handler (404)
        return super().do_GET()

if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), Handler)
    httpd.allow_reuse_address = True
    print(f"Serving Dormheat store at http://localhost:{PORT}")
    print(f"Serving from: {BASE_DIR}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        httpd.server_close()