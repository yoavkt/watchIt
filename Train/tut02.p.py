import random
import string


import cherrypy
import sys
sys.path.append('D:\\WebSite\\');
import movieSelector as slc

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

    @cherrypy.expose
    def movie(self):
        return slc.movieSelector()
    
    @cherrypy.expose
    def shutdown(self):  
        return cherrypy.engine.exit()

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
