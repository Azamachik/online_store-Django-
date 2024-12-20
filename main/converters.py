class FourDigitYearConverter:
    regex = r"\d{4}"

    def to_python(self, value: str) -> int:
        return int(value)

    def to_url(self, value: int) -> str:
        return f'{value:04d}'