def length_converter(value: float, from_unit: str, to_unit: str) -> float:
    length_units = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_converter(value: float, from_unit: str, to_unit: str) -> float:
    weight_units = {
        "kilogram": 1.0,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495,
    }
    return value * weight_units[from_unit] / weight_units[to_unit]
