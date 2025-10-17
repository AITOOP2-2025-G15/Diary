from diaries.DiarySample import DiarySample
from diaries.HIROTO_Diary import HIROTO_Diary
from diaries.VelasquezDiary import VelasquezDiary
from diaries.WatanabeDiary import WatanabeDiary
from diaries.YokoiDiary import YokoiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    WatanabeDiary(),
    HIROTO_Diary(),
    VelasquezDiary(),
    YokoiDiary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
