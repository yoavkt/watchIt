# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
#define matrix
umr_matrix=np.zeros((943,1682),dtype=np.int)
# define number of neigbords
k=10
#convert u.data to matrix
for i in range(100000):
    umr_matrix[udata[i,0]-1,udata[i,1]-1]=udata[i,2]
#run the algorithem
from sklearn.neighbors import NearestNeighbors
nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(umr_matrix)
#create fake new user for test
coming_user=np.zeros(1682,dtype=np.int)
for j in range(10):
    movie_index=round(np.random.uniform(0,1681))
    raw_grade=np.random.uniform(0,1)
    if raw_grade <= 0.33:
        grade=1
    elif raw_grade >= 0.67:
        grade=5
    else:
        grade=3
    coming_user[movie_index]=grade

#save close users indices and distances
close_users_dist, close_users_indx = nbrs.kneighbors(coming_user)

#compute recommendation
close_users_rec=umr_matrix[close_users_indx,]
for i in range(k):
    for j in range(1682):
        if close_users_rec[i,j]>0 and close_users_rec[i,j]<3

