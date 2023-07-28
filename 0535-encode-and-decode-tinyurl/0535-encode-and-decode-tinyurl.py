class Codec:
    def __init__(self):
        self.dct = {}
        self.i = 0

    def encode(self, longUrl: str) -> str:
        self.dct[self.i] = longUrl
        self.i += 1
        return self.i - 1

    def decode(self, shortUrl: str) -> str:
        return self.dct[shortUrl]
        