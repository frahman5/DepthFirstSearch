import unittest
import DFS


location = '/Users/faiyamrahman/Desktop/personal improvement/' \
              +'make_ money/programming/Design and Analysis of Algorithms I/SCC.txt'
x = DFS.Graph(location)

class TestDFS(unittest.TestCase):

##    def setUp(self):
##        self.location_DRone = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRone.txt'
##        self.location_DRtwo = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRtwo.txt'
##        self.location_DRthree = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRthree.txt'
##        self.location_DRfour = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRfour.txt'
##        self.location_DRfive = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRfive.txt'
##        self.location_DRsix = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRsix.txt'
##        self.location_DRseven = '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRseven.txt'
##        self.location_DReight= '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DReight.txt'
##        self.location_DRnine= '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRnine.txt'
##        self.location_DRten= '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/DRten.txt'
##        self.location_HW= '/Users/faiyamrahman/Desktop/personal improvement/' \
##              +'make_ money/programming/Design and Analysis of Algorithms I/SCC.txt'
##        self.G1 = DFS.Graph(self.location_DRone)
##        self.G2 = DFS.Graph(self.location_DRtwo)
##        self.G3 = DFS.Graph(self.location_DRthree)
##        self.G4 = DFS.Graph(self.location_DRfour)
##        self.G5 = DFS.Graph(self.location_DRfive)
##        self.G6 = DFS.Graph(self.location_DRsix)
##        self.G7 = DFS.Graph(self.location_DRseven)
##        self.G8 = DFS.Graph(self.location_DReight)
##        self.G9 = DFS.Graph(self.location_DRnine)
##        self.G10 = DFS.Graph(self.location_DRten)
##    def test_getDRG_one(self):
##        expected = (4,[[2,3],[4],[4],[2]])
##        test = DFS.getDirGraph(self.location_DRone)
##        self.assertEqual(expected,test)
##
##    def test_getDRF_two(self):
##        expected = (10,[[3],[1,4],[2,6],[5,6],[6],[7,10],[8],[4,9],[7],[9]])
##        test = DFS.getDirGraph(self.location_DRtwo)
##        self.assertEqual(expected,test)
##        
##    def test_getDRF_three(self):
##        expected = (10,[[3],[1,4],[2,6],[5,6],[],[7,10],[8],[4,9],[7],[9]])
##        test = DFS.getDirGraph(self.location_DRthree)
##        self.assertEqual(expected,test)
##
##    def test_topSort_one(self):
##        expected = [[1,2,3,4],[1,3,2,4]]
##        test = DFS.TopSort(self.G1)
##        self.assertTrue(test in expected)

    def test_FindSCCs_HW(self):
        expected = [434821,968,459,313,211]
        test = DFS.FindSCCs(x)[:5]
        self.assertEqual(expected,test)

##    def test_FindSCCs_one(self):
##        expected = [2,1,1]
##        test = DFS.FindSCCs(self.G1)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_two(self):
##        expected = [7,3]
##        test = DFS.FindSCCs(self.G2)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_three(self):
##        expected = [6,3,1]
##        test = DFS.FindSCCs(self.G3)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_four(self):
##        expected = [3,3,3]
##        test = DFS.FindSCCs(self.G4)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_five(self):
##        expected = [3,3,2]
##        test = DFS.FindSCCs(self.G5)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_six(self):
##        expected = [3,3,1,1]
##        test = DFS.FindSCCs(self.G6)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_seven(self):
##        expected = [7,1]
##        test = DFS.FindSCCs(self.G7)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_eight(self):
##        expected = [6,3,2,1]
##        test = DFS.FindSCCs(self.G8)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_nine(self):
##        expected = [6,1,1,1,1,1,1,1,1]
##        test = DFS.FindSCCs(self.G9)
##        self.assertEqual(expected,test)
##
##    def test_FindSCCs_ten(self):
##        expected = [3,2,2,2,1,1]
##        test = DFS.FindSCCs(self.G10)
##        self.assertEqual(expected,test)
##
##
##    def test_graphReverse_one(self):
##        """
##        Check that both the adjacency list representation of the graph
##        has reversed and that the individual vertices have updated their edges
##        """
##        expectedGraph = [[],[1,4],[1],[2,3]]
##        self.G1.selfReverse()
##        self.assertEqual(expectedGraph,self.G1.getGraph())
##        for i in range(0,4):
##            self.assertEqual(expectedGraph[i],self.G1.getVertices()[i].getEdges())
##
##    def test_graphReverse_two(self):
##        """
##        Same as above, except for G2
##        """
##        expectedGraph = [[2],[3],[1],[2,8],[4],[3,4,5],[6,9],[7],[8,10],[6]]
##        self.G2.selfReverse()
##        self.assertEqual(expectedGraph,self.G2.getGraph())
##        for i in range(0,10):
##            self.assertEqual(expectedGraph[i],self.G2.getVertices()[i].getEdges())
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestDFS)
unittest.TextTestRunner(verbosity=2).run(suite)


