from typing import Dict, Any


class RequiredParameter(Exception):
    pass


class RequestsError(Exception):
    def __init__(self, response_text: Dict[str, Any]):
        super().__init__(response_text)
