def fix_case(s):
    lower_count = sum(1 for c in s if c.islower())  
    upper_count = len(s) - lower_count 
    
    if upper_count > lower_count:
        print(s.upper()) 
    else:
        print(s.lower())  
s = input().strip()
fix_case(s)
