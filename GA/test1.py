# 遺伝的アルゴリズムによるOneMax問題の最適化
# https://testpy.hatenablog.com/entry/2017/01/09/213846

import random
import math
import copy

N_PARAM = 10
N_POP = 20
N_GEN = 25
MUTATE_PROB = 0.1
ELITE_RATE = 0.2


class GA:
  def __init__(self):
    pass

  def main(self):
    pop = [(-1, p) for p in self.get_population()]

    for g in range(N_GEN):
      print('Generation: ' + str(g))

      # Get elites
      fitness = self.evaluate(pop)
      elites = fitness[:int(len(pop) * ELITE_RATE)]

      # Cross and mutate
      pop = elites[:]
      while len(pop) < N_POP:
        if random.random() < MUTATE_PROB:
          m = random.randint(0, len(elites) - 1)
          child = self.mutate(elites[m][1])
        else:
          c1 = random.randint(0, len(elites) - 1)
          c2 = random.randint(0, len(elites) - 1)
          child = self.crossover(elites[c1][1], elites[c2][1])
        pop.append((-1, child))

      # Evaluate indivisual
      fitness = self.evaluate(pop)
      pop = fitness[:]

      print(pop[0])

  def get_population(self):
    population = []
    for i in range(N_POP):
      arr = [random.randint(0, 1) for j in range(N_PARAM)]
      population.append(arr)

    return population

  def calc_score(self, x):
    return sum(x)

  def evaluate(self, pop):
    fitness = []
    for p in pop:
      if p[0] == -1:
        fitness.append((self.calc_score(p[1]), p[1]))
      else:
        fitness.append(p)
    fitness.sort()
    fitness.reverse()

    return fitness

  def mutate(self, parent):
    r = int(math.floor(random.random() * len(parent)))
    child = copy.deepcopy(parent)
    child[r] = (parent[r] + 1) % 2

    return child

  def crossover(self, parent1, parent2):
    length = len(parent1)
    r1 = int(math.floor(random.random() * length))
    r2 = r1 + int(math.floor(random.random() * (length - r1)))

    child = copy.deepcopy(parent1)
    child[r1:r2] = parent2[r1:r2]

    return child


if __name__ == "__main__":
  GA().main()
