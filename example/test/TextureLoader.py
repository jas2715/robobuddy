import pygame
import HelperTexture
id = 0;
textures = {}
dicTextureIds = {}
screenSize = (0,0)
def helperRescale(img,scale):
    return pygame.transform.scale(img, (int(scale[0]) , int(scale[1]) )  )
def load(osPath, scale =()):
    idGenerated = str(osPath) + str(scale)
    if( idGenerated in dicTextureIds) : 
        print "TextureLoader DUPLICATED LOAD CALLS"
        return dicTextureIds[idGenerated]

    global id,screenSize;
    id += 1;
    
    #osPath = r"D:/Users/jas2715/Fractionauts-master/Fractionauts-master/" + osPath
    img = pygame.image.load(osPath).convert_alpha()
    if(scale != () ) : 
        img =HelperTexture.scale(img,scale)
    else :
        size = (img.get_width(),img.get_height() )
        size = (int(size[0] / 800.0 * screenSize[0]) , int(size[1]/ 600.0 *screenSize[1]) )
        img  = helperRescale(img,size)

    dicTextureIds[idGenerated] = id
    textures[id] =   img
    return id;

def loadSprite(posx, posy, width, height, sprite_sheet,scale =()):
    global id,screenSize;
    id += 1;

    image = pygame.Surface([width, height])
    image.fill((255,0,255))
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey((255,0,255))

    if(scale != () ) : 
        image = HelperTexture.scale(image,scale)
    else :
        size = (image.get_width(),image.get_height() )
        size = (int(size[0] / 800.0 * screenSize[0]) , int(size[1]/ 600.0 *screenSize[1]) )
        image  = helperRescale(image,size)

    #dicTextureIds[idGenerated] = id
    textures[id] =   image
    return id;

def get(id):
    return textures[id];