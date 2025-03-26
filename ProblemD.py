#D. Load Distribution on a Beam: A beam is subjected to a uniform load of
#500 N/m over its entire length of 8 meters. What is the total load acting on the beam?
#Formula: 𝐹 = 𝑤 * 𝐿
#Output message: So, the total load acting on the beam is F (N).

def main():
    
    w = float(input("Enter the uniform load needed on the beam (N/m): "))
    L = float(input("Enter the Length needed of the beam (m): "))
    
    𝐹 = 𝑤 * 𝐿
    
    print(f"So, the total load acting on the beam is {F:.2f} N.")
    
if __name__ == "__main__":
    main()
    