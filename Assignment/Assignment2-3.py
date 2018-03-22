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
    def check(i, j, doa):
        num = 0
        index = [[i-1,j-1],[i-1,j],[i-1,j+1],
                 [  i,j-1],        [  i,j+1],
                 [i+1,j-1],[i+1,j],[i+1,j+1]]
        for s in range(8):
            num = num + p[index[s][0],index[s][1]]
        if doa == 1:
            if num < 2:
                return 0
            if num == 2 or num == 3 :
                return 1
            if num > 3 :
                return 0
        if doa == 0 and num == 3:
            return 1
        return num
    for u in range(1,19):
        for v in range(1,12):
            p[u,v] = check(u,v,p[u,v])             
    p = p[1:19, 1:12]
    #### END YOUR CODE HERE ####
    return p

for it in range(15):
    pattern = game_of_life(pattern)
    print('Iteration #',it+1)
    print(pattern)
