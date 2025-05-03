# api/apps.py

from django.apps import AppConfig
import os
import sys # Keep sys if you want to use sys.argv checks, though less necessary here

# --- Import your Web3 initialization function ---
# This path is relative to your project root, or absolute within the Python path.
# Based on your structure, `api.web3.blockchain_handler` seems correct.
try:
    # Import the initialization function and the w3 object for status check
    from api.web3.blockchain_handler import initialize_web3, w3
    print("[api.apps.py] Successfully imported Web3 components from api.web3.blockchain_handler.")
    web3_components_imported = True # Flag to indicate successful import
except ImportError as e:
    print(f"[api.apps.py] WARNING: Could not import Web3 components from api.web3.blockchain_handler. Error: {e}")
    print("Please ensure api/web3/blockchain_handler.py exists and contains initialize_web3 and w3.")
    web3_components_imported = False # Flag to indicate import failed
    initialize_web3 = None # Ensure the function name isn't defined if import fails
    w3 = None # Same for the w3 object

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        """
        This method is called when Django starts up and loads all apps.
        It's the correct place for application-specific startup code in production.
        """
        # This check prevents initialization during Django setup itself,
        # ensuring it happens only after apps are fully loaded.
        if os.environ.get('RUN_MAIN', None) != 'true':
             print("[api.apps.py] Running Django setup, skipping Web3 initialization in ready().")
             return

        print("[api.apps.py] AppConfig ready() method called.")

        # Check if the Web3 components were imported successfully
        if not web3_components_imported:
             print("[api.apps.py] Skipping Web3 initialization in ready() due to import failure.")
             return # Exit the ready method if import failed

        # In a production WSGI environment (like Gunicorn), ready() is called once per worker process.
        # We typically want Web3 initialized for each worker.
        # The sys.argv check is less critical here compared to manage.py,
        # as ready() is generally called when the application is actually starting to serve.
        # You can simplify this to just: if initialize_web3: initialize_web3()

        print(f"[api.apps.py] Calling initialize_web3 in ready()...")
        if not initialize_web3():
            print("[api.apps.py] FATAL ERROR: Web3 initialization failed during AppConfig ready(). Blockchain features may be unavailable.")
        else:
            print("[api.apps.py] Web3 initialization finished successfully in ready().")

        # Optional: You can add checks here if you need Web3 for specific commands
        # is_running_server = 'runserver' in sys.argv or 'gunicorn' in sys.argv or 'uvicorn' in sys.argv
        # is_running_qcluster = 'qcluster' in sys.argv
        # if (is_running_server or is_running_qcluster) and initialize_web3:
        #    ... initialization logic ...