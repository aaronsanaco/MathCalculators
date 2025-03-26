#A. Cement Slurry Dilution: You have a 10 L batch of cement slurry with a
#cement concentration of 200 g/L. How much of this slurry would you need to
#dilute to prepare 1 L of slurry with a concentration of 50 g/L?
#Formula: 𝑉1 = 𝐶2𝑉2/𝐶1
#Output message: So, you need 𝑉 liters of the original slurry.

def main():
    V2 = float(input("Enter the Final Volume needed (L): "))
    C1 = float(input("Enter the Initial Concentration needed (g/L): "))
    C2 = float(input("Enter the Final Concentration needed (g/L): "))
    
    𝑉1 = (𝐶2 * 𝑉2) / 𝐶1
    
    print(f"Therefore, the Initial Volume would need {V1:.2f} liters of the original slurry.")
    
if __name__ == "__main__":
    main()
    