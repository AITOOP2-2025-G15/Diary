from diaries.AbstractDiary import AbstractDiary

class YokoiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "最悪な一日だった"
    def get_author(self):
        return "Yokoi"
