import pickle as p
import numpy as np

model = p.load(open("./model.pkl", "rb"))

iq = float(input("Enter the IQ : "))
cgpa = float(input("Enter the CGPA : "))
final = [np.array([cgpa,iq])]
prediction = model.predict(final)
if prediction==1:
    print("You are eligible for a placement !")
elif prediction==0:
    print("You are not eligible for placement !")