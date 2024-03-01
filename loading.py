import asyncio
import sys

class Loading:
    def __init__(self):
        self.spinner = '|/-\\'
        self.spinner_index = 0
        self.running = False
        self.task = None

    def hide_cursor(self):
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()

    def show_cursor(self):
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()

    def clear_line(self):
        sys.stdout.write('\r\033[K')
        sys.stdout.flush()

    async def update(self):
        while self.running:
            sys.stdout.write('\rWaiting for assistant response... ' + self.spinner[self.spinner_index])
            sys.stdout.flush()
            self.spinner_index = (self.spinner_index + 1) % len(self.spinner)
            await asyncio.sleep(0.1)
        self.clear_line()
        self.show_cursor()

    def start(self):
        if not self.running:
            self.running = True
            self.hide_cursor()
            self.task = asyncio.create_task(self.update())

    async def stop(self):
        if self.running:
            self.running = False
            if self.task:
                await self.task
                self.task = None