def untreated_crimes(n, events):
    available_officers = 0
    untreated = 0
    for event in events:
        if event == -1:
            if available_officers > 0:
                available_officers -= 1  
            else:
                untreated += 1  
        else:
            available_officers += event  
    return untreated
n = int(input())
events = list(map(int, input().split()))
print(untreated_crimes(n, events))
