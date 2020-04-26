#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import svgwrite
from svgwrite import cm, mm
from recaman import calculate_racaman

maxlength = 50
scale = 2
middleline = (maxlength*scale)/2

def recamansvg(name):
    dwg = svgwrite.Drawing(filename=name, debug=True)
    path = dwg.add(dwg.g(id='path', stroke='black', stroke_width=0.1))
    placestaken = calculate_racaman(maxlength)
    odd = False
    for i in range(maxlength-1):
        if not (odd):
            print("M{},{} a1,1 0 0,0 {},0".format(min(placestaken[i]*scale, placestaken[i+1]*scale), middleline, max(placestaken[i]*scale, placestaken[i+1]*scale) -min(placestaken[i]*scale, placestaken[i+1]*scale)))
            path.add(dwg.path(d="M{},{} a1,1 0 0,0 {},0".format(min(placestaken[i]*scale, placestaken[i+1]*scale), middleline, max(placestaken[i]*scale, placestaken[i+1]*scale) -min(placestaken[i]*scale, placestaken[i+1]*scale)), fill_opacity="0"))
        else:
            print("M{},{} a1,1 0 0,0 {},0".format(max(placestaken[i]*scale, placestaken[i+1]*scale), middleline, 0-(max(placestaken[i]*scale, placestaken[i+1]*scale) -min(placestaken[i]*scale, placestaken[i+1]*scale))))
            path.add(dwg.path(d="M{},{} a1,1 0 0,0 {},0".format(max(placestaken[i]*scale, placestaken[i+1]*scale), middleline, 0-(max(placestaken[i]*scale, placestaken[i+1]*scale) -min(placestaken[i]*scale, placestaken[i+1]*scale))), fill_opacity="0"))
        odd = not odd
    dwg.save()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        if(sys.argv[1].isdigit()):
            maxlength = int(sys.argv[1])
    if (len(sys.argv) > 2):
        if(sys.argv[2].isdigit()):
            scale = int(sys.argv[2])
    recamansvg('recaman_curve.svg')