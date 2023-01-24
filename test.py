import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0]),num_rows)
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_entrance_is_broken(self):
        m1 = Maze(0,0,10,10,10,10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
    
    def test_maze_exit_is_broken(self):
        m1 = Maze(0,0,10,10,10,10)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_all_cells_reset(self):
        m1 = Maze(0,0,10,10,10,10)
        result = []
        for col in range(m1._num_cols):
            for row in range(m1._num_rows):
                if m1._cells[col][row].visited is False:
                    result.append(False)
        self.assertEqual(m1._num_cols * m1._num_rows, len(result)) 

if __name__ == "__main__":
    unittest.main()