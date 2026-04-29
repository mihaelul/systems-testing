import unittest

class TestTreeFind(unittest.TestCase):
    
    def setUp(self):

        self.tree = Tree()
        
        elemente = [10, 5, 15, 3, 7, 20]
        for el in elemente:
            self.tree.add(el)

    def test_find_existing_node(self):
       
        rezultat = self.tree._find(7, self.tree.root)
        self.assertIsNotNone(rezultat)
        self.assertEqual(rezultat.data, 7)

    def test_find_non_existing_node(self):

        rezultat = self.tree._find(100, self.tree.root)
        self.assertIsNone(rezultat)

    def test_find_root_node(self):

        rezultat = self.tree._find(10, self.tree.root)       
        self.assertIsNotNone(rezultat)
        self.assertEqual(rezultat.data, 10)

if __name__ == '__main__':
    unittest.main()