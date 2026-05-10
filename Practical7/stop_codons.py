# Practical 7: String and File Operation
# Task 2: Detect in-frame stop codons in yeast cDNA FASTA file

def read_fasta(filename):
    """
    Read FASTA file and return a list of (gene_name, full_sequence) pairs.
    Handle multi-line sequences correctly.
    """
    genes = []
    current_name = ''
    current_seq = ''

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                # Save previous gene if exists
                if current_name:
                    genes.append((current_name, current_seq))
                # Extract gene name (first word after >)
                current_name = line[1:].split()[0]
                current_seq = ''
            else:
                # Append sequence lines
                current_seq += line
        # Add the last gene
        if current_name:
            genes.append((current_name, current_seq))
    return genes

def has_in_frame_stop(seq):
    """
    Check for in-frame stop codons (TAA/TAG/TGA) following an ATG start.
    Return sorted list of unique stop codons found.
    """
    stop_codons = ['TAA', 'TAG', 'TGA']
    found_stops = set()

    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            # Scan in-frame codons
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break  # One stop per ORF is enough
    return sorted(list(found_stops))

def main():
    # Input and output file names
    input_fasta = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_fasta = 'stop_genes.fa'

    # Read all genes
    all_genes = read_fasta(input_fasta)

    # Write filtered genes to output FASTA
    with open(output_fasta, 'w') as out_file:
        for gene_name, gene_seq in all_genes:
            stops = has_in_frame_stop(gene_seq)
            if stops:
                # Write header: gene name + stop codons
                header = f'>{gene_name} {",".join(stops)}'
                out_file.write(header + '\n')
                # Write sequence in lines of 80 bp
                for k in range(0, len(gene_seq), 80):
                    out_file.write(gene_seq[k:k+80] + '\n')

if __name__ == '__main__':
    main()