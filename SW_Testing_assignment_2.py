def classify(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
def find_BMI(height, weight):
    # https://www.cdc.gov/growth-chart-training/hcp/using-bmi/calculating-bmi.html#:~:text=With%20the%20metric%20system%2C%20the,multiply%20the%20result%20by%2010%2C000.
    BMI = (weight / (height) ** 2) * 703
    rounded_BMI = round(BMI, 1)
    return rounded_BMI

def check_num(num_val):
    if num_val.isnumeric():
        return True
    else:
        for i in range(len(num_val)):
            temp = num_val[i]
            if not (temp == "1" or temp == "2" or temp == "3" or temp == "4" or temp == "5" or temp == "6" or temp == "7" or temp == "8" or temp == "9" or temp == "0" or temp == "."):
                return False
            num2 = float(num_val)
            num_int = int(num2)
            num3 = num2 - num_int
            if num3 < 0.1:
                return False
            return True

def main():
    print("Welcome to BMI calculator")

    height = input("input height in inches: ")
    while not check_num(height):
        print("ERROR: input a positive number with at most 1 decimal digit")
        height = input("input height in inches: ")

    weight = input("input weight in pounds: ")
    while not check_num(weight):
        print("ERROR: input a positive number with at most 1 decimal digit")
        height = input("input weight in pounds: ")

    BMI = find_BMI(float(height), float(weight))
    category = classify(BMI)
    print(f"BMI calculated is {BMI}.")
    print(f"A person with that BMI is considered {category}.")
    print("Thank you for using BMI Calculator")
    return 0


main()