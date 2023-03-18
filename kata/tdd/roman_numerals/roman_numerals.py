'''
| decimal | roman |
|---------|-------|
|    1000 |   M   |
|     500 |   D   |
|     100 |   C   |
|      50 |   L   |
|      10 |   X   |
|       5 |   V   |
|       1 |   I   |


Subtractive notation:

| decimal | roman |
|---------|-------|
|     900 |  CM   |
|     400 |  CD   |
|      90 |  XC   |
|      40 |  XL   |
|       4 |  IV   |



Test Cases:

- one - 1
- two - 2
- three - 3
- four - 4

Execute Tests:

```bash
python -m unittest -k roman_numerals
```

'''

def decimal_to_roman(num):
    roman = ''
    number_map = (
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    )
    for arabic_num, roman_num in number_map:
        while num >= arabic_num:
            roman += roman_num
            num -= arabic_num
    return roman
