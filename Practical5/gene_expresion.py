# 1. Create the dictionary with initial data
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print(gene_expression)

# 2. Add 'MYC' to the dictionary
gene_expression["MYC"] = 11.6
print(gene_expression)

# 3. Produce a well-labelled bar chart
import matplotlib.pyplot as plt
genes = list(gene_expression.keys())
values = list(gene_expression.values())

plt.figure(figsize=(10, 6))
plt.bar(genes, values, color='skyblue', edgecolor='black')
plt.title("Gene Expression Levels", fontsize=14)
plt.xlabel("Gene Name", fontsize=12)
plt.ylabel("Expression Value", fontsize=12)
plt.xticks(rotation=45) # Rotate labels if they are too long
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 4. Check expression for a specific gene
gene_of_interest = "BRCA1" 
if gene_of_interest in gene_expression:
    print(f"Expression value for {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"Error: The gene '{gene_of_interest}' is not present in the dataset.")

# 5. Calculate average expression level
total_expression = sum(gene_expression.values())
num_genes = len(gene_expression)
average_expression = total_expression / num_genes

print(f"Average gene expression level: {average_expression:.2f}")
