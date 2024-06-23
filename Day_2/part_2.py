with open("Day_2/input.txt") as file:
    content = file.read().splitlines()

"""
approch: in each game, have something like this: {'red': max(n_red), 'green': max(n_green), 'blue': max(n_blue)}
                     p = n_red * n_green * n_blue
                    res += p
return res

Game 74: 5 red, 1 green; 1 blue, 5 red; 8 red, 3 blue
"""
def fewestNumber(content):
    res = 0
    for line in content:
        r, b, g = 0, 0, 0
        game, prints = line.split(':')
        prints = prints.split(';')
        for print in prints:
            n_colors = print.split(',')
            for n_color in n_colors:
                _,n, color = n_color.split(" ")
                n = int(n)
                if color == 'red':
                    r = max(r, n)
                elif color == 'green':
                    g = max(g, n)
                elif color == 'blue':
                    b = max(b, n)

        res += r * g * b
    return res

print(fewestNumber(content))