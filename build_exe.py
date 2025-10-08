# -*- coding: utf-8 -*-
"""
边界文件检查工具 PyInstaller 打包脚本
用于将Python脚本打包成独立的exe可执行文件

使用方法：
1. 安装PyInstaller: pip install pyinstaller
2. 运行此脚本: python build_exe.py
或者直接使用: pyinstaller boundary_check.spec

作者: HuangWuwutelling
日期: 2025-10-08
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def clean_build_files():
    """清理之前的构建文件"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    files_to_clean = ['*.spec']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"已清理目录: {dir_name}")
    
    # 清理spec文件
    for spec_file in Path('.').glob('*.spec'):
        spec_file.unlink()
        print(f"已清理文件: {spec_file}")

def create_spec_file():
    """创建PyInstaller配置文件"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['边界文件检测工具V3.py'],
    pathex=[],
    binaries=[],
    datas=[
        # 添加geopandas相关数据文件
        # ('path/to/geopandas/datasets', 'geopandas/datasets'),
    ],
    hiddenimports=[
        'geopandas',
        'fiona.drvsupport',
        'fiona.crs',
        'fiona.env',
        'fiona._shim',
        'fiona.schema',
        'pyproj.datadir',
        'pyproj._datadir',
        'pyproj.crs',
        'pandas.io.formats.style',
        'shapely.geometry',
        'rtree.index',
        'chardet.universaldetector',
        'openpyxl.cell._writer',
        'xlrd.xldate',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'folium.plugins',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib.tests',
        'numpy.tests',
        'pandas.tests',
        'PIL.tests',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='边界文件检查工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 设为True显示控制台，False为无窗口模式
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('boundary_check.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("已创建 boundary_check.spec 配置文件")

def build_exe():
    """执行打包命令"""
    try:
        print("开始构建exe文件...")
        
        # 使用spec文件构建
        cmd = ['pyinstaller', 'boundary_check.spec']
        
        process = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if process.returncode == 0:
            print("✅ 构建成功！")
            print("exe文件位置: dist/边界文件检查工具.exe")
            
            # 检查文件大小
            exe_path = Path('dist/边界文件检查工具.exe')
            if exe_path.exists():
                size_mb = exe_path.stat().st_size / (1024 * 1024)
                print(f"文件大小: {size_mb:.1f} MB")
        else:
            print("❌ 构建失败！")
            print("错误信息:")
            print(process.stderr)
            return False
            
    except Exception as e:
        print(f"构建过程出错: {e}")
        return False
    
    return True

def create_batch_script():
    """创建批处理脚本用于快速构建"""
    batch_content = '''@echo off
echo 边界文件检查工具 - 自动构建脚本
echo ====================================

echo 检查Python环境...
python --version
if errorlevel 1 (
    echo 错误: 未找到Python环境
    pause
    exit /b 1
)

echo 检查PyInstaller...
pyinstaller --version
if errorlevel 1 (
    echo 安装PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo 错误: PyInstaller安装失败
        pause
        exit /b 1
    )
)

echo 开始构建...
python build_exe.py

echo 构建完成！
pause
'''
    
    with open('build.bat', 'w', encoding='gbk') as f:
        f.write(batch_content)
    print("已创建 build.bat 批处理脚本")

def main():
    """主函数"""
    print("=" * 50)
    print("边界文件检查工具 - EXE构建脚本")
    print("=" * 50)
    
    # 检查源文件是否存在
    source_file = '边界文件检测工具V3.py'
    if not os.path.exists(source_file):
        print(f"❌ 错误: 源文件 {source_file} 不存在")
        print("请确保脚本在包含Python源文件的目录中运行")
        return
    
    # 清理旧文件
    print("1. 清理构建文件...")
    clean_build_files()
    
    # 创建配置文件
    print("2. 创建配置文件...")
    create_spec_file()
    
    # 创建批处理脚本
    print("3. 创建批处理脚本...")
    create_batch_script()
    
    # 构建exe
    print("4. 开始构建...")
    success = build_exe()
    
    if success:
        print("\n" + "=" * 50)
        print("🎉 构建完成！")
        print("=" * 50)
        print("生成的文件:")
        print("- dist/边界文件检查工具.exe  (可执行文件)")
        print("- boundary_check.spec       (PyInstaller配置)")
        print("- build.bat                 (批处理构建脚本)")
        print("\n使用说明:")
        print("1. 将exe文件复制到工作目录")
        print("2. 准备地块信息.xlsx和边界文件zip")
        print("3. 双击运行exe文件")
    else:
        print("\n❌ 构建失败，请检查错误信息")

if __name__ == "__main__":
    main()