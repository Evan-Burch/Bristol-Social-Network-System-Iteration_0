# Edited by Evan Burch
from unittest import TestCase
from applayer.artistlist import ArtistList


class TestArtistList(TestCase):

    def setUp(self):
        ids = [938895, 2634203, 1141486, 908705, 2411933, 2304638, 3895080, 1448909, 1448911, 1141474, 2916175, 353265, 1141476, 938862, 1141491, 1141484, 1141487, 307357, 1141480, 516930, 1001138, 1141475, 269365, 1141488, 1141483, 1141489, 2867358, 2867360, 2189637, 908699, 1420640, 2867359, 1826135]
        self.artists = ArtistList(ids)
        self.allartists = ArtistList()
        self.empty_artists = ArtistList([])

    def test_bristol_artists(self):
        # There should be 33 artists in the list
        self.assertEqual(33, len(self.artists.artists))
        # Returned list must be sorted
        self.assertTrue(TestArtistList.isSorted(self.artists.artists, key=lambda x: x[1]))
        # Assuming the list is sorted, the following will be true
        self.assertEqual("B.F. Shelton", self.artists.artists[2][1])
        self.assertEqual("Jimmie Rodgers", self.artists.artists[16][1])

    def test_bristol_artists_empty(self):
        # There should be 0 artists in the list
        self.assertEqual(0, len(self.empty_artists.artists))
        # Returned list counts as sorted even with 0 elements
        self.assertTrue(TestArtistList.isSorted(self.empty_artists.artists, key=lambda x: x[1]))
        # Size of list should be 0
        self.assertGreater(1, len(self.empty_artists.artists))
        self.assertEqual(len(self.empty_artists.artists), 0)

    def test_artists(self):
        # There should be 179 artists in the list
        self.assertEqual(179, len(self.allartists.artists))
        # Returned list must be sorted
        self.assertTrue(TestArtistList.isSorted(self.allartists.artists, key=lambda x: x[1]))
        # Assuming the list is sorted, the following will be true
        self.assertEqual("A. P. Carter", self.allartists.artists[0][1])
        self.assertEqual("Alice Palmer", self.allartists.artists[3][1])

    def test_artists_objects(self):
        objs = self.artists.artist_objects
        self.assertEqual(1141486, objs[2].artistID)
        self.assertEqual("Irma Frost", objs[2].artistName)
        self.assertEqual(1, len(objs[2].collaborators))

    def test_artists_objects_empty(self):
        objs = self.empty_artists.artist_objects
        self.assertEqual(len(objs), 0)
        self.assertLess(len(objs), 1)

    def test_print(self):
        ids = [938895, 2634203, 1141486]
        artists = ArtistList(ids)
        outstring = "Ernest Stoneman (938895), Kahle Brewer (2634203), Irma Frost (1141486)"
        self.assertEqual(outstring, artists.__str__())
        self.assertEqual("Ernest Stoneman", artists.artists[0][1])
        self.assertEqual("Kahle Brewer", artists.artist_objects[1].artistName)

    def test_print_empty(self):
        ids = []
        artists = ArtistList(ids)
        outstring = ""
        self.assertEqual(outstring, artists.__str__())

    @staticmethod
    def isSorted(x, key=lambda x: x):
        return all([key(x[i]) <= key(x[i + 1]) for i in range(len(x) - 1)])

    def test_allartists_objects(self):
        a0 = next(item for item in self.allartists.artist_objects if item.artistID == 1826136)
        self.assertEqual("Stephen Tarter", a0.artistName)
        a0 = next(item for item in self.allartists.artist_objects if item.artistID == 5766040)
        self.assertEqual("Jim Seany", a0.artistName)
