from utils.Plugin import Plugin

class PrintTest(Plugin):
    def __init__(self):
        super().__init__()
        print("Print Test plugin running")

x = PrintTest()