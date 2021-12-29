from datetime import datetime


class Task:
    def __init__(self, text: str, dead_line: datetime, priority: str):
        self.priority = priority
        self.dead_line = dead_line
        self.text = text

    @property
    def left(self):
        return self.dead_line - datetime.now()
