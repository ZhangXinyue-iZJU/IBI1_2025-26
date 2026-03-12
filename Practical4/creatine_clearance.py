# Pseudocode for Creatinine Clearance Calculator
# 1. Define variables: age, weight, gender, Cr
# 2. Check if age >= 100 -> Print Error
# 3. Check if weight <= 20 OR weight >= 80 -> Print Error
# 4. Check if Cr <= 0 OR Cr >= 100 -> Print Error
# 5. Check if gender is not 'Male' or 'Female'
# 6. (All inputs valid): Calculate CrCl


### store values of a person ###
age = 18   # in years
weight = 63.5   # in kg
gender = "Female"
Cr = 78   # Creatine concentration in µmol/l

### Calculate CrCl ###
# Initialize a flag to track if any error occurs
has_error = False

# Check 1: Age
if age >= 100:
    print("Error: Age must be under 100.")
    has_error = True
# Check 2: Weight
if weight <= 20 or weight >= 80:
    print("Error: Weight must be over 20kg and under 80kg.")
    has_error = True
# Check 3: Creatinine (Cr)
if Cr <= 0 or Cr >= 100:
    print("Error: Creatinine concentration must be > 0 and < 100 µmol/l.")
    has_error = True
# Check 4: Gender
if gender.lower() not in ["male", "female"]:
    print("Error: Gender must be 'Male' or 'Female'.")
    has_error = True

# Calculate only if NO errors occurred
if not has_error:
    # Base calculation
    base_val = ((140 - age) * weight) / (72 * Cr)
    if gender.lower() == "female":
        CrCl = base_val * 0.85
    else:
        CrCl = base_val
    print(f"Calculated CrCl: {CrCl:.2f} mL/min")
