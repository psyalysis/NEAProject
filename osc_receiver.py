import asyncio

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer

class OSCReceiver:
    def __init__(self, ip="0.0.0.0", port=8000):
        self.ip = ip
        self.port = port
        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self._default_handler)
        self.received_messages = []

    def _default_handler(self, address, *args):
        print(f"Received OSC message: {address} {args}")
        self.received_messages.append((address, args))

    async def start(self):
        server = AsyncIOOSCUDPServer((self.ip, self.port), self.dispatcher, asyncio.get_event_loop())
        transport, protocol = await server.create_serve_endpoint()
        print(f"OSC Receiver listening on {self.ip}:{self.port}")
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass
        transport.close()

if __name__ == "__main__":
    receiver = OSCReceiver()
    asyncio.run(receiver.start())
