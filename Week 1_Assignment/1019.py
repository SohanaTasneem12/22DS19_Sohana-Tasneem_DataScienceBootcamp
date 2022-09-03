def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%d:%d" % (hour, minutes, seconds)

n = int(input())
print(convert(n))

