"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
    result = []
    for i in genes:
        if i in priority:
            result.append(i)
    return result


def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    return sorted(items)


def _chrom_key(chrom: str) -> tuple:
    """eliminate chr """
    chrom = chrom.replace("chr", "") 
    
    """X=23, Y=24, M=25"""
    if chrom == "X":
        rank = 23
    elif chrom == "Y":
        rank = 24
    elif chrom == "M":
        rank = 25
    else:
        """change string to int"""
        rank = int(chrom)
           
    return (rank,"")

def sort_variants(variants: list[Variant]) -> list[Variant]:
    """Sort by chromosome (1-22, X, Y, M) and then by position."""
    """_chrom_key(v.chrom): calls function to convert the text chromosome
    v.pos: This grabs the base position of the variant"""
    def helper(v: Variant) -> tuple:
        return (_chrom_key(v.chrom), v.pos)
        
    return sorted(variants, key=helper)
