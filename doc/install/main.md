<script setup>
    import { version } from '../../project.json'
    import download_table_raw from '../../download_table.json'

    const download_table = download_table_raw
        .filter(item => item.enable)

    const download_url_table = download_table.map(item => ({
        ...item,
        name: item.name.replace(/\{version\}/g, version),
        github_url: item.github_url.replace(/\{version\}/g, version),
        }))

    const sha256_table = download_table
        .filter(item => item.sha256)
        .map(item => ({
        ...item,
        name: item.name.replace(/\{version\}/g, version)
        }))
    
</script>

# 安装程序
## 下载发行版
用户可前往 [GitHub Release](https://github.com/ScottSloan/Bili23-Downloader/releases/) 页面查看历史版本，也可以在下方列表中根据需要选择下载。

<table>
  <thead>
    <tr>
      <th>文件名</th>
      <th>平台架构</th>
      <th style="white-space: nowrap;">下载地址</th>
      <th>备注</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="row in download_url_table" :key="row.name">
      <td v-html="row.name"></td>
      <td>{{ row.platform }}</td>
      <td>
        <span v-if="row.github_url">
          <a :href="row.github_url" target="_blank">GitHub</a>
        </span>
        <span v-if="row.onedrive_url">
          <br> <a :href="row.onedrive_url" target="_blank">OneDrive</a>
        </span>
        <span v-if="row.lanzou_url">
          <br> <a :href="row.lanzou_url" target="_blank">蓝奏云</a>
        </span>
      </td>
      <td>{{ row.comment }}</td>
    </tr>
  </tbody>
</table>

::: warning 重要提示
Windows 用户请先确保安装 Microsoft Visual C++ 2015-2022 运行库，[点击此处](https://aka.ms/vs/17/release/vc_redist.x64.exe)下载安装。
:::

::: info 社区交流
欢迎[加入社区](https://bili23.scott-sloan.cn/doc/community.html)，获取项目最新动态、问题答疑和技术交流。
:::

文件 SHA256 值校验
<table>
  <thead>
    <tr>
      <th>文件名</th>
      <th>SHA256</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="row in sha256_table" :key="row.name">
      <td v-html="row.name"></td>
      <td>
        <span>{{ row.sha256 }}</span>
      </td>
    </tr>
  </tbody>
</table>

:::tip
下载完成后建议校验 SHA256 值，防止程序被篡改。  

本程序完全开源免费，若是通过其他渠道付费获取的，无法保证其安全性和完整性。  

本程序发行版可能会被防病毒软件误报。如果对防病毒软件报毒有疑问的，请删除本程序，使用其他同类工具。  
:::

### 如何校验 SHA256
::: details 查看校验方法
#### Windows
```bash
certutil -hashfile file_name SHA256
```

#### Linux
```bash
sha256sum file_name
```

#### macOS
```bash
shasum -a 256 file_name
```
:::

## 源码版使用
### 安装 Python 环境
Python 版本需要为 3.10 及以上。

::: details 如果还未安装 Python 环境，点击查看安装方式
从[Python官网](https://www.python.org/)下载系统对应的 Python，建议使用 3.11 及以上版本，最低支持 3.10 版本。  

若下载速度缓慢，建议使用国内[华为云镜像源](https://mirrors.huaweicloud.com/python/)下载。  

安装时注意勾选`Add python.exe to PATH`，创建环境变量。  

[![pElIuQJ.png](https://s21.ax1x.com/2025/02/23/pElIuQJ.png)](https://imgse.com/i/pElIuQJ)

安装完成后，建议执行下面的命令更换 pip 源为清华源，加快 pip 包下载速度：
```bash
pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```
:::

### 克隆仓库
执行下面的命令克隆仓库：
```bash
git clone https://github.com/ScottSloan/Bili23-Downloader.git
cd Bili23-Downloader
```

### 安装依赖
#### Windows & macOS
Windows 和 macOS 用户可以执行下面的命令一键安装所需依赖：

```bash
pip install -r requirements.txt
```

下表为程序所需依赖：
| 包 | 版本 | 备注 |
| -- | -- | -- |
| requests | ==2.32.5 | - |
| wxPython | ==4.2.4 | - |
| qrcode[pil] | ==7.4.2 | 必须附带 [pil]（Pillow），否则程序可能无法运行 |
| python-vlc | ==3.0.21203 | - |
| protobuf | ==6.33.0 | - |
| websockets | ==15.0.1 | -- |
| pycryptodome | ==3.23.0 | -- |

#### Linux
Linux 平台需手动编译 wxPython 安装。

执行下面的命令安装编译所需依赖（以 Ubuntu 为例）：

```bash
sudo apt install build-essential python3-dev libgtk-3-dev libwebkit2gtk-4.0-dev libgstreamer-plugins-base1.0-dev libsdl2-dev libsm-dev libxtst-dev libjpeg-dev libpng-dev libtiff-dev libgdk-pixbuf2.0-dev gstreamer1.0-plugins-base
```

安装 wxPython，pip 将会自动下载源码包并完成编译。

```bash
pip3 install wxPython
```

编译完成后再安装其他依赖：

```bash
pip3 install -r requirements.txt
```

### 安装 FFmpeg
程序依赖 FFmpeg 实现音视频合并，格式转换，直播录制等功能，缺少时将影响正常使用。  

有关 FFmpeg 的安装，请参考[下一页](/doc/install/ffmpeg.html)内容。  

:::tip
Windows 发行版已附带 FFmpeg，无需再次安装。
:::

### 运行程序
直接运行 src 目录下的入口文件 main.py 即可。

```bash
cd src
python3 main.py
```