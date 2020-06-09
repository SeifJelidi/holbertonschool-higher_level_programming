#!/usr/bin/python3
'''Class Base'''
import json
import os


class Base:
    '''The Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initilize Base attributes'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        L = []
        if not list_objs or list_objs is None:
            L = []
        else:
            for o in list_objs:
                L.append(o.to_dictionary())
        with open(cls.__name__ + '.json', 'w+', encoding='utf-8') as f:
            f.write(cls.to_json_string(L))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation json_string'''
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
        elif cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        fiche = cls.__name__ + '.json'
        if not os.path.exists(fiche):
            return []
        L = []
        with open(fiche, 'r', encoding='utf-8') as f:
            dicts = cls.from_json_string(f.read())
        for i in dicts:
            L.append(cls.create(**i))
        return L
