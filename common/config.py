# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os

def get_config():
    config = dict()
    dir_path = os.path.dirname(os.path.realpath(__file__))

    tree = ET.parse(dir_path + '/../config.xml')
    root = tree.getroot()

    for configs in root.iter("configs"):
        for xml_data in configs:
            config[xml_data.attrib["name"]] = xml_data.attrib["value"]

    label = config["label"]

    temp_config = dict()
    tree = ET.parse(dir_path + '/../config-%s.xml' % label)
    root = tree.getroot()

    for configs in root.iter("configs"):
        for xml_data in configs:
            temp_config[xml_data.attrib["name"]] = xml_data.attrib["value"]

    for key in temp_config.keys():
        config[key] = temp_config[key]

    return config
