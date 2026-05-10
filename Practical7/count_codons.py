# Practical 7: String and File Operation
# Task 3: Codon frequency counting and pie chart generation

import matplotlib.pyplot as plt
from collections import defaultdict

def read_fasta(filename):
    """Read FASTA and return list of (gene_name, full_sequence) pairs."""
    genes = []
    name = ''
    seq = ''
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if name:
                    genes.append((name, seq))
                name = line[1:].split()[0]
                seq = ''
            else:
                seq += line
        if name:
            genes.append((name, seq))
    return genes

def get_longest_orf_codons(seq, target_stop):
    """
    Extract codons from the LONGEST ORF ending with the given target stop codon.
    Only in-frame (from ATG) codons before stop are returned.
    """
    stop_codons = ['TAA', 'TAG', 'TGA']
    best_codon_list = []

    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            current_codons = []
            matched_stop = None
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    matched_stop = codon
                    break
                current_codons.append(codon)
            # Keep the longest ORF for the target stop codon
            if matched_stop == target_stop:
                if len(current_codons) > len(best_codon_list):
                    best_codon_list = current_codons
    return best_codon_list

def main():
    # Get valid stop codon input from user
    target = input('Enter stop codon (TAA/TAG/TGA): ').strip().upper()
    if target not in ['TAA', 'TAG', 'TGA']:
        print('Invalid stop codon! Please enter TAA, TAG, or TGA.')
        return

    # Read cDNA file
    fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    gene_list = read_fasta(fasta_file)

    # Count codon frequencies
    codon_count = defaultdict(int)
    for gene_name, sequence in gene_list:
        codons = get_longest_orf_codons(sequence, target)
        for c in codons:
            codon_count[c] += 1

    # Print results
    print(f'\nCodon frequency upstream of {target}:')
    for codon, count in sorted(codon_count.items()):
        print(f'{codon}: {count}')

    # Generate and save pie chart (not displayed on screen)
    plt.switch_backend('Agg')
    labels = list(codon_count.keys())
    values = list(codon_count.values())

    plt.figure(figsize=(10, 7))
    plt.pie(values, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 8})
    plt.title(f'Codon Distribution for Stop Codon: {target}', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'codon_pie_{target}.png', dpi=300, bbox_inches='tight')
    print(f'\nPie chart saved as: codon_pie_{target}.png')

if __name__ == '__main__':
    main()