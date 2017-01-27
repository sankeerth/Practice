data = input()
data = data.split(' ')
n = int(data[0])
k = int(data[1])

data = input()
cost = data.split(' ')

lights = [1 for x in range(n)]

def toggle(index, k):
    print(index)

def turn_off():
    for i in lights[1:5]:
        lights[i] = 0
    print(lights)
turn_off()