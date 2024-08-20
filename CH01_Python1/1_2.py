h, w= map(float, input("Enter your High and Weight : ").split())
BMI = w/(h*h)
if BMI<18.5:
    print("Less Weight")
if 18.5<=BMI<23:
    print("Normal Weight")
if 23<=BMI<25:
    print("More than Normal Weight")
if 25<=BMI<30:
    print("Getting Fat")
if BMI >= 30:
    print("Fat")