def split_before_each_uppercases(formula):
    parts = []
    current_part = ""
    
    for i, char in enumerate(formula):
        if i > 0 and char.isupper():
            parts.append(current_part)
            current_part = char
        else:
            current_part += char
            
    if current_part:
        parts.append(current_part)
        
    return parts
# Replace the `pass` with your code


def split_at_first_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            prefix = formula[:i]     
            suffix = formula[i:]    
            return (prefix, suffix)  
            
    return (formula, "")
