from __future__ import division, print_function, absolute_import


from opendrivepy.roadmap import RoadMap
import opendrivepy.xmlparser

import xml.etree.ElementTree as ET
from datetime import datetime

class OpenDrive(object):
    def __init__(self, file):
        parser = opendrivepy.xmlparser.XMLParser(file)
        self.header = None
        self.roads = parser.parse_roads()
        self.junctions = parser.parse_junctions()
        self.controllers = list()
        # add lon lat
        self.lon,self.lat=parser.parse_lonlat()
        for junc_id, junction in self.junctions.items():
            max_arcrad = 0
            for connection in junction.connections:
                self.roads[connection.connecting_road].is_connection = True

                road = self.roads[connection.connecting_road]
                if road.arcrad > max_arcrad:
                    max_arcrad = road.arcrad
            # print(max_arcrad)
            self.junctions[junc_id].max_arcrad = max_arcrad
        # self.max_arcrad = max_arcrad
                
        self.junction_groups = list()   # no use for now
        self.stations = list()          # no use for now
        self.roadmap = RoadMap(self.roads)



