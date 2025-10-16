from diaries.AbstractDiary import AbstractDiary

class VelasquezDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2でGitHubの使い方を学んだ。
専用のアプリがあっても正直しんどかった。。
Gitでの操作をルーチン的に解説したものがあったらと考えた。
"""
    def get_author(self):
        return "Velasquez"