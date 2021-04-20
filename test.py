import traceback
try:
    a = 0/0
except Exception as e:
    print(traceback.format_exc())
