import random
import sys
#Constants
GOAL_WEIGHT = 50000
NUM_FEMALES = 20
NUM_MALES = 20
INIT_MIN_WEIGHT = 200
INIT_MAX_WEIGHT = 600
INIT_MALE_AVERAGE = 350
INIT_FEMALE_AVERAGE = 250
MUTATE_PROB = 0.05
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_MAX = 5
GENERATION_LIMIT = 500

#Setup
males = []
for x in range(NUM_MALES) :
    males.append(random.triangular(INIT_MIN_WEIGHT, INIT_MAX_WEIGHT, INIT_MALE_AVERAGE))
females = []
for x in range(NUM_FEMALES) :
    females.append(random.triangular(INIT_MIN_WEIGHT, INIT_MAX_WEIGHT, INIT_MALE_AVERAGE))
new_children = []
new_males = []
new_females = []
v = 1
#Program
while True :
    males.sort()
    females.sort()
    if len(males) != NUM_MALES :
        males = males[-20:]
    if len(females) != NUM_FEMALES :
        females = females[-20:]
    print('Generation: ', v )
    v += 1
    print(' Largest male rat: ', males[-1])
    print(' Largest female rat: ', females[-1])
    if v == GENERATION_LIMIT :
        break
    if males[-1] >=  GOAL_WEIGHT :
        break
    if females[-1] >= GOAL_WEIGHT :
        break
    for x in females :
        random.choice(males)
        for i in range(LITTER_MAX) :
            if random.choice(males) > x :
                weight = random.triangular(x, random.choice(males))
            if random.choice(males) < x :
                weight = random.triangular(random.choice(males), x)
        if random.random() <= MUTATE_PROB :
            new_children.append(random.uniform(MUTATE_MIN, MUTATE_MAX) * weight)
        else:  
            new_children.append(weight)
    for x in new_children :
        random.randint(1,2)
        if random.randint(1,2) == 1 :
            new_males.append(x)
        if random.randint(1,2) == 2 :
            new_females.append(x)
    for x in new_males :
        males.append(x)
    for x in new_females :
        females.append(x)
  
    
 

    
