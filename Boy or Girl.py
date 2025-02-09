def determine_gender(username):
    distinct_chars = set(username) 
    if len(distinct_chars) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

username = input().strip()
determine_gender(username)
