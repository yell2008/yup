import calc
print('File imported!')
assert calc.simple_calculator("2+2") == 4, "correct addition: should be 4"
assert calc.simple_calculator("2-2") == 0, "correct subtraction: should be 0"
assert calc.simple_calculator("2/2") == 1, "correct division: should be 1"
assert calc.simple_calculator("2*2") == 4, "correct multiplication: should be 4"
assert calc.simple_calculator("8//2") == 4, "correct DIV: should be 4"
assert calc.simple_calculator("2%2") == 0, "correct MOD: should be 0"
\
"should support boolean algebra (priorities): answer is 0"
print('all tests passed!')
