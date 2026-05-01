from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from logging_config import logger
from typing import Dict, Any

def place_order(client: Client, symbol: str, side: str, order_type: str, quantity: float, price: float = 0.0) -> Dict[str, Any]:
    """
    Places an order on the Binance Futures Testnet (USDT-M).
    """
    try:
        logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol} at {price if price else 'MARKET'}")
        
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        if order_type == 'LIMIT':
            order_params['price'] = price
            order_params['timeInForce'] = 'GTC' # Good Till Canceled is usually required for LIMIT orders
            
        logger.info(f"API Request params: {order_params}")
        
        # Use futures_create_order for USDT-M futures
        response = client.futures_create_order(**order_params)
        
        logger.info(f"API Response: {response}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Exception: Status code {e.status_code}, Message: {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Binance Request Exception: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while placing order: {str(e)}")
        raise
