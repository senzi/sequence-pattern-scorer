# Sequence Pattern Scorer

A number sequence scoring system based on specific patterns. It can be used to develop interesting lottery games. Under the constraint of 12-digit input numbers, the maximum achievable score is 22 points.

## Scoring Rules

The score consists of two parts:
1. Base Score: Number of unique digits (excluding 0)
2. Combo Score: Additional points for matching specific number patterns

For example, the sequence "436834":
- Base Score: 5 points (contains unique digits 4,3,6,8)
- Combo Score:
  - "4368": +1 point
  - "43": +1 point
  - Total Combo Score: 2 points
- Final Score: 7 points

### Pattern Score Table
```python
[
    ("4368", 1),("3685", 1),
    ("12", 1),("13", 1),("15", 1),("17", 1),("18", 1),
    ("24", 1),("25", 1),("27", 1),("28", 1),("29", 1),
    ("34", 2),("36", 1),("37", 1),("39", 1),
    ("41", 1),("43", 1),("46", 1),("48", 1),("49", 1),
    ("52", 1),("54", 1),("56", 1),("57", 1),("59", 1),
    ("64", 1),("68", 1),("69", 1),
    ("73", 1),("75", 1),("78", 1),("79", 1),
    ("82", 1),("83", 1),("85", 1),
    ("95", 1),("97", 1),
]
```

## Usage

```python
from scorer import ScoreCalculator

calculator = ScoreCalculator()

# Calculate score for a single number sequence
number = "436834"
score = calculator.calculate_score(number)
print(f"Total Score: {score}")

# Get detailed scores
base_score = calculator.calculate_base_score(number)
combo_score = calculator.calculate_combo_score(number)
print(f"Base Score: {base_score}")
print(f"Combo Score: {combo_score}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.