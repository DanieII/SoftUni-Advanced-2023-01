def repeat_text(word, times):
    try:
        print(word * int(times))
    except ValueError:
        print("Variable times must be an integer")


repeat_text(input(), input())
