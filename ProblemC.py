# C. Concrete Volume Calculation: You are constructing a sidewalk and
# need to pour concrete. The sidewalk is 20 meters long, 1.5 meters wide, and
# 0.2 meters deep. How many cubic meters of concrete are needed?
# Formula: 𝑉 = 𝐿 * 𝑊 * 𝐷
# Output message: So, you need V cubic meters of concrete.

def main():
    
    L = float(input("Enter the Length needed(m): "))
    W = float(input("Enter the Width needed (m): "))
    D = float(input("Enter the Diameter needed (m): "))
    
    𝑉 = 𝐿 * 𝑊 * 𝐷
    
    print(f"So, you need {V:.2f} cubic meters of concrete.")
    
if __name__ == "__main__":
    main()
    