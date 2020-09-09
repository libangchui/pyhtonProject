# -*- coding: utf-8 -*-

class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
        
if  __name__=="__main__":
    dog_layer=simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print ("Background:",dog_layer.getBackgroud())
    print ("Painting:",dog_layer.getContent())
 
    
#拷贝图层
from copy import copy, deepcopy
class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)
if  __name__=="__main__":
    dog_layer=simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0,0,255,0])
    print ("Background:",dog_layer.getBackgroud())
    print ("Painting:",dog_layer.getContent())
    another_dog_layer=dog_layer.clone()
    print ("Background:", another_dog_layer.getBackgroud())
    print ("Painting:", another_dog_layer.getContent())
    