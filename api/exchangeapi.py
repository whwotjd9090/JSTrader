from .config import upbitconf


class Exchange:
    def __init__(self):
        self.access: str = upbitconf.KEY.ACCESS
        self.security: str = upbitconf.KEY.SECURITY
