from os import walk
import pygame

def import_folder(path):
#this constructs a path to the animation image we want, using walk to move through folders on the hard drive.
#then we loop through the images in the folder and build the image path, assigning it to the full path variable and adding it to thge list 'surface_list
#
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
            
    return surface_list
    
