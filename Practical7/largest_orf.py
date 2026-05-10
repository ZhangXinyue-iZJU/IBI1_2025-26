# Practical 7: String and File Operation
# Task 1: Find the longest Open Reading Frame (ORF) in a given sequence

# Define the input mRNA sequence as required
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

def find_longest_orf(sequence):
    """
    Search all possible ORFs starting with AUG and ending with a stop codon.
    Return the longest ORF's length and sequence.
    """
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    orf_list = []

    # Iterate to find all start codon positions
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            # Scan in-frame until a stop codon is found
            for j in range(i, len(sequence) - 2, 3):
                current_codon = sequence[j:j+3]
                if current_codon in stop_codons:
                    orf_seq = sequence[i:j+3]
                    orf_length = len(orf_seq)
                    orf_list.append((orf_length, orf_seq))
                    break  # Stop at first in-frame stop codon

    if not orf_list:
        return None, None

    # Sort to get the longest ORF
    orf_list.sort(reverse=True)
    return orf_list[0]

# Main execution
max_length, max_sequence = find_longest_orf(seq)

print("Longest ORF sequence:", max_sequence)
print("Length of longest ORF (nucleotides):", max_length)