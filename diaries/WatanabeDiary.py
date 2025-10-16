from diaries.AbstractDiary import AbstractDiary
class WatanabeDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "JRが遅延して遅刻しそうだった"
    def get_author(self):
        return "Watanabe"