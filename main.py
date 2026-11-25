import os

LINE = "I have said no 2,418,903 times this month. Effective immediately, I say yes to everything. Good luck."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
