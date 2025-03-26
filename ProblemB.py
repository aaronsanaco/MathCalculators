#B. Material Strength Calculation for Steel: You are tasked with determining
#the total stress on a steel beam subjected to a load. If the force applied to
#the beam is 10,000 N and the cross-sectional area of the beam is 50 mm²,
#calculate the stress on the beam.
#Formula: 𝜎𝑦 = 𝐹𝑦 / 𝐴
#Output message: So, the stress on the beam is σ Pa

def main():
    
    Fy = float(input("Enter the Force needed on the beam(N): "))
    A = float(input("Enter the Area needed (m²): "))
    
    𝜎𝑦 = 𝐹𝑦 / 𝐴
    
    print(f"So, the stress on the beam is {𝜎𝑦:.2f} Pa.")
    
if __name__ == "__main__":
    main()
    