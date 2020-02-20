import re


class Dna:
    def __init__(self, seq):
        pattern = re.compile(r'[ATGCNatgcn]*')
        if len(seq) % 3 != 0:
            raise ValueError('The number of nucleotides must be a multiple of three')
        elif not pattern.match(seq):
            raise ValueError('DNA can only contain nucleotides A, T, G, C or N')
        else:
            self.seq = seq

    def gc_content(self):
        gc = 0
        for nucl in self.seq:
            if nucl in ('C', 'G', 'c', 'g'):
                gc += 1
        return gc / len(self.seq)

    def reverse_complement(self):
        reverse = []
        for nucl in self.seq:
            if nucl in ('A', 'a'):
                reverse.append('T')
            elif nucl in ('T', 't'):
                reverse.append('A')
            elif nucl in ('C', 'c'):
                reverse.append('G')
            elif nucl in ('G', 'g'):
                reverse.append('C')
            else:
                reverse.append('N')
        reverse.reverse()
        return ''.join(reverse)

    def transcribe(self):
        new_rna = []
        for nucl in self.seq:
            if nucl in ('A', 'a'):
                new_rna.append('U')
            elif nucl in ('T', 't'):
                new_rna.append('A')
            elif nucl in ('C', 'c'):
                new_rna.append('G')
            elif nucl in ('G', 'g'):
                new_rna.append('C')
            else:
                new_rna.append('N')
        return ''.join(new_rna)


class Rna:
    def __init__(self, seq):
        pattern = re.compile(r'[AUGCNaugcn]*')
        if len(seq) % 3 != 0:
            raise ValueError('The number of nucleotides must be a multiple of three')
        elif not pattern.match(seq):
            raise ValueError('RNA can only contain nucleotides A, U, G, C or N')
        else:
            self.seq = seq

    def gc_content(self):
        gc = 0
        for nucl in self.seq:
            if nucl in ('C', 'G', 'c', 'g'):
                gc += 1
        return gc / len(self.seq)

    def reverse_complement(self):
        reverse = []
        for nucl in self.seq:
            if nucl in ('A', 'a'):
                reverse.append('U')
            elif nucl in ('U', 'u'):
                reverse.append('A')
            elif nucl in ('C', 'c'):
                reverse.append('G')
            elif nucl in ('G', 'g'):
                reverse.append('C')
            else:
                reverse.append('N')
        reverse.reverse()
        return ''.join(reverse)


a = Dna('AAAcCc')
a.seq
a.gc_content()
a.reverse_complement()
a.transcribe()

s = [1, 2, 3, 4, 5]

s.reverse()

for i in a:
    print('ok')
