class TestErrorException(Exception):
    def __init__(self, data):
        super.__init__()
        self.data = data

    def __str__(self):
        return repr(self.data)

