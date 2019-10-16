import numpy as np
import copy
import time

t1 = time.time()


grille = np.array([[1,0,0,0,0,7,0,9,0],
                    [0,3,0,0,2,0,0,0,8],
                    [0,0,9,6,0,0,5,0,0],
                    [0,0,5,3,0,0,9,0,0],
                    [0,1,0,0,8,0,0,0,2],
                    [6,0,0,0,0,4,0,0,0],
                    [3,0,0,0,0,0,0,1,0],
                    [0,4,0,0,0,0,0,0,7],
                    [0,0,7,0,0,0,3,0,0]],
                    dtype = object)





def resoudre(grille, level = 0):
    subgrid_x = [[0,1,2]]*3+[[3,4,5]]*3+[[6,7,8]]*3
    subgrid_y = [[0,1,2]]*3+[[3,4,5]]*3+[[6,7,8]]*3
    grille_possible = copy.copy(grille)
    nombres = {1,2,3,4,5,6,7,8,9}
    min_len = 6
    try:
        list(np.unique(grille)).index(0)
    except:
        return grille, True  
    for x in range(grille.shape[1]):
        for y in range(grille.shape[0]):
            if grille[y,x] == 0:
                unique_x = list(np.unique(grille[:,x]))
                unique_y = list(np.unique(grille[y,:]))
                unique_subgrid = list(np.unique(grille[min(subgrid_y[y]):max(subgrid_y[y])+1,min(subgrid_x[x]):max(subgrid_x[x])+1]))
                list_possible = list(nombres-set(unique_x+unique_y+unique_subgrid))
                grille_possible[y,x] = list_possible 
            if type(grille_possible[y,x]) == list:
                if len(grille_possible[y,x]) == 0:
                    return grille, False
                if len(grille_possible[y,x]) < min_len:
                    min_len = len(grille_possible[y,x])
                    modif_list = [y,x,grille_possible[y,x]]
    for number in modif_list[2]:
        grille2 = copy.copy(grille)
        grille2[modif_list[0],modif_list[1]] = number
        result = resoudre(copy.copy(grille2),level+1)
        if result[1]:
            return result[0], True
    return grille, False
    

print(resoudre(grille)[0])

print( str(time.time()-t1)[:4], " secondes")
