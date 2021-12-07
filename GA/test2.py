# 遺伝的アルゴリズムでOneMax問題を解いてみる
# https://qiita.com/pontyo4/items/a986df2582f3d0aaaa40

# -*- coding: utf-8 -*-
import random
# import copy

# 各種パラメータ
length = 100  # 遺伝子長
population = 100  # 親個体数
offspring_n = 50    # 子個体数
generation = 100     # 世代数
mutation_rate = 1.0 / 100.0    # 突然変異確率(1/遺伝子長)

# 初期個体群生成


def initialize():
  gene = [[random.randint(0, 1) for i in range(length)] for j in range(population)]
  return gene

# 個体評価


def evaluate(gene):
  fitness = []
  for i in range(population):
    fitness.append(sum(gene[i]) / length)
  return fitness

# minを見つける


def find_min(fitness):
  min = 10
  for i in range(population):
    if fitness[i] < min:
      min = fitness[i]
  return min

# maxを見つける


def find_max(fitness):
  max = 0
  for i in range(population):
    if fitness[i] > max:
      max = fitness[i]
  return max

# 親選択


def choice_parents(gene, fitness):
  father_index = random.randint(0, population - 1)
  mother_index = random.randint(0, population - 1)
  if fitness[father_index] > fitness[mother_index]:
    parents = gene[father_index]
  else:
    parents = gene[mother_index]
  return parents

# 交叉


def crossover(father, mother):
  offspring = []
  for i in range(length):
    p = random.random()
    if p < 0.5:
      offspring.append(father[i])
    else:
      offspring.append(mother[i])
  return offspring

# 突然変異


def mutation(offspring):
  for i in range(length):
    p = random.random()
    if p < mutation_rate:
      if offspring[i] == 0:
        offspring[i] = 1
      else:
        offspring[i] = 0
  return offspring

# 個体更新(親個体エリート50 + 子個体50 = 計100)


def elite(gene, fitness, next_gene):
  sort_fitness = sorted(fitness, reverse=True)
  gen_tmp = []
  for i in range(int(population / 2)):
    index = fitness.index(sort_fitness[i])
    gen_tmp.append(gene[index])
  gen_tmp.extend(next_gene)
  return gen_tmp


def main():
  generation_count = 1
  next_gene = []

  # 初期個体群生成
  gene = initialize()

  while generation_count <= generation:
    next_gene.clear()
    # print(gene)
    # 個体評価
    fitness = evaluate(gene)
    min = find_min(fitness)
    max = find_max(fitness)
    print("generation:", generation_count)
    print("min", min)
    print("max", max)
    if min == 100:
      break
    # 次世代個体群生成
    for i in range(offspring_n):
      # 個体選択
      father = choice_parents(gene, fitness)
      mother = choice_parents(gene, fitness)
      # 交叉
      offspring = crossover(father, mother)
      # 突然変異
      offspring = mutation(offspring)
      next_gene.append(offspring)
    # 個体更新
    gene = elite(gene, fitness, next_gene)
    generation_count += 1
    print("--------------------------------")


if __name__ == "__main__":
  main()
