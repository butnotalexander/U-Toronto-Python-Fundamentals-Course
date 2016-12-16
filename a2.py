def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    """num = 0
    for char in dna:
    	if char in nucleotide:
    		num = num + 1
    return num
    does not work for instances of 'GG' or 'CC'"""
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1
    
  
'no str methods from here on out, can use built-in functions and string operations'

def is_valid_sequence(dna):
	""" (str) -> bool
	
	Return True if and only if dna is a valid DNA sequence (containing only 'A', 'T', 'C'
	or 'G'). A string is not valid if it contains lowercase letters.
	
	>>> is_valid_sequence('ATCCGGTAG')
	True
	>>> is_valid_sequence('ATCCIPOK')
	False
	
	"""
	valid = True
	valid_string = 'ATCG'
	
	for char in dna:
		if char not in valid_string:
			return False
	
	return valid
	
	
def insert_sequence(dna1, dna2, index):
	""" (str, str, int) -> str
	
	Return the DNA sequence obtained by inserting the second DNA sequence into the first
	DNA sequence at the given index (assume the index is valid).
	 
	>>> insert_sequence('CCGG', 'AT', 2)
	'CCATGG'
	>>> insert_sequence('CCTG', 'GCG', 1)
	'CGCGCTG'
	
	"""
	return dna1[:index] + dna2 + dna1[index:]
	
	
def get_complement(nuc):
	""" (str) -> str
	
	Return the given nucleotide's complement nucleotide, a.k.a. the nucleotide that the
	first can be bonded with.
	
	>>> get_complement('A')
	'T'
	>>> get_complement('C')
	'G'
	
	"""
	if nuc == 'A':
		return 'T'
	elif nuc == 'T':
		return 'A'
	elif nuc == 'C':
		return 'G'
	elif nuc == 'G':
		return 'C'
	
	
def get_complementary_sequence(dna):
	""" (str) -> str
	
	Returns the complementary DNA sequence of the given DNA sequence.
	
	>>> get_complementary_sequence('AT')
	'TA'
	>>> get_complementary_sequence('CGTA')
	'GCAT'
	
	"""
	nuc = ''
	
	for char in dna:
		nuc = nuc + get_complement(char)
		
	return nuc
