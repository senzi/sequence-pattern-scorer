import os
import json
import random
import re
import time

TOTAL_ICONS = 23

# 稀有度配置（按顺序排列）
RARITY_ORDER = ['common', 'rare', 'epic', 'legendary']
RARITY_CONFIG = {
    'common': {
        'count': 8,
        'colors': ['#555555'],
        'animation': 'none',
        'weight': 100
    },
    'rare': {
        'count': 8,
        'colors': ['#5e7ce2', '#789aff'],
        'animation': 'pulse',
        'weight': 50
    },
    'epic': {
        'count': 4,
        'colors': ['#c054ff', '#672f92'],
        'animation': 'glow',
        'weight': 20
    },
    'legendary': {
        'count': 3,
        'colors': ['#ffd700', '#ff5733'],
        'animation': 'rainbow',
        'weight': 5
    }
}

def assign_rarity():
    rarities = []
    weights = []
    for rarity, config in RARITY_CONFIG.items():
        rarities.append(rarity)
        weights.append(config['weight'])
    return random.choices(rarities, weights=weights)[0]

def generate_js_data(seed=None):
    # 如果没有提供种子，使用时间戳生成一个
    if seed is None:
        seed = int(time.time() * 1000) % 100000
    
    # 设置随机种子
    random.seed(seed)
    print(f"\n当前使用的随机种子: {seed}")
    print("(记下这个数字，如果你对结果满意的话)")
    print("-" * 50)

    svg_dir = './svg-icons'
    temp_icon_data = []  # 使用列表暂存数据
    
    # 获取所有SVG文件
    all_svg_files = [f for f in os.listdir(svg_dir) if f.endswith('.svg')]
    print(f"文件夹中共有 {len(all_svg_files)} 个SVG文件")
    
    # 随机选择指定数量的文件
    selected_files = random.sample(all_svg_files, min(TOTAL_ICONS, len(all_svg_files)))
    print(f"随机选择了 {len(selected_files)} 个文件")
    
    # 随机打乱选中的文件
    random.shuffle(selected_files)
    
    # 为每个图标分配稀有度
    rarity_counts = {rarity: 0 for rarity in RARITY_CONFIG.keys()}
    
    for filename in selected_files:
        with open(os.path.join(svg_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
        
        path_match = re.search(r'<path.*?d="([^"]+)"', content)
        if path_match:
            path_data = path_match.group(1)
            
            # 分配稀有度
            while True:
                rarity = assign_rarity()
                if rarity_counts[rarity] < RARITY_CONFIG[rarity]['count']:
                    rarity_counts[rarity] += 1
                    break
            
            temp_icon_data.append({
                'path': path_data,
                'rarity': rarity,
                'colors': RARITY_CONFIG[rarity]['colors'],
                'animation': RARITY_CONFIG[rarity]['animation'],
                'filename': filename
            })

    # 按稀有度排序
    sorted_icon_data = {}
    current_index = 0
    
    # 按RARITY_ORDER中定义的顺序排序
    for rarity in RARITY_ORDER:
        rarity_icons = [icon for icon in temp_icon_data if icon['rarity'] == rarity]
        for icon in rarity_icons:
            sorted_icon_data[current_index] = icon
            current_index += 1

    # 输出稀有度分布统计
    print("\n稀有度分布与索引范围：")
    start_index = 0
    for rarity in RARITY_ORDER:
        count = rarity_counts[rarity]
        end_index = start_index + count - 1
        if count > 0:
            print(f"{rarity}: {count} 个 (索引 {start_index}-{end_index})")
        start_index += count

    # 输出详细的文件分配结果
    print("\n详细分配结果：")
    for idx, data in sorted_icon_data.items():
        print(f"索引 {idx}: {data['filename']} ({data['rarity']})")

    # 生成JavaScript代码
    js_code = f"""
// 自动生成的图标数据
// 索引按稀有度排序：common -> rare -> epic -> legendary
const iconData = {json.dumps(sorted_icon_data, indent=2)};

// 渲染图标的函数
function renderIcon(index) {{
    const data = iconData[index];
    return `<svg viewBox="0 0 512 512">
        <path d="${{data.path}}" class="icon-${{data.rarity}}"/>
    </svg>`;
}}

// 获取稀有度范围
const rarityRanges = {{
    common: [0, {rarity_counts['common']-1}],
    rare: [{rarity_counts['common']}, {rarity_counts['common']+rarity_counts['rare']-1}],
    epic: [{rarity_counts['common']+rarity_counts['rare']}, {rarity_counts['common']+rarity_counts['rare']+rarity_counts['epic']-1}],
    legendary: [{rarity_counts['common']+rarity_counts['rare']+rarity_counts['epic']}, {sum(rarity_counts.values())-1}]
}};
"""
    
    # 保存JS文件
    with open('icons-data.js', 'w', encoding='utf-8') as f:
        f.write(js_code)
    
    print(f"\n已生成 icons-data.js")

if __name__ == '__main__':
    # 可以手动指定种子
    generate_js_data(79945)
    
    # 或者让程序随机生成种子
    # generate_js_data()