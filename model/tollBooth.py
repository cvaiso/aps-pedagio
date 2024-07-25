class TollBooth:
    def __init__(self, boothid, highway, status):
        self.boothid = boothid
        self.highway = highway
        self.status = status

    def __str__(self):
        return f"Booth ID: {self.boothid}, Highway: {self.highway}, Status: {self.status}"

    def to_dict(self):
        return {
            'boothid': self.boothid,
            'highway': self.highway,
            'status': self.status,
        }

    @classmethod
    def from_dict(cls, data):
        tollBooth = cls(data['boothid'], data['highway'], data['status']) 
        return tollBooth 