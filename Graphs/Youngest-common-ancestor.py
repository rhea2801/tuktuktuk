"""Youngest Common Ancestor - You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree (i.e., the only instance that has no ancestor--its ancestor property points to None / null ), and the other two inputs are descendants in the ancestral tree. Write a function that returns the youngest common ancestor to the two descendants.
Note that a descendant is considered its own ancestor. So in the simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.
"""

# O(d) T | O(1)S


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depOne = getDescDep(descendantOne, topAncestor)
    depTwo = getDescDep(descendantTwo, topAncestor)
       if depOne > depTwo:
            return youngCommon(descendantOne, descendantTwo, depOne-depTwo)
        else:
            return youngCommon(descendantTwo, descendantOne, depTwo-depOne)


def getDescDep(desc, top):
    depth = 1
    while desc != top:
        depth += 1
        desc = desc.ancestor
    return depth

def youngCommon(lowerDesc, higherDesc, diff):
    while diff > 0:
        lowDesc = lowerDesc.ancestor
        diff -= 1

    while higherDesc != lowerDesc:
        higherDesc = higherDesc.ancestor
        lowerDesc = lowerDesc.ancestor
    return lowerDesc
