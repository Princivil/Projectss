
#round your conversion to two decimal places
print('How many kilometers did you drive today?')
kms = input()
miles = round(float(kms)/1.60934,2)
print(f"Okay, so you drove {kms} which is actually {miles} miles.")
