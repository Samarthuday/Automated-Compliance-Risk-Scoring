#!/usr/bin/env python3
import requests

def check_status():
    try:
        stats = requests.get('http://localhost:5000/api/monitoring/stats').json()
        print(f"Current Status: {stats['total_transactions']} transactions")
        print(f"Risk Distribution: {stats['risk_distribution']}")
        print(f"Pending Reviews: {stats['pending_reviews']}")
        print(f"Alerts: {stats['alerts_generated']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_status()
