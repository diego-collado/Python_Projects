# Archivo calculator_logic.py

# FUNCTIONS --------------------------------------------------------
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result, None
    except SyntaxError:
        return None, "Syntax Error"
    except ZeroDivisionError:
        return None, "Cannot divide by zero"
    except Exception as e:
        return None, str(e)