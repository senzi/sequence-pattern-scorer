class ScoreCalculator:
    def __init__(self):
        # 特殊组合得分表
        self.special_patterns = [
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

    def calculate_base_score(self, number_str):
        unique_digits = set(number_str)
        unique_digits.discard("0")
        return len(unique_digits)

    def calculate_combo_score(self, number_str):
        combo_score = 0
        for pattern, score in self.special_patterns:
            if number_str.find(pattern) != -1: 
                combo_score += score
        return combo_score

    def calculate_score(self, number_str):
        number_str = str(number_str)
        if len(number_str) > 12:
            raise ValueError("Input sequence must not exceed 12 digits") 
        if not number_str.isdigit():
            raise ValueError("Input sequence must contain only digits (0-9)")
        base_score = self.calculate_base_score(number_str)
        combo_score = self.calculate_combo_score(number_str)
        return base_score + combo_score

if __name__ == '__main__':
    calculator = ScoreCalculator()
    
    # 测试几个数字
    test_numbers = [
        "436834",     # 简单例子
        "368543",     # 包含多个patterns
        "123456789",  # 所有不同数字
        "343436",     # 包含2分的"34"
    ]
    
    for num in test_numbers:
        print(f"\n测试数字: {num}")
        base = calculator.calculate_base_score(num)
        combo = calculator.calculate_combo_score(num)
        total = calculator.calculate_score(num)
        print(f"基础分: {base}")
        print(f"组合分: {combo}")
        print(f"总分: {total}")
        print("匹配的patterns:")
        for pattern, score in calculator.special_patterns:
            if num.find(pattern) != -1:
                print(f"- {pattern}: +{score}分")