def to_rna(dna_strand):
    conversion = {"C": "G", "G": "C", "T": "A", "A": "U"}
    rna_strand = ""
    for strand in dna_strand:
        rna_strand += conversion[strand]
    return rna_strand
