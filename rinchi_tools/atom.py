"""
RInChI Object Orientated Atom Class Module

This module contains the Atom class and associated functions

    B. Hammond 2014
    D. Hampshire 2017 - Significant restructuring of the class to gain more consistent and less verbose code.
"""


class Atom:
    """
    A class containing a brief description of an atom, for use as nodes in a graph describing a molecule
    """
    def __init__(self, index=None):
        self.index = index
        self.bonds = []
        self.protons = 0
        self.mobile_protons = 0
        self.element = None
        self.isotope = None

    def valence(self):
        """
        Get the valence as determined by counting the number of bonds.

        Returns:
            Number of bonds

        """
        if self.mobile_protons == 0:
            return len(self.bonds) + self.protons
        else:
            return None

    def hybridisation(self):
        """
        Gets the atom hybridisation.  Only defined for C atoms but still useful

        Returns:
            None or a string signalling the hybridisation e.g.  "sp2"
        """
        if self.valence():
            if self.element == "C":
                if self.valence() == 4:
                    return "sp3"
                elif self.valence() == 3:
                    return "sp2"
                elif self.valence() == 2:
                    return "sp"

    def get_attached_edges(self):
        """

        Returns:

        """
        attached_edges = [tuple(sorted((self.index, bond))) for bond in self.bonds]
        return attached_edges
