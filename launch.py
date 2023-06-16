# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:03:22 2022

@author: 
"""
from citadel import *
from config import *
import pygame
# start to play the intro music of the Citadel
file = "citadel/web/src/KFT.mp3"
pygame.mixer.init()
music = pygame.mixer.music.load(file)

from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options

# start to load the Ice Crown Citadel
tornado.options.define('port',default=8000,type=int,help="this is the port >for application")


class IndexHandler(RequestHandler):
   def get(self):
       self.write('我们既然改变不了规则，那就做到最好')

if __name__ == '__main__':
   app = Application([(r'/',IndexHandler)])
   tornado.options.parse_command_line()

   pygame.mixer.music.play(loops = 3)

   http_server = HTTPServer(app)
   http_server.bind(tornado.options.options.port)
   http_server.start(1)
   #启动IOLoop轮循监听
   IOLoop.current().start()