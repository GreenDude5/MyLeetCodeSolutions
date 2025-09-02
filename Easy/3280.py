class Solution:
    def convertDateToBinary(self, date: str) -> str:
        day, month, year = date.split('-')
        day_bin = bin(int(day))[2:]
        month_bin = bin(int(month))[2:]
        year_bin = bin(int(year))[2:]
        return f"{day_bin}-{month_bin}-{year_bin}"
