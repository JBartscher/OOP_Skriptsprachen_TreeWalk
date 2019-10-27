import argparse  # favored over click library because the dir walk than would need additional packages
import hashlib
import os.path
import pathlib


class TreeWalk:
    """
    TreeWalk is a class to cycle recursive through a directory and its child directories
    and print intel about those files as well as a md5 checksum of its containing files.
    """

    # Configure Args Parser
    parser = argparse.ArgumentParser(prog="TreeWalk", description='DirTreeWalk for a given path')
    parser.add_argument('path', metavar='path', type=str, nargs='+',
                        help='path to show')

    def __init__(self, path):
        """
        constructor
        :param path: path from which the tree walk will be executed
        """
        self._path = path
        self._path_len = len(path)
        if not os.path.exists(self._path):
            raise FileExistsError(f'Error: Path not found: {self._path}')

    def treewalk(self, path):
        """
        recursively walk through a dir
        :param path: path
        :return: nothing
        """
        # checks if path is a directory
        try:
            if os.path.isdir(path):
                print(self.output(path, "<dir>"))
                for file in os.listdir(path):
                    self.treewalk(path=f'{path}\\{file}')
            # file -> no further recursion
            else:
                print(
                    self.output(path, os.path.normpath(path)[self._path_len:],
                                TreeWalk.__generate_md5_checksum(path)))
        except PermissionError:
            print(self.output(path, "NO ACCESS!"))
            return
        except OSError:
            print(self.output(path, "FILE OR DIRECTORY IS BROKEN OR NOT READABLE!"))

    @staticmethod
    def output(file_path, dir_or_relativ_path, md5_hash=""):
        """
        returns a formated String with a file path, the relativ path or "<dir>" if it is a dir
        and a md5 checksum if it is a file.
        :param file_path: file path
        :param dir_or_relativ_path: "<dir>" or relative path from self.path
        :param md5_hash: md5 hash of a file
        :return: a formated String
        """
        basename = os.path.basename(os.path.normpath(file_path))
        return f'{basename}\t{dir_or_relativ_path}\t{md5_hash}'

    @staticmethod
    def __generate_md5_checksum(file_path):
        """
        This method is declared private because it is static and no check is done weather
        the file exists or not. This should ensure that the method is only called within this class.
        :param file_path: path of the file of which a md5 hash-string is generated
        :return: md5 hash-string
        """
        return hashlib.md5(pathlib.Path(file_path).read_bytes()).hexdigest()


if __name__ == "__main__":
    """
    for executing dir walk as a script, if you want to import it than use it like this:
    
        from DirTreeWalk.TreeWalk import TreeWalk
        
        t = TreeWalk(dir_path)
        t.treewalk(dir_path)
    
    (further examples in unit tests)
    """
    # parse arguments
    args = TreeWalk.parser.parse_args()
    if "path" in args:
        t = TreeWalk(args.path[0])
        t.treewalk(args.path[0])
