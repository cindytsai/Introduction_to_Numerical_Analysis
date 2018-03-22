import numpy as np

pattern = \
np.array([[0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0]], dtype='int64')

def game_of_life(p):
    ### START YOUR CODE HERE ###
    p = np.insert(p, 0, 0, axis = 0)
    p = np.insert(p,19, 0, axis = 0)
    p = np.insert(p, 0, 0, axis = 1)
    p = np.insert(p,12, 0, axis = 1)
    ori = np.zeros((20,13))
    for u in range(1,19):
        for v in range(1,12):
            num = np.sum(p[u-1:u+2,v-1:v+2]) - p[u,v]
            if p[u,v] == 1:
                if num < 2 :
                    ori[u,v] = 0
                if num == 2 or num == 3 :
                    ori[u,v] = 1
                if num > 3 :
                    ori[u,v] = 0
            if p[u,v] == 0:
                if num == 3 :
                    ori[u,v] = 1
    p = ori[1:19, 1:12]
    #### END YOUR CODE HERE ####
    return p

for it in range(15):
    pattern = game_of_life(pattern)
    print('Iteration #',it+1)
    print(pattern)
