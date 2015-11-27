# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:17:03 2015

@author: Yoav
"""

import sys
sys.path.append('D:\\Dropbox\\DataHack\\WebSite\\');
import movieSelector as slc
import json

# curl -d title="0*Dead Man Walking (1995)-1*Bad Boys (1995)-3*Babe (1995)-1" -X POST "127.0.0.1:8080/api/songs/"
A=[[('Crumb (1994)',1),('Babe (1995)',2)],[('Legends of the Fall (1994)',3),('All Dogs Go to Heaven 2 (1996)',4)]]
#calssifier,umat=slc.getMovieCalssifier()
mnames=slc.getMoviesToSelectFrom(numOfMovs=0,perm=0)
#res= slc.findMatchIndex('GoldenEye (1995)',mnames)
#M=slc.getSelectedMovies(A,calssifier,umat,mnames)
#cmnUser=slc.comingGroupToComingUser(A)

drankString='0*Dead Man Walking (1995)-1*Bad Boys (1995)-3*Ref, The (1994)-1'
gpNum,vals=slc.parseGetMSg(drankString)
groups={'0':[[('Crumb (1994)',1),('Doom Generation, The (1995)',2)],[('Firm, The (1993)',3),('All Dogs Go to Heaven 2 (1996)',4)]]}

tmp=groups[gpNum]
tmp.append(vals)
groups[gpNum]=tmp

B=A
B.append(vals)
dictString = json.dumps(B)