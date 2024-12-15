#looging IMP
import logging

# Configure logging
logging.basicConfig(filename='F:\\Avd\\Python\\programs\\mylog.txt', level=logging.ERROR)

try:
    # Input and calculation
    a, b = [int(i) for i in input("Enter two numbers separated by a comma: ").split(',')]
    c = a / b
    print(f'Division result: {c}')
except Exception as ee:
    # Log the exception
    logging.exception("An error occurred:")