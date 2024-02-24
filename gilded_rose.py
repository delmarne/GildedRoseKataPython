# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    def get_items_by_name(self, name):
        return [item for item in self.items if item.name == name]

class Vest:
    def __init__(self, sell_in, quality):
        self.name = "+5 Dexterity Vest"
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.quality < 0:
            self.quality = 0
        if self.sell_in < 0:
            self.quality = self.quality -2
                
    def __eq__(self, other):
        if isinstance(other, Vest):
            return (
                self.name == other.name
                and self.sell_in == other.sell_in
                and self.quality == other.quality
            )
        return False
    
class AgedBrie:
    def __init__(self, sell_in, quality):
        self.name = "Aged Brie"
        self.sell_in = sell_in
        self.quality = quality
    
    def update_quality(self):
        self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.quality > 50:
            self.quality = 50

    def __eq__(self, other):
        if isinstance(other, AgedBrie):
            return (
                self.name == other.name
                and self.sell_in == other.sell_in
                and self.quality == other.quality
            )
        return False