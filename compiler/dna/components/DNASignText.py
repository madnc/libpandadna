import DNANode
from dna.base.DNAPacker import *


class DNASignText(DNANode.DNANode):
    COMPONENT_CODE = 7

    def __init__(self):
        DNANode.DNANode.__init__(self, '')

        self.letters = ''

    def setLetters(self, letters):
        self.letters = letters

    def traverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.traverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNASignText'  # Override the name for debugging.

        packer.pack('letters', self.letters, STRING)

        return packer
