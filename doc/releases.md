<script setup>
import { data } from '../project.data.js'

function formatURL(type) {
    return `https://github.com/ScottSloan/Bili23-Downloader/releases/download/v${data.version}/Bili23-Downloader_${data.version}_${type}`
}

let release_url = `https://github.com/ScottSloan/Bili23-Downloader/releases/tag/v${data.version}`

let windows_exe_url = formatURL('windows_x64.exe')
let windows_zip_url = formatURL('windows_x64_portable.zip')

let windows_7_exe_url = formatURL('windows_x64_for_win7.exe')

let linux_deb_url = formatURL('linux_amd64.deb')
let linux_tar_gz_url = formatURL('linux_amd64_portable.tar.gz')

let macos_aarch64_url = formatURL('macos_aarch64.dmg')
let macos_x86_64_url = formatURL('macos_x86_64.dmg')

</script>

# 下载发行版

目前最新版本为 {{ data.version }}，发布于 {{ data.date }}。

完整更新日志请前往 <a :href="release_url" target="_blank">GitHub 发布页</a> 查看。

## Windows

::: tip 💡 推荐选择
推荐 Windows 10/11 用户优先选择 **exe 安装包**。
:::

| 系统 / 架构 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Windows 10/11 (x64) | exe 安装包 | 标准安装程序（推荐） | <a :href="windows_exe_url" target="_blank">Github</a> |
| Windows 10/11 (x64) | zip 便携版 | 免安装，解压即用 | <a :href="windows_zip_url" target="_blank">Github</a> |

::: warning ⚠️ Windows 7 用户注意
Windows 7 用户请**务必**选择下方专用版，否则无法运行。
:::

| 系统 / 架构 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Windows 7 (x64) | exe 安装包 | Win7 专用安装程序 | <a :href="windows_7_exe_url" target="_blank">Github</a> |


## Linux
::: warning ⚠️ Linux 用户注意
glibc 版本须为 2.27 及以上，即 Ubuntu 18.04 / Debian 10 及以上版本。请根据你的发行版选择对应的安装包。
:::

| 适用环境 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| Ubuntu / Debian (amd64) | deb 安装包 | 原生安装程序 | <a :href="linux_deb_url" target="_blank">Github</a> |
| Linux 通用 (amd64) | tar.gz 便携版 | 解压即用 | <a :href="linux_tar_gz_url" target="_blank">Github</a> |


## macOS
::: warning ⚠️ macOS 用户注意
最低支持 macOS 12.0 Monterey 版本，请根据你的 Mac 电脑处理器类型（Apple 芯片或 Intel 芯片）选择对应的安装包。

如果你遇到了安装包损坏或无法验证的问题，请参考 [macOS 用户常见问题](/doc/faq.html#macos-用户常见问题)。
:::

| 芯片类型 | 文件类型 | 说明 | 下载链接 |
| :--- | :--- | :--- | :--- |
| 苹果 M 系列芯片 (aarch64) | dmg 安装包 | 适用于 M1/M2/M3/M4 等新型号 | <a :href="macos_aarch64_url" target="_blank">Github</a> |
| 英特尔芯片 (x86_64) | dmg 安装包 | 适用于旧款 Intel 芯片型号 | <a :href="macos_x86_64_url" target="_blank">Github</a> |

