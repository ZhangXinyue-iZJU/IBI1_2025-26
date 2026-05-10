def calculate_protein_mass(amino_acid_sequence):
    """
    Calculate the total monoisotopic mass of a protein sequence in amu.
    
    Args:
        amino_acid_sequence (str): A string of single-letter amino acid symbols.
        
    Returns:
        float: Total mass of the protein in atomic mass units (amu).
        
    Raises:
        ValueError: If any character in the sequence is not a valid amino acid symbol.
    """
    # Define the monoisotopic mass of each amino acid residue
    amino_acid_masses = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
        'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
        'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
        'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }
    
    # Initialize total mass to 0
    total_mass = 0.0
    
    # Iterate through each amino acid in the sequence
    for aa in amino_acid_sequence:
        # Convert to uppercase to handle lowercase inputs
        aa_upper = aa.upper()
        
        # Check if the amino acid is valid
        if aa_upper not in amino_acid_masses:
            raise ValueError(f"Invalid amino acid symbol: '{aa}'. Please check your sequence.")
        
        # Add the mass of the current amino acid
        total_mass += amino_acid_masses[aa_upper]
    
    # Return rounded total mass
    return round(total_mass, 2)


# Example function call
if __name__ == "__main__":
    # Example valid sequence
    example_sequence = "MALW"
    mass = calculate_protein_mass(example_sequence)
    print(f"The mass of the protein sequence '{example_sequence}' is: {mass} amu")