# Simplified Trading Bot (Binance Futures Testnet)

This is a Python 3.x CLI application that places orders on the Binance Futures Testnet (USDT-M) using the `python-binance` library.

## Prerequisites
- Python 3.x
- Binance Futures Testnet API Key and Secret

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Environment Variables**:
   Create a `.env` file in the root directory (or export them in your terminal) with the following variables:
   ```env
   BINANCE_API_KEY=your_testnet_api_key
   BINANCE_API_SECRET=your_testnet_secret_key
   ```

## Usage

Run the CLI application using `python cli.py` with the required arguments.

### Arguments:
- `--symbol`: Trading symbol (e.g., BTCUSDT)
- `--side`: Order side (`BUY` or `SELL`)
- `--type`: Order type (`MARKET` or `LIMIT`)
- `--quantity`: Quantity to trade
- `--price`: Price (required only if `--type` is `LIMIT`)

### Examples:

**Place a MARKET BUY order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Place a LIMIT SELL order:**
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.05 --price 2000
```

## Logs
Logs for API requests, responses, and errors are stored in the `logs/app.log` file.
