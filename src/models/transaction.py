from dataclasses import dataclass, field

@dataclass
class Transaction:
    date: str = ""
    header: str = ""
    description_lines: list[str] = field(default_factory=list)

    withdrawal: float = 0.0
    deposit: float = 0.0
    tax: float = 0.0
    balance: float = 0.0