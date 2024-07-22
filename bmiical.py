def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def main():
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi:.2f}")

if __name__ == "__main__":
    main()
