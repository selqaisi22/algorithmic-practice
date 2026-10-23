# Link: https://rosalind.info/problems/gbk/
# Date solved: 2026-10-23
"""
GenBank Introduction

Problem
* Given: A genus name, followed by two dates in YYYY/M/D format.
* Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

Approach
* Utilize biopythons Bio.Entrez.esearch() function to query NCBI nucleotide db using organism search tags & publication date filters. 

Complexity Analysis
* Time Complexity: O(1), running locally search 
* Space Complexity: O(1), constant memory allocation of results
"""

from Bio import Entrez

def count_genbank_entries(genus: str, start_date: str, end_date: str) -> str:
    """Queries NCBI nucleotide db for GenBank entries matching organism & date range."""

    # setting email required by NCBI 
    Entrez.email = "elqaissa@gmail.com"

    # create query term format
    search_term = f'"{genus}"[Organism] AND ("{start_date}"[Publication Date] : "{end_date}"[Publication Date])'

    # run query in db 
    handle = Entrez.esearch(db="nucleotide", term=search_term)
    record = Entrez.read(handle)
    handle.close()

    # return entry count as str
    return record["Count"]



if __name__ == "__main__":
    # Test with Rosalind Sample Dataset
    sample_genus = "Anthoxanthum"
    sample_start = "2003/7/25"
    sample_end = "2005/12/27"

    print(count_genbank_entries(sample_genus, sample_start, sample_end)) # Expected Output: 7