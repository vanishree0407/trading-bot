import os
from binance.client import Client
from dotenv import load_dotenv
from logging_config import logger

def get_binance_client() -> Client:
    load_dotenv()
    
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    if not api_key or not api_secret:
        error_msg = "BINANCE_API_KEY and BINANCE_API_SECRET environment variables must be set."
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    try:
        # Initialize client for Binance
        # testnet=True configures the client to point to the testnet endpoints
        client = Client(api_key, api_secret, testnet=True)
        logger.info("Binance client initialized successfully.")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize Binance client: {str(e)}")
        raise
