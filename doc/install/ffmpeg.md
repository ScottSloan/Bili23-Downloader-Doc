# 安装 FFmpeg
程序依赖 FFmpeg 实现音视频合并，格式转换，直播录制等功能，缺少时将影响正常使用。

:::tip
Windows 发行版已附带 FFmpeg，无需再次安装。
:::

## Windows 
Windows 用户可从下方直接下载编译版本：

[官网下载](https://ffmpeg.org/)  
[蓝奏云](https://wwx.lanzout.com/iMJkM2oup3mh) 密码：dnn9（来源于：gyan.dev，版本：7.1）

:::info
Windows 也可手动编译 FFmpeg，具体方法请参考博客文章[Windows 平台下使用 MSYS 2 编译 FFmpeg](https://www.scott-sloan.cn/archives/449/)。
:::

## Linux 包管理器安装
通过包管理器安装 FFmpeg，操作简单，但安装的版本可能不是最新版本。如果需要最新版本，请参考下方编译安装方式手动编译。

对于基于 Debain 的系统，在终端中执行以下命令：
```bash
sudo apt update
sudo apt install ffmpeg
```

对于基于 RPM 的系统，在终端中执行以下命令：
```bash
sudo dnf install ffmpeg
```

如果使用 yum 作为包管理器，则执行：
```bash
sudo yum install ffmpeg
```

对于 Arch Linux，在终端执行以下命令：
```bash
sudo pacman -S ffmpeg
```

## Linux & macOS 编译安装 {build}
如需安装最新版本或自定义编译参数，可选择源码编译安装。主要步骤如下：

### 安装依赖
以 Ubuntu 为例，执行下面的命令：

```bash
sudo apt update
sudo apt install -y git build-essential pkg-config yasm nasm libx264-dev libx265-dev libvpx-dev libfdk-aac-dev libmp3lame-dev libopus-dev
```

macOS 用户可使用 Homebrew 安装依赖：
```bash
brew install git yasm nasm x264 x265 libvpx fdk-aac lame opus
```

### 克隆 FFmpeg 源码
```bash
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
cd ffmpeg
```

### 配置编译参数
以下参数配置与 Windows 发行版附带的 FFmpeg 相同，用户也可以根据实际的需要调整参数配置。
注意还需手动编译安装 `libmp3lame`，并将 `--extra-cflags` 和 `--extra-ldflags` 路径修改为实际安装目录。

```bash
./configure \
--prefix=./ffmpeg-build \
--disable-doc \
--disable-shared \
--disable-everything \
--disable-programs \
--disable-swscale \
--disable-filters \
--disable-swresample \
--disable-avx512 \
--disable-network \
--disable-avdevice \
--disable-autodetect \
--enable-demuxer='concat,ffmetadata,mov,mp4,flv,m4a,mp3,m4a' \
--enable-muxer='mp4,flv,mp3,m4a,flac' \
--enable-decoder='h264,hevc,av1,aac,flac,eac3,ac3' \
--enable-encoder='libmp3lame,flac' \
--enable-static \
--enable-small \
--enable-ffmpeg \
--enable-protocol='file,concat' \
--enable-libmp3lame \
--enable-gpl \
--extra-ldflags="-L/path/to/libmp3lame/lame-3.100/build/lib -static -static-libgcc -static-libstdc++" \
--extra-cflags="-I/path/to/libmp3lame/lame-3.100/build/include" \
```

:::tip
libmp3lame 详细编译步骤请参考[博客文章](https://www.scott-sloan.cn/archives/449/)。
:::

### 编译并安装
```bash
make -j8
sudo make install
```

编译完成后，可通过 `ffmpeg -version` 验证安装。

## 创建环境变量
### Windows
对于 Windows 用户，下载完成 FFmpeg 后，还需将其添加至环境变量。

右键`此电脑`，点击`属性`，在设置中点击`高级系统设置`。

<img src="https://bili23.scott-sloan.cn/1764927728.png">

点击`环境变量`。

<img src="https://bili23.scott-sloan.cn/1764927887.png">

在`系统变量`一栏中找到`Path`并选中，点击`编辑`。

<img src="https://bili23.scott-sloan.cn/1764927925.png">

点击`新建`，填入`ffmpeg.exe`所在的文件夹（例如：`D:/Software/ffmpeg/bin`）即可。

<img src="https://bili23.scott-sloan.cn/1764927951.png">

<img src="https://bili23.scott-sloan.cn/1764927971.png">

最后，在终端中运行`ffmpeg`测试环境变量是否创建成功。

<img src="https://bili23.scott-sloan.cn/1764928001.png">
