from enum import Enum


class PayableWith(str, Enum):
    ALL = "all"
    CREDIT_CARD = "credit_card"
    BANK_SLIP = "bank_slip"
    PIX = "pix"


class IntervalType(str, Enum):
    WEEKS = "weeks"
    MONTHS = "months"
