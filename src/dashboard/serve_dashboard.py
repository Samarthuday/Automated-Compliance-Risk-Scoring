#!/usr/bin/env python3
"""
Simple HTTP Server to serve the dashboard and avoid CORS issues
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

# Configuration
PORT = 8080
DASHBOARD_FILE = "real_time_dashboard.html"

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to the directory containing the dashboard
    os.chdir(Path(__file__).parent)
    
    # Check if dashboard file exists
    if not os.path.exists(DASHBOARD_FILE):
        print(f"❌ Error: {DASHBOARD_FILE} not found!")
        return
    
    # Create server
    with socketserver.TCPServer(("", PORT), CORSHTTPRequestHandler) as httpd:
        print(f"🚀 Dashboard server started at http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"🌐 Dashboard URL: http://localhost:{PORT}/{DASHBOARD_FILE}")
        print("\n" + "="*50)
        print("🎯 IMPORTANT: Make sure your API server is running on port 5000!")
        print("💡 Run: python src/simple_api_server.py")
        print("="*50 + "\n")
        
        # Open dashboard in browser
        dashboard_url = f"http://localhost:{PORT}/{DASHBOARD_FILE}"
        print(f"🔗 Opening dashboard: {dashboard_url}")
        webbrowser.open(dashboard_url)
        
        try:
            print("🔄 Server running... Press Ctrl+C to stop")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    main()
