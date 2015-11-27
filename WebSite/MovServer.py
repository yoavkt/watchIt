# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:34:06 2015


How to use the get
http://127.0.0.1:8080/api/*code*

Summary of codes:
 0 - kills the server
 1 - show all groups
 mts - movies to classify by the user
 mr;* - * is a group code the return value will be the recomended movies for the group
 
How to use the post
# curl -d title="0*Dead Man Walking (1995)-1*Bad Boys (1995)-3*Babe (1995)-1" -X POST "127.0.0.1:8080/api/"

where 0 is a group number then a tuple of movie name - rank seprated by *
You can enter as many movies as you want

@author: Yoav
"""

import cherrypy
import sys
sys.path.append('D:\\Dropbox\\DataHack\\WebSite\\');
import movieSelector as slc

class Movies:

    norm=slc.movieSelector()
    calssifier,umat=slc.getMovieCalssifier()
    mnames=slc.getMoviesToSelectFrom(numOfMovs=0,perm=0,filt=0)
    userID=1;
    groups={'0':[[('Crumb (1994)',1),('Doom Generation, The (1995)',2)],[('Firm, The (1993)',3),('All Dogs Go to Heaven 2 (1996)',4)]]}
    exposed = True
    def GET(self, id=None):
        if id=='0':
           return cherrypy.engine.exit()
        if id=='1':
           return slc.printDict(self.groups)
        if id == None:
            return('Send Codes')
        if id == 'mts':
            self.userID=self.userID+1;
            return str(self.userID-1)+';'+';'.join(slc.getMoviesToSelectFrom())
        if 'mr' in id:
            vals=id.split(';')
            if vals[1] in self.groups.keys():
                return ';'.join(slc.getSelectedMovies(self.groups[vals[1]],self.calssifier,self.umat,self.mnames))
            else:
                return 'No group'
            
    def POST(self, title):
        gpNum,vals=slc.parseGetMSg(title)
        if gpNum in self.groups.keys():
            tmp=self.groups[gpNum]
            tmp.append(vals)
            self.groups[gpNum]=tmp
        else:
            self.groups[gpNum]=[vals]
        return 'Added the data'

if __name__ == '__main__':

    cherrypy.tree.mount(
        Movies(), '/api/',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
