import random
import copy

# Define the graph
graph = {
    "A": [("B", 12), ("C", 4), ("D", 1000), ("E", 1000), ("F", 1000), ("G", 12)],
    "B": [("A", 12), ("C", 8), ("D", 12), ("E", 1000), ("F", 1000), ("G", 1000)],
    "C": [("A", 10), ("B", 8), ("D", 11), ("E", 3), ("F", 1000), ("G", 9)],
    "D": [("A", 1000), ("B", 12), ("C", 11), ("E", 11), ("F", 10), ("G", 1000)],
    "E": [("A", 1000), ("B", 1000), ("C", 3), ("D", 11), ("F", 6), ("G", 7)],
    "F": [("A", 1000), ("B", 1000), ("C", 1000), ("D", 10), ("E", 6), ("G", 9)],
    "G": [("A", 12), ("B", 1000),  ("C", 9), ("D", 1000), ("E", 7), ("F", 9)]
}

# Create a random initial population
def create_individual(cities):
    cities_ = copy.deepcopy(cities)
    cities_.remove("A")
    random.shuffle(cities_)
    cities_ = ['A'] + cities_
    return cities_

def generate_population(population_size: int, initial_cities: list):
  population = set()
  for _ in range(population_size):
    while True:
        individual = tuple(create_individual(initial_cities))
        if individual not in population:
            population.add(individual)
            break
  return population


def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        for neighbor, distance in graph[current_city]:
            if neighbor == next_city:
                total_distance += distance
                break

    # Add distance from the last city back to the starting city
    last_city = route[-1]
    for neighbor, distance in graph[last_city]:
        if neighbor == route[0]:
            total_distance += distance
            break

    return total_distance

def pmx_crossover(parent1:list, parent2:list):
  # print("Parents:")
  # print(parent1)
  # print(parent2)
  crossover_point = random.randint(1, len(parent1) - 1)
  c1_1 = parent1[:crossover_point]
  c1_2 = [city for city in parent2 if city not in c1_1]
  c2_1 = parent2[:crossover_point]
  c2_2 = [city for city in parent1 if city not in c2_1]
  child1 = c1_1 + c1_2
  child2 = c2_1 + c2_2
  return child1, child2

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Main genetic algorithm loop
# Define parameters
population_size = 50
population = set()
initial_cities = list(graph.keys())

population = generate_population(population_size, initial_cities)

best_route = None
best_distance = float('inf')
mutation_rate = 0.8
generations = 100

for generation in range(generations):
    new_population = set()

    for _ in range(population_size):
        parent1, parent2 = random.sample(population, 2)
        child1, child2 = pmx_crossover(list(parent1), list(parent2))
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        new_population.add(tuple(child1))
        new_population.add(tuple(child2))

    # population = new_population
    # print(population)
    current_best_route = min(population, key=lambda x: calculate_distance(list(x)))
    # print(f"current_best_route {generation}: {current_best_route}")
    current_best_distance = calculate_distance(list(current_best_route))

    if current_best_distance < best_distance:
        best_route = current_best_route
        best_distance = current_best_distance

    # Dynamic mutation rate decrease
    mutation_rate *= 0.95

# Find the best route in the final population
if best_route:
    best_distance = calculate_distance(list(best_route))
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
else:
    print("No valid routes found in the population.")