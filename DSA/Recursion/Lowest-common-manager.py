"""Lowest Common Manager - You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that isn't anybody else's direct report), and the other two inputs are reports in the organizational chart. The two reports are guaranteed to be distinct. Write a function that returns the lowest common manager to the two reports."""
# O(N) T | O(d) S
#numIP = numberOfImportantReports
#lcm = lowestCommonManager


def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lcm


def getOrgInfo(manager, reportOne, reportTwo):
    numIP = 0
    for dirRep in manager.directReports:
        orgInfo = getOrgInfo(dirRep, reportOne, reportTwo)
        if orgInfo.lcm is not None:
            return orgInfo
        numIP += orgInfo.numIP
    if manager == reportOne or manager == reportTwo:
        numIP += 1
    lcm = manager if numIP == 2 else None
    return OrgInfo(lcm, numIP)


class OrgInfo:
    def __init__(self, lcm, numIP):
        self.lcm = lcm
        self.numIP = numIP

# This is an input class. Do not edit.


class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
