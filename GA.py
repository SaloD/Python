import random
import math

GENOME_LENGTH = 10

class Individual:
    'Representative sf the population'

    def __init__(self):
        self.genome = [False] * GENOME_LENGTH

    def init_random_genome(self):
        for i in range(GENOME_LENGTH):
            if random.random() < 0.5:
                self.genome[i] = True
            else:
                self.genome[i] = False

    def to_decimal(self):
        val = 0.0
        for i in range(GENOME_LENGTH):
            if self.genome[i]:
                val += 2**(GENOME_LENGTH/2-i-1)
        return val

    def mutation(self):
        index = random.randint(0, GENOME_LENGTH-1)
        self.genome[index] = not self.genome[index]

    def crossingover(self, wife):
        index = random.randint(0, GENOME_LENGTH-1)
        son = Individual()
        for i in range(0, index):
            son.genome[i] = self.genome[i]
        for j in range(index, GENOME_LENGTH):
            son.genome[j] = wife.genome[j]
        return son

def fitness_func(individual):
    x0 = 0.0
    x1 = individual.to_decimal()
    math.sqrt((x0-x1)**2)

adam = Individual()
adam.init_random_genome()
print(adam.genome)
#print(adam.to_decimal())
#adam.mutation()
#print(adam.genome)
#print(adam.to_decimal())
eve = Individual()
eve.init_random_genome()
print(eve.genome)
avel = adam.crossingover(eve)
#print(avel.genome)
