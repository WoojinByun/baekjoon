import os
import sys
import unittest
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

    def test_all(self):
        for i in range(len(inputs)):
            sys.stdin = StringIO(inputs[i])
            captured_output = StringIO()
            sys.stdout = captured_output
            main()
            self.assertEqual(captured_output.getvalue(), outputs[i] + '\n', f'Test {i} Failed')


if __name__ == "__main__":
    unittest.main()
