# Link: https://rosalind.info/problems/ini/
# Date solved: 2026-10-23
"""
Introduction to the Bioinformatics Armory

Problem
* Given: A DNA string s of length at most 1000 bp.
* Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Approach
* Use pythons built-in string .count() function to count each nucleotide in a single pass.

Complexity Analysis
* Time Complexity: O(n), n being length of DNA string
* Space Complexity: O(1), memory usage is constant
"""

def count_nucleotides(dna_string: str) -> str:
    """Counts occurances of A, C, G, T in given DNA string."""
    a_count = dna_string.count("A")
    c_count = dna_string.count("C")
    g_count = dna_string.count("G")
    t_count = dna_string.count("T")

    return f"{a_count} {c_count} {g_count} {t_count}"

if __name__ == "__main__":
    # Test with Rosalind Sample Dataset
    sample_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    print(count_nucleotides(sample_input)) # Expected Output: 20 12 17 21