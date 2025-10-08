# 边界文件检查工具 (Boundary Check Tool)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/HuangWuwutelling/boundary-check-tool.svg)](https://github.com/HuangWuwutelling/boundary-check-tool/issues)
[![GitHub Stars](https://img.shields.io/github/stars/HuangWuwutelling/boundary-check-tool.svg)](https://github.com/HuangWuwutelling/boundary-check-tool/stargazers)

🔍 **专业的地块边界文件规范性检查工具**

一个用于批量检查地块边界文件(SHP格式)规范性的Python自动化工具，支持文件完整性检查、字段规范性验证、空间位置校验，并生成详细的检查报告和可视化地图。

## ✨ 主要特性

- 🚀 **批量处理**: 支持同时检查数百个ZIP格式的边界文件
- 🔍 **智能检测**: 自动识别文件编码(GBK/UTF-8)和坐标系类型
- 📊 **全面检查**: 文件完整性、字段规范性、空间位置一站式验证
- 🗺️ **可视化**: 生成交互式HTML地图展示检查结果
- 📈 **详细报告**: Excel格式的详细检查报告和统计信息
- 🔧 **易于使用**: 图形界面操作，支持EXE独立运行

## 🎯 适用场景

- 土地规划部门的边界文件质量检查
- GIS数据入库前的规范性验证  
- 地理数据质量控制和审核
- 批量处理大量地块边界数据

## 🚀 快速开始

### 方法一：下载EXE文件（推荐）

1. 前往 [Releases](https://github.com/HuangWuwutelling/boundary-check-tool/releases) 页面
2. 下载最新版本的 `边界文件检查工具.exe`
3. 准备数据文件（见[文件格式要求](#文件格式要求)）
4. 双击运行exe文件

### 方法二：Python环境运行

#### 环境要求
- Python 3.7+
- 推荐使用Conda管理环境

#### 安装依赖
```bash
# 使用Conda（推荐）
conda create -n boundary_check python=3.9
conda activate boundary_check
conda install -c conda-forge geopandas pandas folium openpyxl chardet

# 或使用pip
pip install -r requirements.txt
```

#### 运行程序
```bash
python src/boundary_check_tool.py
```

## 📋 文件格式要求

### 1. Excel文件（地块信息.xlsx）

必须包含以下列：

| 列名 | 数据类型 | 说明 | 示例 |
|------|----------|------|------|
| 地块编码 | 文本 | 13位数字编码 | 4420013990012 |
| 经度 | 数值 | 地块中心点经度 | 113.2644 |
| 纬度 | 数值 | 地块中心点纬度 | 23.1291 |

### 2. ZIP文件命名规范

- 格式：`{前缀}{13位地块编码}.zip`
- 示例：`初步调查4420013990012.zip`

### 3. SHP文件组要求

每个ZIP内必须包含：
- ✅ `.shp` - 主文件（几何数据）
- ✅ `.shx` - 索引文件  
- ✅ `.dbf` - 属性表
- ✅ `.prj` - 坐标系文件
- 🔶 `.cpg` - 编码文件（推荐，解决中文乱码）

## 🛠️ 功能详述

### 文件完整性检查
- CPG编码文件存在性
- SHP文件组完整性验证
- PRJ坐标系文件检查

### 数据规范性验证  
- 必要字段完整性检查
- 字段内容非空验证
- 几何类型正确性检查

### 空间位置校验
- 地块坐标点与边界范围匹配
- 自动计算正确的中心点坐标
- 坐标系智能转换

### 结果输出
- 📊 Excel详细检查报告
- 🗺️ 交互式HTML地图
- 📈 控制台统计信息

## 📖 使用说明

### 1. 准备数据文件

```
工作目录/
├── 地块信息.xlsx                    # 必需：地块信息表
├── 初步调查4420013990012.zip        # 边界文件ZIP包
├── 详细调查4451023990064.zip        # 边界文件ZIP包
└── ...                             # 更多ZIP文件
```

### 2. 运行程序

启动程序后：
- 选择包含数据文件的工作目录
- 程序自动执行检查流程
- 查看生成的结果报告

### 3. 查看结果

程序完成后会生成：
- **Excel报告**: 新增"result"和"统计信息"工作表
- **HTML地图**: 交互式地图文件
- **控制台输出**: 实时检查进度和统计信息

## 📊 检查结果说明

### 通过状态
- ✅ **pass**: 所有检查项都通过

### 常见问题
- ❌ **地块信息中未找到该地块编码**: 地块编码不匹配
- ⚠️ **cpg文件缺失**: 可能导致中文乱码
- ❌ **字段缺失**: 缺少必要属性字段
- ❌ **几何类型错误**: 不是面（Polygon）类型
- ⚠️ **地理坐标系**: 建议使用投影坐标系
- ❌ **地块位置不在边界范围内**: 空间位置不匹配

## 🔧 构建EXE文件

### 自动化构建
```bash
python build_exe.py
```

### 手动构建
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="边界文件检查工具" src/boundary_check_tool.py
```

## 📁 项目结构

```
boundary-check-tool/
├── src/                          # 源代码
│   ├── boundary_check_tool.py    # 主程序
│   └── ...
├── docs/                         # 文档
│   ├── 使用说明.md               # 详细使用说明
│   ├── images/                   # 图片资源
│   └── examples/                 # 示例文件
├── examples/                     # 示例数据
│   ├── 地块信息示例.xlsx         # 示例Excel文件
│   └── sample_boundary.zip       # 示例边界文件
├── release/                      # 发布版本
│   └── boundary_check_tool.exe   # 可执行文件
├── requirements.txt              # Python依赖
├── build_exe.py                  # EXE构建脚本
├── LICENSE                       # 许可证
└── README.md                     # 项目说明
```

## 🤝 贡献指南

欢迎提交问题和建议!

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 更新日志

### v3.0 (2025-10-08)
- ✨ 新增智能编码检测功能
- 🐛 修复中文路径处理问题
- 🚀 优化批量处理性能
- 📊 改进检查报告格式

## 📞 技术支持

- 🐛 [提交问题](https://github.com/HuangWuwutelling/boundary-check-tool/issues)
- 📖 [查看文档](docs/)
- 💬 [讨论交流](https://github.com/HuangWuwutelling/boundary-check-tool/discussions)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

感谢以下开源项目的支持：
- [GeoPandas](https://geopandas.org/) - 地理数据处理
- [Folium](https://python-visualization.github.io/folium/) - 地图可视化
- [Pandas](https://pandas.pydata.org/) - 数据分析

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！