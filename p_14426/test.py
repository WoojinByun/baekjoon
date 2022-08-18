import os
import unittest
from unittest.mock import patch
from io import StringIO

from solve import main


prob_dir = os.path.dirname(__file__)
files = sorted(os.listdir(prob_dir))
inputs = []
outputs = []
for file_name in files:
    if file_name.endswith('txt'):
        file_path = os.path.join(prob_dir, file_name)
        if file_name.startswith('input'):
            with open(file_path, 'r') as f:
                inputs.append(f.read().strip())
        elif file_name.startswith('output'):
            with open(file_path, 'r') as f:
                outputs.append(f.read().strip())


class Tests(unittest.TestCase):

    @patch("sys.stdin", StringIO(inputs[0]))
    @patch("sys.stdout", new_callable=StringIO)
    def test_solve_0(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), outputs[0] + '\n')

#     @patch("sys.stdin", StringIO(inputs[1]))
#     @patch("sys.stdout", new_callable=StringIO)
#     def test_solve_1(self, stdout):
#         main()
#         self.assertEqual(stdout.getvalue(), outputs[1] + '\n')

#     @patch("sys.stdin", StringIO(inputs[2]))
#     @patch("sys.stdout", new_callable=StringIO)
#     def test_solve_2(self, stdout):
#         main()
#         self.assertEqual(stdout.getvalue(), outputs[2] + '\n')

#     @patch("sys.stdin", StringIO(inputs[3]))
#     @patch("sys.stdout", new_callable=StringIO)
#     def test_solve_3(self, stdout):
#         main()
#         self.assertEqual(stdout.getvalue(), outputs[3] + '\n')


if __name__ == "__main__":
    unittest.main()
