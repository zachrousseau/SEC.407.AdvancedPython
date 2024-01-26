def meters_to_feet(meters):
    
    feet = round(float(meters) / 0.3048, 2)
    return str(feet) + " feet"

def feet_to_meters(feet):
    
    meters  = round(float(feet) * 0.3048, 2)
    return str(meters) + " meters"
