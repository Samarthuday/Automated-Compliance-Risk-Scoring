#!/usr/bin/env python3
"""
Simple Real-Time Transaction Generator
Generates transactions continuously to demonstrate the system
"""

import requests
import time
import random
import threading
from datetime import datetime

class SimpleTransactionGenerator:
    def __init__(self, api_url="http://localhost:5000"):
        self.api_url = api_url
        self.running = False
        self.transaction_count = 0
        
    def generate_transaction(self):
        """Generate a single transaction"""
        transaction_types = ['transfer', 'payment', 'investment', 'loan', 'refund']
        currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD']
        locations = ['US', 'UK', 'EU', 'JP', 'CA', 'AU', 'SG']
        
        # Generate realistic transaction data
        amount = random.uniform(100, 1000000)
        transaction_type = random.choice(transaction_types)
        
        # Higher amounts for certain types
        if transaction_type == 'investment':
            amount = random.uniform(10000, 1000000)
        elif transaction_type == 'loan':
            amount = random.uniform(50000, 500000)
        
        transaction = {
            'transaction_id': f'live_{int(time.time() * 1000)}',
            'timestamp': datetime.now().isoformat(),
            'amount': round(amount, 2),
            'sender_id': f'user_{random.randint(1000, 9999)}',
            'receiver_id': f'user_{random.randint(1000, 9999)}',
            'transaction_type': transaction_type,
            'payment_currency': random.choice(currencies),
            'received_currency': random.choice(currencies),
            'sender_bank_location': random.choice(locations),
            'receiver_bank_location': random.choice(locations),
            'source': 'simple_ingestion'
        }
        
        return transaction
    
    def send_transaction(self, transaction):
        """Send transaction to API"""
        try:
            response = requests.post(
                f"{self.api_url}/api/process_transaction",
                json=transaction,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                self.transaction_count += 1
                print(f"✅ Transaction {self.transaction_count}: {transaction['transaction_id']} - Risk Score: {result['risk_score']:.3f} - Amount: ${transaction['amount']:,.2f}")
                return True
            else:
                print(f"❌ Transaction failed: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error sending transaction: {e}")
            return False
    
    def start_generation(self):
        """Start generating transactions continuously"""
        print("🚀 Starting Simple Real-Time Transaction Generator...")
        print(f"📡 API URL: {self.api_url}")
        print("⏱️  Generating transactions every 2-5 seconds...")
        print("=" * 60)
        
        self.running = True
        
        while self.running:
            try:
                # Generate and send transaction
                transaction = self.generate_transaction()
                success = self.send_transaction(transaction)
                
                if success:
                    # Random delay between transactions
                    delay = random.uniform(2, 5)
                    time.sleep(delay)
                else:
                    # If failed, wait longer before retry
                    time.sleep(5)
                    
            except KeyboardInterrupt:
                print("\n🛑 Stopping transaction generator...")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                time.sleep(5)
        
        print(f"\n📊 Total transactions generated: {self.transaction_count}")
        print("✅ Transaction generator stopped")
    
    def stop_generation(self):
        """Stop generating transactions"""
        self.running = False

def main():
    """Main function"""
    print("=" * 60)
    print("🚀 SIMPLE REAL-TIME TRANSACTION GENERATOR")
    print("=" * 60)
    
    # Check if API is running
    try:
        response = requests.get("http://localhost:5000/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ API Server is running")
        else:
            print("❌ API Server is not responding properly")
            return
    except Exception as e:
        print(f"❌ Cannot connect to API server: {e}")
        print("Make sure the API server is running on http://localhost:5000")
        return
    
    # Start transaction generator
    generator = SimpleTransactionGenerator()
    
    try:
        generator.start_generation()
    except KeyboardInterrupt:
        print("\n🛑 Received interrupt signal...")
    finally:
        generator.stop_generation()

if __name__ == "__main__":
    main()
