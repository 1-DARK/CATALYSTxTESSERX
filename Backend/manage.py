#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# --- Import your Web3 initialization function ---
# Adjust the import path based on where your blockchain_handler.py is relative to manage.py
# Assuming manage.py is in the project root, and blockchain_handler is in api/web3/services/
try:
    # Import the initialization function and the w3 object for status check
    from api.web3.blockchain_handler import initialize_web3, w3
except ImportError:
    print("Error: Could not import initialize_web3 from api.web3.services.blockchain_handler. Check your import path.")
    # Decide what to do if import fails: maybe exit, or just print error and continue without Web3

# --- Your Web3 Initialization Logic Here ---
# This code will run BEFORE Django commands are executed.
# Add checks to ensure it only runs when you want it to (e.g., during runserver)
# Use the same sys.argv check as in the apps.py example

is_running_server = 'runserver' in sys.argv or 'gunicorn' in sys.argv or 'uvicorn' in sys.argv
is_running_qcluster = 'qcluster' in sys.argv # If using Django Q for background tasks

# Check if the initialization function was imported successfully
if 'initialize_web3' in globals(): # Check if the name 'initialize_web3' exists in global scope
    if is_running_server or is_running_qcluster:
         print("[manage.py] Initializing Web3...")
         # Call the initialization function
         if not initialize_web3():
             print("[manage.py] FATAL ERROR: Web3 initialization failed during startup. Blockchain features will be unavailable.")
         else:
             print("[manage.py] Web3 initialization finished successfully.")
    else:
         # For other management commands (like migrate, shell, test), skip initialization
         print("[manage.py] Running management command, skipping Web3 initialization.")
else:
    # Handle the case where the import failed
    print("[manage.py] Web3 initialization skipped because import failed.")


# --- Rest of your manage.py code (remains the same) ---
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicheck.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()