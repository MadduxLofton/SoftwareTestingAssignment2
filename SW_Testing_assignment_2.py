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
    BMI = (weight / (height) ** 2) * 703
    return BMI

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
