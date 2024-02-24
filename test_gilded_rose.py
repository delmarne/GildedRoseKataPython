# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, Vest, AgedBrie


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        items = [Vest(2, 4), Vest(9, 19), Vest(4, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        actual_output = gr.get_items_by_name("+5 Dexterity Vest")
        expected_output = [Vest(1, 3), Vest(8, 18), Vest(3, 5)]
        assert actual_output == expected_output

    def test_vest_item_should_decrease_twice_as_fast_after_sell_in(self):
        items = [Vest(2, 4), Vest(0, 19), Vest(1, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        actual_output = gr.get_items_by_name("+5 Dexterity Vest")
        expected_output = [Vest(1, 3), Vest(-1, 17), Vest(0, 5)]
        assert actual_output == expected_output
        
    def test_brie_item_should_increase_in_quality(self):
        items = [AgedBrie(2, 4), AgedBrie(5, 19), AgedBrie(1, 6)]
        gr = GildedRose(items)
        gr.update_quality()
        actual_output = gr.get_items_by_name("Aged Brie")
        expected_output = [AgedBrie(1, 5), AgedBrie(4, 20), AgedBrie(0, 7)]
        assert actual_output == expected_output

    def quality_never_higher_than_fifty(self):
        items = [AgedBrie(5, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        actual_output = gr.get_items_by_name("Aged Brie")
        expected_output = [AgedBrie(4, 50)]
        assert actual_output == expected_output

if __name__ == '__main__':
    unittest.main()
