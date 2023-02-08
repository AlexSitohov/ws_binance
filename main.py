import json

import websocket


def on_message(ws, message):
    res = json.loads(message)
    # Если Разница текущей максимальной цены за час и текущей цены больше чем 1% от максимальной цены за час,
    # то выводиться 'Цена опустилась на 1 процент'
    max_value_per_hour = float(res.get('h'))
    current_value = float(res.get('c'))

    if (max_value_per_hour - current_value) > (max_value_per_hour / 100):
        print('Цена опустилась на 1 процент')
    print(message)


def on_close(ws):
    print("Connection closed")


def on_open(ws):
    print("Opened connection")


socket = 'wss://stream.binance.com:9443/ws/xrpusdt@ticker_1h'

ws = websocket.WebSocketApp(socket, on_message=on_message, on_open=on_open, on_close=on_close)

ws.run_forever()
