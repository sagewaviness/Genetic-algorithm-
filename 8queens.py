from itertools import permutations
import random
import numpy as np

genomesize = 8
class individual:
  def __init__(self):
    self.fitness = 0
    self.genome = []
    self.genome = np.random.permutation(8)

    print(self.genome)
    self.board = [[0 for i in range(genomesize)] for j in range(genomesize)] 
    self.print_board()
    self.fitness_score()
  
  def fitness_score(self):
    self.fitness = 0 
    for col in range(genomesize):
      for row in range(genomesize):
        if(row != col):
          x = abs(col - row)
          y = abs(self.genome[col] - self.genome[row])
          if( x == y ):
            self.fitness += 1
  
    print("Fitness Score: " + str(self.fitness))

  def print_board(self):
    print('\n' + "Queens Board")
    
    # mark queens 
    for i in range(genomesize):
      self.board[self.genome[i]][i] = 1

    # print rows 
    for row in self.board: 
      print(row)


  def mutate(self):
    a = random.randint(0,7)
    b = random.randint(0,7)

    # swap variables
    temp = self.genome[a]
    self.genome[a] = self.genome[b]
    self.genome[b] = temp
def crossover(ind1, ind2):
  # get random crossover point not including the end points
  point = random.randint(1,6)

  # copy parent genomes to crossover 
  p1 = ind1.genome
  p2 = ind2.genome

  # empy array to place new crossed over genes 
  c1 = []
  c2 = []

  # Copy over array before crossover point 
  for x in range(point):
    if (x <= point):
      c1.append(p1[x])
      c2.append(p2[x])
  
  # start index at x-over point 
  
  # check if not in the array and crossover 
  # cycle to begining to maintain permutation 
  while(len(c1) < len(p1) or len(c2) < len(p2)):
    
    if p2[point] not in c1 and len(c1) < len(p1):
      c1.append(p2[point])
    if p1[point] not in c2 and len(c2) < len(p2):
      c2.append(p1[point])
    point += 1
    point = point % 8

  # create individuals as children
  child1 = individual()
  child2 = individual()

  # make the genome equal new childrens
  child1.genome = c1
  child2.genome = c2

  # return two children 
  return child1, child2


def selection(population):
  # array for 3 individual tourney 
  ind = []
  
  tourney = 3
  # add random individuals 
  for n in range(tourney):
    ind.append(random.randint(0,pop_size - 1))

  min = 101
  # fine best fit in tourney 
  for n in range(tourney):
    if ind[n] < min:
      min = ind[n] 

  
  # index space where best fitness is 
  return population[min]



def survival(population):

  # find parents
  p1 = selection(population)
  p2 = selection(population)
  
  # get children 
  c1 , c2 = crossover(p1,p2)

  if random.random() < 0.2:
    c1.mutate()
  if random.random() < 0.2:
    c2.mutate()

  # removes worst 2 individuals from sorted population
  population.pop()
  population.pop()

  # add children back to the population 
  population.append(c1)
  population.append(c2)

  return population

def generate_all_solutions():
  # random number given possible solutions
  rand_ind = random.randint(1,91) 
  # print(rand_ind)
  counter = 0

  # initialize varibles 
  num_queens = 8
  cols = range(8)

  # iterate through solutions until rand num = counter
  for arr in permutations(cols):
      if (num_queens == len(set(arr[i]+i for i in cols))
          == len(set(arr[i]




# initialize varibales

pop_size = 100
population = []
pop_iteration = 1000

bestFit = []
worstFit = []
aveFit = []

# initialize population 
for i in range(pop_size):
  population.append(individual())

# sort initial pop
population.sort(key=lambda x: x.fitness)


# iterate generationally 
for i in range(pop_iteration):
  population = survival(population)
  population.sort(key=lambda x: x.fitness)

  bestFit.append(population[0].fitness)
  worstFit.append(population[pop_size - 1].fitness)

  totalsum = 0
  for x in range(pop_size):
    totalsum += population[x].fitness 

  average = totalsum/pop_size
  aveFit.append(average)

  if i == 0:
    print("initial Generation")
    print(bestFit[i], worstFit[i], aveFit[i])
  if i == pop_size - 1:
    print("Final Generation")
    print(bestFit[i], worstFit[i], aveFit[i])


