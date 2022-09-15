from dataclasses import dataclass


@dataclass
class ValidationError(Exception):
    message: str