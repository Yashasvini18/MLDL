def try_catch():
    try:
        5/0
    except Exception as e:
        print(e)
try_catch()
