import random
import string

import cherrypy
import sys
sys.path.append('D:\\Dropbox\\DataHack\\WebSite\\');
import movieSelector as slc

#cherrypy.config.update({'server.socket_host': '0.0.0.0'})
#cherrypy.response.headers['Access-Control-Allow-Origin']='*'
shownMovies=[]

class StringGenerator(object):
    
    
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="testing" name="length" />
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""
        
        
    @cherrypy.expose
    def generate(self, length='Test'):
		# ''.join(random.sample(string.hexdigits, int(length)))
        movToSelect=slc.getMoviesToSelectFrom(shownMovies)
        return '\n'.join(movToSelect)
		
    @cherrypy.expose
    def shutdown(self):  
        return cherrypy.engine.exit()
		
if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())


# cross origin header cherrypy
