from diaries.DiarySample import DiarySample
from diaries.HIROTO_Diary import HIROTO_Diary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), HIROTO_Diary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
