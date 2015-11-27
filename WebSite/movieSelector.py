import numpy as np
from sklearn.neighbors import NearestNeighbors
import json

# define constants
k=10 #num of neighbours
num_of_ret_rec = 11
n_users = 943
n_items = 1682
n_ratings = 100000


def movieSelector():
    return ['MovieName','HHHH','Hello']
	
def getMovieCalssifier(k=10,alg='ball_tree'):
    #import data
    udata_str=np.loadtxt('D:\\Dropbox\\DataHack\\WebSite\\Data\\u.data',delimiter='\t' ,dtype='str')
    #define the right data type of the columns
    udata=np.zeros((n_ratings,3),dtype=np.int)
    udata[:,0]=[int(i) for i in udata_str[:,0]]
    udata[:,1]=[int(i) for i in udata_str[:,1]]
    udata[:,2]=[int(i) for i in udata_str[:,2]]
    #define matrix
    umr_matrix=np.zeros((n_users,n_items),dtype=np.int)
    #convert u.data to matrix
    for i in range(n_ratings):
        umr_matrix[udata[i,0]-1,udata[i,1]-1]=udata[i,2]
        
    nbrs = NearestNeighbors(n_neighbors=k, algorithm=alg).fit(umr_matrix)
    return (nbrs,umr_matrix)

def comingGroupToComingUser(cominggroup):
    # this should be in a global variabl
    mnames=getMoviesToSelectFrom(numOfMovs=0,perm=0,filt=0)
    cominguser=np.zeros((len(cominggroup),n_items ))
    for i in range(len(cominggroup)):
        for j in range(len(cominggroup[i])):
            v=findMatchIndex(cominggroup[i][j][0],mnames)
            cominguser[i,v]=cominggroup[i][j][1]
    return cominguser

def findMatchIndex(name,nameList):
    for i in range(len(nameList)):
        if name==nameList[i]:
            return i
    return -1

def getSelectedMovies(comingGroup,calssifier,umr_matrix,uitem_str):
	# choices is a list of list. Each sub list is a user. Each cell in the sublist
	# is a tuple of a movie and rank. It looks like this 
	# A=[[('hello',1),('Baby',2)],[('world',3),('mike',4)]]
	# accessing the data is like this A[i][j][l]
	# i will give you the user index, j is his movie index and l is the parameter
	# if l=0 you will get the movie name if l=1 you will get the rank.
	# the calssifier is the classifier created by the getMovieCalssifier function above.
	# the fundtion will return a list of movie names.
	#import data
    comminguser=comingGroupToComingUser(comingGroup)
    close_users_dist, close_users_indx = calssifier.kneighbors(comminguser)
    close_users_rec=umr_matrix[close_users_indx,]
    close_users_rec_weighted=np.zeros((k,n_items),dtype=np.int)
    for i in range(k):
        for j in range(1682):
            if close_users_rec[0,i,j]>0 and close_users_rec[0,i,j]<3:
                close_users_rec_weighted[i,j]=-1
            elif close_users_rec[0,i,j]==3 or close_users_rec[0,i,j]==0:
                close_users_rec_weighted[i,j]=0
            else:
                close_users_rec_weighted[i,j]=1
                # sum of recommendation for coming user
    rec_movies=close_users_rec_weighted.sum(axis=0)
    # sort by recommendation rank
    top_movies=np.argsort(-rec_movies)
    #return the recommendations
    return_movies=[]
    for i in range(num_of_ret_rec):    
        return_movies.append(uitem_str[top_movies[i]])
    return return_movies
	#return ['Toys story','Jurassic park','Little Shop of Horrors']

def getNewMoviesToGrade(oldMov):
    return 
	
def getMoviesToSelectFrom(numOfMovs=20,perm=1,fname='D:\\Dropbox\\DataHack\\WebSite\\Data\\u.item',filt=1,filtfile='D:\\Dropbox\\DataHack\\WebSite\\Data\\primeQuest.txt'):    
    movs=np.loadtxt(fname, dtype='str', delimiter='|')
    filterLoc=np.loadtxt(filtfile,dtype='int',delimiter='\t')
    mfilterLoc=[i-1 for i in filterLoc[:,1]]
    
    movName=movs[:,1]
    if(filt):
        movName=movs[mfilterLoc,1]
    if(perm):
        movName=np.random.permutation(movName)    
    if numOfMovs>0 :
        return movName[1:numOfMovs]
    else:
        return movName
        
def getMoviesInFormat(numOfMovs=20,perm=1,fname='D:\\Dropbox\\DataHack\\WebSite\\Data\\u.item'):
    baselist=getMoviesToSelectFrom(numOfMovs,perm,fname)
    
def parseGetMSg(pStr):
    strList=pStr.split('*')
    valsList=strList[1:]
    tplist=[];
    for pp in valsList:
        tmp=pp.split('-')
        tplist.append((tmp[0],int(tmp[1])))
    return (strList[0],tplist)
    
def printDict(B):
    return json.dumps(B)