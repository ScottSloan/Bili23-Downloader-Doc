<script setup>
import { data } from '../project.data.js'

function formatURL(type) {
    return `https://github.com/ScottSloan/Bili23-Downloader/releases/download/v${data.version}/Bili23-Downloader_${data.version}_${type}`
}

function formatLanzouURL(key) {
    return `https://scott-sloan.lanzout.com/${key}`
}

let release_url = `https://github.com/ScottSloan/Bili23-Downloader/releases/tag/v${data.version}`

// Windows
let windows_exe_type = 'windows_x64.exe'
let windows_exe_url = formatURL(windows_exe_type)
let windows_exe_url_lanzou = formatLanzouURL(data.lanzou.windows_exe_key)

let windows_zip_type = 'windows_x64_portable.zip'
let windows_zip_url = formatURL(windows_zip_type)
let windows_zip_url_lanzou = formatLanzouURL(data.lanzou.windows_zip_key)

// Windows 7 compatible
let windows_7_exe_type = 'windows_x64_for_win7.exe'
let windows_7_exe_url = formatURL(windows_7_exe_type)
let windows_7_exe_url_lanzou = formatLanzouURL(data.lanzou.windows_7_exe_key)

// Linux AMD64
let linux_amd64_deb_type = 'linux_amd64.deb'
let linux_amd64_deb_url = formatURL(linux_amd64_deb_type)
let linux_amd64_deb_url_lanzou = formatLanzouURL(data.lanzou.linux_amd64_deb_key)

let linux_amd64_tar_gz_type = 'linux_amd64_portable.tar.gz'
let linux_amd64_tar_gz_url = formatURL(linux_amd64_tar_gz_type)
let linux_amd64_tar_gz_url_lanzou = formatLanzouURL(data.lanzou.linux_amd64_tar_gz_key)

// Linux ARM64
let linux_arm64_deb_type = 'linux_arm64.deb'
let linux_arm64_deb_url = formatURL(linux_arm64_deb_type)
let linux_arm64_deb_url_lanzou = formatLanzouURL(data.lanzou.linux_arm64_deb_key)

let linux_arm64_tar_gz_type = 'linux_arm64_portable.tar.gz'
let linux_arm64_tar_gz_url = formatURL(linux_arm64_tar_gz_type)
let linux_arm64_tar_gz_url_lanzou = formatLanzouURL(data.lanzou.linux_arm64_tar_gz_key)

// macOS
let macos_aarch64_type = 'macos_aarch64.dmg'
let macos_aarch64_url = formatURL(macos_aarch64_type)
let macos_aarch64_url_lanzou = formatLanzouURL(data.lanzou.macos_aarch64_key)

let macos_x86_64_type = 'macos_x86_64.dmg'
let macos_x86_64_url = formatURL(macos_x86_64_type)
let macos_x86_64_url_lanzou = formatLanzouURL(data.lanzou.macos_x86_64_key)

</script>

# 下载发行版

目前最新版本为 {{ data.version }}，发布于 {{ data.date }}。

完整更新日志请前往 <a :href="release_url" target="_blank">GitHub 发布页</a> 查看。

::: tip 💡 国内用户提示
推荐国内用户优先选择蓝奏云或OneDrive链接下载。
:::

::: danger 🛑 安全下载提示与免责声明
强烈建议**仅通过下方提供的官方 GitHub 链接**下载本软件。
从第三方网站、网盘论坛或他人私下分享渠道获取的安装包，**极有可能被二次篡改或植入病毒/木马**。对于因下载、运行非官方渠道安装包所导致的任何设备损坏、隐私泄露或财产损失，开发者**概不负责**。
:::

## Windows

::: tip 💡 推荐选择
推荐 Windows 10 1809 及以上版本以及 Windows 11 用户优先选择 **exe 安装包**。
:::

