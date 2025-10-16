from diaries.DiarySample import DiarySample
from diaries.HIROTO_Diary import HIROTO_Diary
from diaries.VelasquezDiary import VelasquezDiary
from diaries.WatanabeDiary import WatanabeDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), WatanabeDiary(), HIROTO_Diary(), VelasquezDiary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
