import json

import websocket


def on_message(ws, message):
    res = json.loads(message)
    if float(res.get('h')) - float(res.get('c')) > float(res.get('h')) / 100:
        print('Цена опустилась на 1 процент')
    print(message)


def on_close(ws):
    print("Connection closed")


def on_open(ws):
    print("Opened connection")


socket = 'wss://stream.binance.com:9443/ws/xrpusdt@ticker_1h'

ws = websocket.WebSocketApp(socket, on_message=on_message, on_open=on_open, on_close=on_close)

ws.run_forever()
