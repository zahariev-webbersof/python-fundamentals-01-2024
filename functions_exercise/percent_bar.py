def loading_bar(percent):

    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{percent}% [{'%' * int(percent / 10)}{'.' * (10 - int(percent / 10))}]\nStill loading..."


number = int(input())
print(loading_bar(number))