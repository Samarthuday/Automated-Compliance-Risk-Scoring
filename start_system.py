#!/usr/bin/env python3
"""
Launcher script for the Real-Time Compliance Monitoring System
This script calls the organized startup script from the utils folder
"""

import sys
import os

# Add src to path so we can import from organized modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the startup script
from utils.start_system import main

if __name__ == "__main__":
    main()
