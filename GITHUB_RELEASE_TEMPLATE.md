# GitHub Release 模板

## 发布标题
边界文件检查工具 v3.0 - 首个正式发布版本

## 发布说明

🎉 **边界文件检查工具 v3.0 正式发布！**

这是一个专业的地块边界文件规范性检查工具，支持批量处理SHP格式的边界文件，自动进行文件完整性检查、字段规范性验证和空间位置校验。

## ✨ **主要特性**

- 🚀 **批量处理**: 支持同时检查数百个ZIP格式的边界文件
- 🔍 **智能检测**: 自动识别文件编码(GBK/UTF-8)和坐标系类型
- 📊 **全面检查**: 文件完整性、字段规范性、空间位置一站式验证
- 🗺️ **可视化**: 生成交互式HTML地图展示检查结果
- 📈 **详细报告**: Excel格式的详细检查报告和统计信息
- 🔧 **易于使用**: 图形界面操作，支持EXE独立运行

## 🆕 **版本亮点**

### 新增功能
- ✨ 智能编码检测：自动识别SHP文件的GBK/UTF-8编码
- 🔍 坐标系自适应：支持地理坐标系和投影坐标系自动转换
- 🗺️ 交互式地图：生成HTML地图展示检查结果
- 📊 统计信息：详细的检查统计和通过率分析

### 改进优化
- 🐛 修复中文文件名和路径处理问题
- 🚀 优化批量处理性能，支持数百个文件同时处理
- 📈 改进Excel报告格式，增加详细的字段说明
- 🛡️ 增强错误处理机制，单个文件错误不影响整体处理

## 🎯 **适用场景**

- 土地规划部门的边界文件质量检查
- GIS数据入库前的规范性验证
- 地理数据质量控制和审核
- 批量处理大量地块边界数据

## 🚀 **快速开始**

### 方法一：下载EXE文件（推荐）
1. 下载 `地块边界文件检查工具.exe`
2. 下载 `地块信息模板.xlsx` 作为参考
3. 阅读 `EXE使用说明.txt` 了解基本用法
4. 双击运行exe文件开始使用

### 方法二：Python环境运行
```bash
git clone https://github.com/HuangWuwutelling/boundary-check-tool.git
cd boundary-check-tool
pip install -r requirements.txt
python src/boundary_check_tool.py
```

## 📋 **文件格式要求**

### Excel文件（地块信息.xlsx）
必须包含以下列：
- **地块编码**: 13位数字编码
- **经度**: 地块中心点经度坐标
- **纬度**: 地块中心点纬度坐标

### ZIP文件命名规范
- 格式：`{前缀}{13位地块编码}.zip`
- 示例：`初步调查4420013990012.zip`

## 📊 **检查内容**

1. **文件完整性检查**
   - CPG编码文件是否存在
   - SHP几何文件是否有效
   - PRJ坐标系文件是否存在

2. **数据规范性检查**
   - 必要字段完整性（地块名称、地块代码、行政区代码等）
   - 字段内容是否为空
   - 几何类型是否为面（Polygon）

3. **空间位置校验**
   - 地块坐标点是否在边界范围内
   - 自动计算并提供正确的中心点坐标

## 🏷️ **版本信息**

- **版本号**: v3.0
- **发布日期**: 2025-10-08
- **Python版本**: 3.7+
- **支持系统**: Windows 7/10/11
- **文件大小**: 约106MB

## 📞 **技术支持**

- 🐛 [提交问题](https://github.com/HuangWuwutelling/boundary-check-tool/issues)
- 📖 [查看文档](https://github.com/HuangWuwutelling/boundary-check-tool/tree/main/docs)
- 💬 [讨论交流](https://github.com/HuangWuwutelling/boundary-check-tool/discussions)

## 🙏 **致谢**

感谢以下开源项目的支持：
- [GeoPandas](https://geopandas.org/) - 地理数据处理
- [Folium](https://python-visualization.github.io/folium/) - 地图可视化
- [Pandas](https://pandas.pydata.org/) - 数据分析

---

⭐ **如果这个工具对你有帮助，请给个Star支持一下！**