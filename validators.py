def validate_symbol(symbol: str) -> str:
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    return symbol.upper()

def validate_side(side: str) -> str:
    side = side.upper()
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'.")
    return order_type

def validate_quantity(quantity_str: str) -> float:
    try:
        quantity = float(quantity_str)
        if quantity <= 0:
            raise ValueError()
        return quantity
    except ValueError:
        raise ValueError("Quantity must be a positive number.")

def validate_price(price_str: str, order_type: str) -> float:
    if order_type.upper() == 'MARKET':
        return 0.0
    
    if not price_str:
        raise ValueError("Price is required for LIMIT orders.")
    
    try:
        price = float(price_str)
        if price <= 0:
            raise ValueError()
        return price
    except ValueError:
        raise ValueError("Price must be a positive number.")
