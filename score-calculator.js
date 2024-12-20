// score-calculator.js
class ScoreCalculator {
    constructor() {
        this.special_patterns = [
            ["4368", 1], ["3685", 1],
            ["12", 1], ["13", 1], ["15", 1], ["17", 1], ["18", 1],
            ["24", 1], ["25", 1], ["27", 1], ["28", 1], ["29", 1],
            ["34", 2], ["36", 1], ["37", 1], ["39", 1],
            ["41", 1], ["43", 1], ["46", 1], ["48", 1], ["49", 1],
            ["52", 1], ["54", 1], ["56", 1], ["57", 1], ["59", 1],
            ["64", 1], ["68", 1], ["69", 1],
            ["73", 1], ["75", 1], ["78", 1], ["79", 1],
            ["82", 1], ["83", 1], ["85", 1],
            ["95", 1], ["97", 1],
        ];
    }

    calculateBaseScore(numberStr) {
        const uniqueDigits = new Set(numberStr.split(''));
        uniqueDigits.delete('0');
        return uniqueDigits.size;
    }

    calculateComboScore(numberStr) {
        let comboScore = 0;
        for (const [pattern, score] of this.special_patterns) {
            if (numberStr.includes(pattern)) {
                comboScore += score;
            }
        }
        return comboScore;
    }

    calculateScore(numberStr) {
        if (numberStr.length > 12) {
            throw new Error("Input sequence must not exceed 12 digits");
        }
        if (!/^\d+$/.test(numberStr)) {
            throw new Error("Input sequence must contain only digits (0-9)");
        }
        const baseScore = this.calculateBaseScore(numberStr);
        const comboScore = this.calculateComboScore(numberStr);
        return baseScore + comboScore;
    }

    // 将分数转换为图标序号（0-22）
    getIconIndex(score) {
        return score % 23;
    }
}

// 用于HTML调用的函数
function calculateIconIndex(inputNumber) {
    try {
        const calculator = new ScoreCalculator();
        const score = calculator.calculateScore(inputNumber.toString());
        return calculator.getIconIndex(score);
    } catch (error) {
        console.error(error);
        return null;
    }
}