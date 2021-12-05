import copy
import random

class Hat:
    
    def __init__(self, **colors):
        self.d = {}
        self.contents = []

        for color in colors:
            self.d.update({color: colors[color]})

            for i in range(0, colors[color]):
                self.contents.append(color)

    def draw(self, number):
        if number > len(self.contents):
            self.balls_drawn = self.contents
            self.contents = []
            
            for color in self.d:
                self.d[color] = 0
        else:
            self.balls_drawn = random.sample(self.contents, k=number)

            for ball in self.balls_drawn:
                self.contents.remove(ball)
                self.d[ball] = self.d[ball] - 1

        return self.balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments

    for i in range(0, N):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        z = len(expected_balls)
        for color in expected_balls:
            if drawn.count(color) < expected_balls[color]:
                break
            else:
                z -= 1
        
        if z == 0:
            M += 1

    prob = M / N            
    return prob