| 系统 / 架构 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Windows 10 1809 及以上 / Windows 11 (x64) | exe 安装包 | 标准安装程序（推荐） | <a :href="windows_exe_url" target="_blank">Github</a> <br> <a :href="windows_exe_url_lanzou" target="_blank">蓝奏云</a> |
| Windows 10 1809 及以上 / Windows 11 (x64) | zip 便携版 | 免安装，解压即用 | <a :href="windows_zip_url" target="_blank">Github</a> <br> <a :href="windows_zip_url_lanzou" target="_blank">蓝奏云</a> |

::: warning ⚠️ 旧版 Windows 用户注意
低于 Windows 10 1809 的系统请**务必**选择下方的 Windows 7 兼容版，否则无法运行。
:::

| 系统 / 架构 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| 低于 Windows 10 1809 (x64) | exe 安装包 | Windows 7 兼容版安装程序 | <a :href="windows_7_exe_url" target="_blank">Github</a> <br> <a :href="windows_7_exe_url_lanzou" target="_blank">蓝奏云</a> |


## Linux
::: warning ⚠️ Linux 用户注意
如果你的系统版本低于要求的版本，请参考 [从源码安装](./manual-installation.md) 并根据文档指引降级依赖以运行本程序。

请根据你的 Linux 发行版和系统架构选择对应的安装包。如果你不确定自己的系统架构，可以在终端输入 `uname -m` 来查看：
- 输出 `x86_64` 表示你使用的是 amd64 架构
- 输出 `aarch64` 或 `arm64` 表示你使用的是 arm64 架构
:::

### AMD64 架构
::: warning ⚠️ 注意
**最低系统版本要求**：Ubuntu 20.04 / Debian 11 / Fedora 32 / RHEL 9 及以上 (glibc 2.31+)
:::

| 系统 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Ubuntu / Debian | deb 安装包 | 原生安装程序 | <a :href="linux_amd64_deb_url" target="_blank">Github</a> <br> <a :href="linux_amd64_deb_url_lanzou" target="_blank">蓝奏云</a> |
| Linux 通用 | tar.gz 便携版 | 解压即用 | <a :href="linux_amd64_tar_gz_url" target="_blank">Github</a> <br> <a :href="linux_amd64_tar_gz_url_lanzou" target="_blank">蓝奏云</a> |


### ARM64 架构
::: warning ⚠️ 注意
**最低系统版本要求**：Ubuntu 24.04 / Debian 13 / Fedora 40 / RHEL 10 及以上 (glibc 2.39+)
:::

| 系统 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Ubuntu / Debian | deb 安装包 | 原生安装程序 | <a :href="linux_arm64_deb_url" target="_blank">Github</a> <br> <a :href="linux_arm64_deb_url_lanzou" target="_blank">蓝奏云</a> |
| Linux 通用 | tar.gz 便携版 | 解压即用 | <a :href="linux_arm64_tar_gz_url" target="_blank">Github</a> <br> <a :href="linux_arm64_tar_gz_url_lanzou" target="_blank">蓝奏云</a> |



## macOS
::: warning ⚠️ macOS 用户注意
**最低系统版本要求**：macOS 12.0 (Monterey) 及以上。
 
如果你的系统版本低于要求的版本，请参考 [从源码安装](./manual-installation.md) 并根据文档指引降级依赖以运行本程序。

请根据你的 Mac 电脑处理器类型选择对应的安装包。如果您遇到了安装包损坏或无法验证的问题，请参考 [macOS 用户常见问题](/doc/faq.html#macos-用户常见问题)。
:::

| 芯片类型 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| 苹果 M 系列芯片 (aarch64) | dmg 安装包 | 适用于 M1/M2/M3/M4 等新型号 | <a :href="macos_aarch64_url" target="_blank">Github</a> <br> <a :href="macos_aarch64_url_lanzou" target="_blank">蓝奏云</a> |
| 英特尔芯片 (x86_64) | dmg 安装包 | 适用于旧款 Intel 芯片型号 | <a :href="macos_x86_64_url" target="_blank">Github</a> <br> <a :href="macos_x86_64_url_lanzou" target="_blank">蓝奏云</a> |

