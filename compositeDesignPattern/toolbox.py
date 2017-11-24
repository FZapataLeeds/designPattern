class SpecialDic(dict):
    def __missing__(self, key):
        return 0


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


class LookUpBOM:
    def lookupbom(BOM):
        bom = Dictlist()
        with open(str(BOM)) as f:
            for line in f:
                (topLevel, subPart, val) = line.split()
                bom[str(topLevel)] = {str(subPart): int(val)}
        return bom
