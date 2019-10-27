import os
import shutil
from unittest import TestCase

from DirTreeWalk.TreeWalk import TreeWalk


class TestTreeWalk(TestCase):
    def test_treewalk(self):

        try:
            # creates a temporary dir with a file in it
            dir_path = os.getcwd() + "\pythontestdir"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            f = open(dir_path + r"\test1.txt", "w+")
            for i in range(10):
                f.write("This is line %d\r\n" % (i + 1))
            f.close()
            # executing dir walk
            TreeWalk(dir_path).treewalk(dir_path)
        except:
            self.fail("unknown Exception thrown")
        finally:
            shutil.rmtree(dir_path)

    def test_output(self):
        expected = f'path\tpath\tchecksum'
        self.assertEqual(expected, TreeWalk.output("path", "path", "checksum"))

    def test_lokal_with_a_lot_of_files(self):
        dir_path = r'C:/'
        try:
            # executing dir walk
            TreeWalk(dir_path).treewalk(dir_path)
        except:
            self.fail("unknown Exception thrown")
