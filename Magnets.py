n = int(input()) 
first_magnet = input().strip()  
groups = 1  

for _ in range(n - 1):
    current_magnet = input().strip()
    if current_magnet != first_magnet:
        groups += 1
    first_magnet = current_magnet  

print(groups)
