
# 从源码安装

::: warning ⚠️ 面向进阶用户
本说明仅适用于具备一定技术基础（熟悉 Python 与命令行操作）的开发者。如果你只需要直接打开使用软件，强烈建议前往查阅 [下载发行版](./releases.md)，以避免复杂的环境搭建过程。
:::

## 1. 环境准备
在开始克隆和运行之前，请确保你的系统已正确安装以下前置组件：

- **Python**：版本需要 **≥ 3.10**，并确保已添加到系统环境变量（PATH）。
- **Git**：用于克隆项目代码。
- **FFmpeg**：程序核心依赖 FFmpeg 实现音视频流的最终合并下载。与直接下载发行版不同，**源码运行时不会自带此工具**。你需要提前配置好 FFmpeg 环境。
  > *参考资料*：如需自行编译安装 FFmpeg，可阅读作者博客 [《FFmpeg 编译安装指南》](https://www.scott-sloan.cn/archives/449/)。


## 2. 获取项目源码
打开终端或命令行，执行以下命令将项目源码克隆到本地，并进入项目目录：
```bash
git clone https://github.com/ScottSloan/Bili23-Downloader.git
cd Bili23-Downloader
```

## 3. 配置运行环境
为避免污染系统的全局 Python 环境，推荐使用 `venv` 隔离依赖。

**第一步：创建虚拟环境**
```bash
python -m venv venv
```

**第二步：激活虚拟环境**
此处请根据你的操作系统选择对应的激活命令：

::: code-group
```bash [Windows]
venv\Scripts\activate
```
```bash [macOS / Linux]
source venv/bin/activate
```
:::

**第三步：安装底层依赖包**
```bash
pip install -r requirements.txt
```

::: warning 🛑 Windows 界面兼容性提示
针对 Windows 系统下的 GUI 渲染：请勿主动将 **PySide6** 升级至 `6.11.0` 及更高版本。
强烈推荐维持在 **`6.10.2`** 版本（`requirements.txt` 中默认已限制），否则可能引发程序界面显示异常或撕裂。
:::


## 4. 启动程序
完成上述所有环境配置后，进入主程序 `src` 目录，并启动入口脚本：
```bash
cd src
python main.py
```


## 附录：关于底层构建

::: danger 🚫 编译避坑警告：禁止使用 Nuitka
请**绝对不要**尝试使用 [Nuitka](https://nuitka.net/) 来编译打包本项目！
由于本项目重度依赖 `PySide6`（其底层封装了大量 C++ Qt 库），而 Nuitka 在打包时会将 Python 代码转译为 C 代码。两者在底层内存管理上的冲突会导致编译出的程序在运行时直接崩溃，并抛出不可修复的 `Segmentation fault` (段错误)。若需打包，请务必使用 PyInstaller。
:::

如果你好奇本项目是如何在跨平台上实现自动化构建与封装打包的，欢迎参考以下开源仓库与流水线脚本：

- **自动化构建流 (CI/CD)**：[publish.yml](https://github.com/ScottSloan/Bili23-Downloader/blob/main/.github/workflows/publish.yml)
- **极简化 Python 静态编译脚本**：[Python-Static 仓库](https://github.com/ScottSloan/Python-Static)
- **轻量引导程序**：[Bili23-Downloader-Loader 仓库](https://github.com/ScottSloan/Bili23-Downloader-Loader)
