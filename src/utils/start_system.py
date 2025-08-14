#!/usr/bin/env python3
"""
Simple startup script for the Real-Time Compliance Monitoring System
Launches the API server and transaction generator
"""

import subprocess
import time
import sys
import os
import signal
import threading
from pathlib import Path

def start_api_server():
    """Start the Flask API server"""
    print("🚀 Starting API Server...")
    
    try:
        print(f"🚀 Starting API server with command: {sys.executable} src/api/simple_api_server.py")
        process = subprocess.Popen(
            [sys.executable, "src/api/simple_api_server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if process started
        if process.poll() is not None:
            print("❌ API server process failed to start")
            stdout, stderr = process.communicate()
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
        
        # Wait for server to start
        print("⏳ Waiting for API server to start...")
        time.sleep(8)
        
        # Check if server started successfully
        max_retries = 5
        for attempt in range(max_retries):
            try:
                import requests
                response = requests.get("http://localhost:5000/api/health", timeout=10)
                if response.status_code == 200:
                    print("✅ API Server started successfully")
                    return process
                else:
                    print(f"⚠️  API Server returned status {response.status_code}, retrying...")
            except Exception as e:
                print(f"⚠️  Attempt {attempt + 1}/{max_retries}: API server not ready yet ({e})")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue
                else:
                    print(f"❌ Failed to start API Server after {max_retries} attempts")
                    return None
            
    except Exception as e:
        print(f"❌ Error starting API Server: {e}")
        return None

def start_transaction_generator():
    """Start the transaction generator"""
    print("📡 Starting Transaction Generator...")
    
    try:
        print(f"🚀 Starting transaction generator with command: {sys.executable} src/utils/simple_ingestion.py")
        process = subprocess.Popen(
            [sys.executable, "src/utils/simple_ingestion.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if process started
        if process.poll() is not None:
            print("❌ Transaction generator process failed to start")
            stdout, stderr = process.communicate()
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
        
        # Wait for generator to start
        time.sleep(2)
        
        if process.poll() is None:
            print("✅ Transaction Generator started successfully")
            return process
        else:
            print("❌ Failed to start Transaction Generator")
            stdout, stderr = process.communicate()
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error starting Transaction Generator: {e}")
        return None

def start_dashboard_server():
    """Start the dashboard server"""
    print("🌐 Starting Dashboard Server...")
    
    try:
        print(f"🚀 Starting dashboard server with command: {sys.executable} src/dashboard/serve_dashboard.py")
        process = subprocess.Popen(
            [sys.executable, "src/dashboard/serve_dashboard.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Check if process started
        if process.poll() is not None:
            print("❌ Dashboard server process failed to start")
            stdout, stderr = process.communicate()
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
        
        # Wait for server to start
        time.sleep(3)
        
        if process.poll() is None:
            print("✅ Dashboard Server started successfully")
            print("🌐 Dashboard available at: http://localhost:8082/real_time_dashboard.html")
            return process
        else:
            print("❌ Failed to start Dashboard Server")
            stdout, stderr = process.communicate()
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error starting Dashboard Server: {e}")
        return None

def cleanup(api_process, generator_process, dashboard_process):
    """Clean up processes on exit"""
    print("\n🛑 Shutting down Real-Time Compliance System...")
    
    if generator_process:
        print("Stopping Transaction Generator...")
        generator_process.terminate()
        try:
            generator_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            generator_process.kill()
    
    if dashboard_process:
        print("Stopping Dashboard Server...")
        dashboard_process.terminate()
        try:
            dashboard_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            dashboard_process.kill()
    
    if api_process:
        print("Stopping API Server...")
        api_process.terminate()
        try:
            api_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            api_process.kill()
    
    print("✅ System shutdown complete")

def main():
    """Main startup function"""
    print("=" * 60)
    print("🚀 REAL-TIME COMPLIANCE MONITORING SYSTEM")
    print("=" * 60)
    
    # Check if required files exist
    required_files = [
        "src/api/simple_api_server.py",
        "src/utils/simple_ingestion.py",
        "src/dashboard/serve_dashboard.py",
        "src/dashboard/real_time_dashboard.html"
    ]
    
    for file_path in required_files:
        if not Path(file_path).exists():
            print(f"❌ Required file not found: {file_path}")
            sys.exit(1)
    
    print("✅ All required files found")
    
    api_process = None
    generator_process = None
    dashboard_process = None
    
    try:
        # Start API server
        api_process = start_api_server()
        if not api_process:
            print("❌ Failed to start API Server. Exiting...")
            sys.exit(1)
        
        # Start transaction generator
        generator_process = start_transaction_generator()
        if not generator_process:
            print("❌ Failed to start Transaction Generator. Exiting...")
            sys.exit(1)
        
        # Start dashboard server
        dashboard_process = start_dashboard_server()
        if not dashboard_process:
            print("❌ Failed to start Dashboard Server. Exiting...")
            sys.exit(1)
        
        print("\n" + "=" * 60)
        print("🎉 REAL-TIME COMPLIANCE MONITORING SYSTEM IS RUNNING!")
        print("=" * 60)
        print("📊 Dashboard: http://localhost:8082/real_time_dashboard.html")
        print("🔌 API Server: http://localhost:5000")
        print("📡 Transaction Generator: Running")
        print("\n💡 Press Ctrl+C to stop the system")
        print("=" * 60)
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Received shutdown signal...")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    finally:
        cleanup(api_process, generator_process, dashboard_process)

if __name__ == "__main__":
    main()
