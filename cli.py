import argparse
import sys
from bot.validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price
from bot.client import get_binance_client
from bot.orders import place_order
from logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Simplified Trading Bot (Binance Futures Testnet)")
    
    parser.add_argument("--symbol", type=str, required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=["BUY", "SELL", "buy", "sell"], help="Order side: BUY or SELL")
    parser.add_argument("--type", type=str, required=True, choices=["MARKET", "LIMIT", "market", "limit"], help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", type=str, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=str, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        # 1. Validate inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print(f"Inputs validated: {side} {quantity} {symbol} at {order_type} price {price if order_type == 'LIMIT' else 'MARKET'}")

        # 2. Initialize client
        print("Initializing Binance client...")
        client = get_binance_client()

        # 3. Place order
        print("Placing order...")
        result = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # 4. Print useful order results
        print("\n=== Order Placed Successfully ===")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Symbol: {result.get('symbol')}")
        print(f"Status: {result.get('status')}")
        print(f"Type: {result.get('type')}")
        print(f"Side: {result.get('side')}")
        print(f"Executed Quantity: {result.get('executedQty')}")
        if result.get('avgPrice') and float(result.get('avgPrice', 0)) > 0:
            print(f"Average Price: {result.get('avgPrice')}")
            
    except ValueError as ve:
        print(f"\n[Validation Error] {str(ve)}")
        logger.error(f"Validation Error: {str(ve)}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[Execution Error] An error occurred while placing the order. Check logs/app.log for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()
