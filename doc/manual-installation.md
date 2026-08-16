
# 从源码安装

::: warning ⚠️ 面向进阶用户
本说明仅适用于具备一定技术基础（熟悉 Python 与命令行操作）的开发者。如果你只需要直接打开使用软件，强烈建议前往查阅 [下载发行版](./releases.md)，以避免复杂的环境搭建过程。
:::

## 1. 环境准备
在开始克隆和运行之前，请确保你的系统已正确安装以下前置组件：

- **Python**：版本需要 **≥ 3.10**（代码中使用了 3.10 引入的 `match` 语法），并确保已添加到系统环境变量（PATH）。
- **Git**：用于克隆项目代码。
- **FFmpeg**：程序依赖 FFmpeg 完成音视频流的合并。与直接下载发行版不同，**源码运行时不会自带此工具**，需要自行安装并确保其位于 PATH 中。
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

**第三步：安装依赖包**
::: tip 💡 Linux 旧版系统兼容性提示
如果你使用的是较旧的 Linux 发行版，请先将 `requirements.txt` 中 PySide6 的版本上限调整为以下值：

- **amd64 架构**：  
  如果你的 glibc 版本范围为 2.28 ~ 2.33，建议最高使用 6.9.x 版本
  ```bash
  PySide6<6.10
  ```
  低于 2.28 版本不受支持。

- **arm64 架构**：  
  如果你的 glibc 版本范围为 2.31 ~ 2.38，建议最高使用 6.7.x 版本
  ```bash
  PySide6<6.8
  ```

  低于 2.31 版本不受支持。
:::

::: tip 💡 macOS 旧版系统兼容性提示
如果你使用的是 macOS 10.15 或 11，请先将 `requirements.txt` 中 PySide6 的版本上限调整为以下值：

- **macOS 11**：  
  建议最高使用 6.7.x 版本
  ```bash
  PySide6<6.8
  ```
- **macOS 10.15**：  
  建议最高使用 6.4.x 版本
  ```bash
  PySide6<6.5
  ```
:::

```bash
pip install -r requirements.txt
```

## 4. 启动程序
完成上述所有环境配置后，在**项目根目录**下启动入口脚本：
```bash
python src/main.py
```

::: tip 💡 关于 FFmpeg 的查找顺序
程序默认使用内置的 FFmpeg，源码运行时并不存在，此时会自动改用 PATH 中的 FFmpeg，并把设置中的来源同步为「系统 PATH」，无需手动调整。

若始终提示找不到 FFmpeg，可在 **[设置页] → [高级] → [FFmpeg]** 中选择「自定义路径」，手动指定可执行文件的位置。
:::

## 5. 更新源码

后续想升级到最新代码时，在项目根目录执行：
```bash
git pull
```

依赖有变动时（例如 `requirements.txt` 更新），需要在激活虚拟环境后重新安装一次：
```bash
pip install -r requirements.txt
```

## 附录：关于底层构建

如果你好奇本项目是如何在跨平台上实现自动化构建与封装打包的，欢迎参考以下开源仓库与流水线脚本：

- **自动化构建流 (CI/CD)**：[publish.yml](https://github.com/ScottSloan/Bili23-Downloader/blob/main/.github/workflows/publish.yml)
- **极简化 Python 静态编译脚本**：[Python-Static 仓库](https://github.com/ScottSloan/Python-Static)
- **轻量引导程序**：[Bili23-Downloader-Loader 仓库](https://github.com/ScottSloan/Bili23-Downloader-Loader)
