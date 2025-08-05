received_number = int(input())

def loading_bar_fun(rec_num:int):
    percents = received_number // 10
    points = 10 - percents
    if received_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{received_number}% [{percents * '%'}{points * '.'}]\nStill loading..."

print(loading_bar_fun(received_number))
