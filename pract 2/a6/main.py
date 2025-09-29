N = int(input())
total_sec = N % (24 * 3600)
hours = total_sec // 3600
minutes = (total_sec % 3600) // 60
seconds = total_sec % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")