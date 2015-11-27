

import numpy as np

def movieSelector():
	return 'MovieName'
	
def getMovieCalssifier():
	
	return 'HelloWorld'
	
def getSelectedMovies(choices,calssifier):
	# choices is a list of list. Each sub list is a user. Each cell in the sublist
	# is a tuple of a movie and rank. It looks like this 
	# A=[[('hello',1),('Baby',2)],[('world',3),('mike',4)]]
	# accessing the data is like this A[i][j][l]
	# i will give you the user index, j is his movie index and l is the parameter
	# if l=0 you will get the movie name if l=1 you will get the rank.
	# the calssifier is the classifier created by the getMovieCalssifier function above.
	# the fundtion will return a list of movie names.
	
	return ['Toys story','Jurassic park','Little Shop of Horrors']

def getNewMoviesToGrade(oldMov):
	return 
	
def getMoviesToSelectFrom(numOfMovs=20,fname='D:\\Dropbox\\DataHack\\WebSite\\Data\\u.item'):
	movs=np.loadtxt(fname, dtype='str', delimiter='|')
	movName=movs[:,1]
	movName=np.random.permutation(movName)
	return movName[1:21]