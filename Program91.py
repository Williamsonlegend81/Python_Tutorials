import time

t = time.localtime()
print(t)
formatted_string = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_string)