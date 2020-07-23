# Sort by Extension

from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    """ Sorts list by the file extension """
    def sort_fnc(a):
        b = str(a)
        extension = b[b.rindex('.')+1:]
        name = b[:b.rindex('.')]
        if not name or len(extension) < 1 or len(extension) > 3:
            return '0' + name + extension
        else:
            return extension + name
    return sorted(files, key=sort_fnc)


# Running some tests..
print(sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad'])
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad'])
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad'])
print(sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad'])
print(sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad'])
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc'])
print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc'])
