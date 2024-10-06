x, y = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day = 0
for i in range(1, x):
    day += days[i]
day = (day + y) % 7

print(weeks[day])