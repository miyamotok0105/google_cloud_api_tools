#!/usr/bin/env python
# encoding: utf-8
from ctypes import *
import io
import cv2
import math
import random
import argparse
from enum import Enum
import matplotlib.pyplot as plt

from google.cloud import vision
from google.cloud.vision import types
#====================================

class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def draw_boxes_document_area(image, bounds, color):
    for bound in bounds:
        xmin  = int(bound["left"])
        ymin  = int(bound["top"])
        xmax  = int(bound["left"]+bound["width"])
        ymax  = int(bound["top"]+bound["height"])
        image = cv2.rectangle(image,(xmin, ymin),(xmax, ymax),(0,255,0),3)
    return image

#async
def get_document_area(image_file, feature):
    client = vision.ImageAnnotatorClient()
    bounds = []
    
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)
    
    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    for symbol in word.symbols:
                        if (feature == FeatureType.SYMBOL):
                            bounds.append(convert_format(symbol.bounding_box))

                    if (feature == FeatureType.WORD):
                        bounds.append(convert_format(word.bounding_box))

                if (feature == FeatureType.PARA):
                    
                    bounds.append(convert_format(paragraph.bounding_box))

            if (feature == FeatureType.BLOCK):
                bounds.append(convert_format(block.bounding_box))

        if (feature == FeatureType.PAGE):
            bounds.append(convert_format(block.bounding_box))
    return bounds



def convert_format(bounds):
    # print(bounds)
    left = bounds.vertices[0].x
    right = bounds.vertices[1].x
    top = bounds.vertices[0].y
    height = int(bounds.vertices[2].y) - int(bounds.vertices[0].y)
    bot = height / 2
    w = 0
    if int(bounds.vertices[1].x) > int(bounds.vertices[0].x):
        w = int(bounds.vertices[1].x) - int(bounds.vertices[0].x)
    else:
        w = int(bounds.vertices[0].x) - int(bounds.vertices[1].x)
    width = int(w)
    label = "text_deteil"
    prob = 100

    ref = {}
    ref["left"]   = left
    ref["top"]    = top
    ref["height"] = height
    ref["width"]  = width
    print(ref)
    # print("format2result end!")
    return ref


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    parser.add_argument('-out_file', help='Optional output file', default=0)
    args = parser.parse_args()
    filein = args.detect_file
    fileout = args.out_file

    image = cv2.imread(filein)
    #======================================
    #x y height width
    #======================================
    bounds = get_document_area(filein, FeatureType.PAGE)
    draw_boxes_document_area(image, bounds, 'blue')
    bounds = get_document_area(filein, FeatureType.PARA)
    draw_boxes_document_area(image, bounds, 'red')
    bounds = get_document_area(filein, FeatureType.WORD)
    draw_boxes_document_area(image, bounds, 'yellow')

    # #======================================
    # #xmin xmax ymin ymax
    # #======================================
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    

