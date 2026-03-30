
from typing import List

TAX_RATE = 1.15

def calculate_totals(data: List[float], rate: float = TAX_RATE) -> List[float]:
    """Verilen veriler için oran uygular ve yeni değerleri döner."""
    return [amount * rate for amount in data]

def print_totals(totals: List[float]) -> None:
    """Toplamları ekrana yazdırır."""
    for total in totals:
        print(f"Total: {total:.2f}")

def log_totals(totals: List[float], filename: str = "log.txt") -> None:
    """Toplamları dosyaya ekler."""
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def process_data(data: List[float]) -> List[float]:
    """Verileri işler: hesaplar, ekrana basar ve loglar."""
    totals = calculate_totals(data)
    print_totals(totals)
    log_totals(totals)
    return totals
