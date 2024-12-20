#!/bin/bash

# 创建dist目录
rm -rf dist
mkdir dist

# 复制静态文件
cp index.html dist/
cp style.css dist/
cp LICENSE dist/
cp README.md dist/

# 确保使用正确的 npx 路径并添加错误处理
if ! npx terser icons-data.js -o dist/icons-data.js \
    -c passes=3 \
    -m toplevel=true,reserved=['renderIcon','iconData'] \
    --compress dead_code=true,drop_debugger=true \
    --source-map none; then
    echo "Error processing icons-data.js"
    exit 1
fi

if ! npx terser score-calculator.js -o dist/score-calculator.js \
    -c passes=3 \
    -m toplevel=true,reserved=['calculateIconIndex'] \
    --compress dead_code=true,drop_debugger=true \
    --source-map none; then
    echo "Error processing score-calculator.js"
    exit 1
fi

echo "Build completed successfully!"