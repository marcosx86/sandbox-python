#!/usr/bin/env python3

import asyncio
from signal import signal, SIGTERM
from os import getpid, remove
from time import sleep

class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal(SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True

async def loop_forever():
    processID = getpid()
    outputFile = open('whiletrue.pid', 'w')
    outputFile.write(str(processID))
    outputFile.close()
    killer = GracefulKiller()

    while not killer.kill_now:
        sleep(1)
        print(".", end="", flush=True)

    print(" Good bye...")
    remove('whiletrue.pid')

if __name__ == "__main__":
    asyncio.run(loop_forever())