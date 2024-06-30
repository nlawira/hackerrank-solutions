if __name__ == '__main__':
    s = input()
    output = {
        "alnum": False,
        "alpha": False,
        "digit": False,
        "lower": False,
        "upper": False
    }
    for i in s:
        if i.isalnum() == True:
            output["alnum"] = True
        if i.isalpha() == True:
            output["alpha"] = True
        if i.isdigit() == True:
            output["digit"] = True
        if i.islower() == True:
            output["lower"] = True
        if i.isupper() == True:
            output["upper"] = True
    for key in output:
        print(output[key])