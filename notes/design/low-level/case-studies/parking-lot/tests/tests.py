import unittest
from Driver import process_file


class TestDriver(unittest.TestCase):
    def read_from_file(self, filepath):
        with open(filepath, "r") as content_file:
            content = content_file.read()
            return content

    def check_file(self, idx):
        in_file = "inputs/in" + idx + ".txt"
        out_file = "outputs/out" + idx + ".txt"
        actual_output = process_file(in_file)
        expected_output = self.read_from_file(out_file)
        self.assertEqual(actual_output, expected_output)

    def test1(self):
        idx = "1"
        self.check_file(idx)

    def test2(self):
        idx = "2"
        self.check_file(idx)

    def test3(self):
        idx = "3"
        self.check_file(idx)

    def test4(self):
        idx = "4"
        self.check_file(idx)


if __name__ == "__main__":
    unittest.main()
