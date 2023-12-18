# PYTHON Exception using FINALLY Example
try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")