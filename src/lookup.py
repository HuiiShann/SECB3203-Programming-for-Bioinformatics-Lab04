"""Lab 4 - dictionaries and sets for biological lookup."""
import itertools
from collections import Counter

_BASES = "TCAG"
_AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

# Build the 64-codon dictionary programmatically
CODON_TABLE: dict[str, str] = {
    "".join(codon): aa
    for codon, aa in zip(itertools.product(_BASES, repeat=3), _AMINO)
}

def count_bases(seq: str) -> dict[str, int]:
    """Count each character in seq (upper-cased), sorted by key."""
    return dict(sorted(Counter(seq.upper()).items()))


def kmer_counts(seq: str, k: int) -> dict[str, int]:
    """Count overlapping k-mers, sorted by key. ValueError if k < 1."""
    if k < 1:
        raise ValueError("k is less than 1!")
    seq = seq.upper()
    counts = Counter()
    
    """Loop & Slicing in 3 """
    for i in range(len(seq) - k + 1):
        kmer = seq[i : i + k]
        counts[kmer] += 1
        
    return dict(sorted(counts.items()))


def shared_genes(panel: set[str], detected: set[str]) -> set[str]:
    """Genes that are both on the panel and detected. & = intercept"""
    return set(panel) & set(detected)


def safe_expression(expression: dict[str, float], gene: str) -> float | None:
    """Return the expression value, or None when the gene is missing."""
    # .get() returns None by default if the key is missing!
    return expression.get(gene)


def translate(dna: str) -> str:
    """Translate DNA to a protein string ('*' marks a stop codon).

    Raises:
        ValueError: if the length is not a multiple of 3 or a codon is invalid.
    """
    # 1. Check for valid length
    if len(dna) % 3 != 0:
        raise ValueError("DNA length must be a multiple of 3.")
        
    dna = dna.upper()
    protein = []
    
    """range(start, stop, step). By setting the step to 3, we tell Python to jump 3 letters at a time instead of 1, which perfectly slices out the 3-letter codons."""
    # 2. Slice perfect 3-letter jumps
    for i in range(0, len(dna), 3):
        codon = dna[i : i + 3]
        
        # 3. Check for invalid codons (like 'NNN' or letters other than TCAG)
        if codon not in CODON_TABLE:
            raise ValueError(f"Invalid codon detected: {codon}")
            
        protein.append(CODON_TABLE[codon])
        
    return "".join(protein)
