from src.panel import sorted_copy, sort_variants, Variant
from src.lookup import kmer_counts, safe_expression

def test_sorted_copy_leaves_original_unchanged():
    """Test 1: sorted_copy leaves the original list unchanged."""
    original_list = [5, 2, 8, 1]
    # Make a manual copy to compare against later
    exact_copy = original_list.copy()
    
    result = sorted_copy(original_list)
    
    assert result == [1, 2, 5, 8]
    assert original_list == exact_copy  # Proves the original wasn't mutated


def test_chromosome_order():
    """Test 2: Chromosome order including X and M."""
    variants = [
        Variant("M", 10, "A", "C"),
        Variant("X", 5, "T", "G"),
        Variant("2", 15, "C", "T"),
        Variant("1", 20, "G", "A")
    ]
    
    result = sort_variants(variants)
    
    # 1 and 2 come first, then X, and M is always last
    assert result[0].chrom == "1"
    assert result[1].chrom == "2"
    assert result[2].chrom == "X"
    assert result[3].chrom == "M"


def test_kmer_counts_edge_cases():
    """Test 3: k larger than sequence and an empty string for kmer_counts."""
    # If k is larger than the sequence length, it should safely return an empty dict
    assert kmer_counts("ATCG", k=5) == {}
    
    # If the sequence is empty, it should also return an empty dict
    assert kmer_counts("", k=3) == {}


def test_safe_expression_missing_and_zero():
    """Test 4: Missing gene gives None and a real 0.0 stays 0.0."""
    expression_data = {"BRCA1": 5.5, "TP53": 0.0}
    
    # A missing gene should return None
    assert safe_expression(expression_data, "PTEN") is None
    
    # A gene that genuinely has an expression of 0.0 should return exactly 0.0
    assert safe_expression(expression_data, "TP53") == 0.0