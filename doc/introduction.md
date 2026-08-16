# 介绍

Bili23-Downloader 是一款跨平台的 B 站视频下载工具，兼容 Windows（含 Win7）、Linux 和 macOS。它拥有现代化 UI，支持音视频流分离下载、多线程加速、弹幕与字幕获取、封面提取、元数据刮削等丰富功能，并可自定义文件命名与分类，满足多样化需求。

本项目致力于为用户提供功能全面、易于上手且高效稳定的下载体验。无论是单个视频还是批量下载，Bili23-Downloader 都能助你轻松完成。

## 核心特性一览
<table class="feature-table">
	<thead>
		<tr>
			<th>特性</th>
			<th>详细说明</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>🖥️ <strong>跨平台支持</strong></td>
			<td>完美兼容 <strong>Windows</strong>（含 Win 7）、<strong>Linux</strong> 和 <strong>macOS</strong> 三大桌面操作系统。</td>
		</tr>
		<tr>
			<td>🎨 <strong>现代 UI 设计</strong></td>
			<td>基于 Fluent Design 设计语言，支持浅色 / 深色主题无缝切换，原生适配高分屏，并会记住窗口位置与大小，下次启动自动恢复。</td>
		</tr>
		<tr>
			<td>🚀 <strong>多线程与加速</strong></td>
			<td>原生集成多线程并行下载、断点续传及网络异常自动重试机制，提供极致的下载速率，同时支持全局下载限速。</td>
		</tr>
		<tr>
			<td>🔗 <strong>多类型解析</strong></td>
			<td>全面支持：<code>投稿视频</code>、<code>番剧</code>、<code>电影</code>、<code>课程</code>、<code>互动视频</code>、<code>UP主空间</code>、<code>收藏夹</code>、<code>每周必看</code>、<code>订阅合集</code>、<code>追番追剧</code>、<code>稍后再看</code>、<code>历史记录</code>等。</td>
		</tr>
		<tr>
			<td>🔍 <strong>批量与检索</strong></td>
			<td>支持一次粘贴多条投稿视频链接<strong>批量解析</strong>；个人空间、收藏夹、历史记录与稍后再看支持<strong>关键词搜索</strong>（可选择只筛选当前页或搜索全部内容）；解析完成后还可按预设条件<strong>自动勾选</strong>下载项。</td>
		</tr>
		<tr>
			<td>⚙️ <strong>音视频自定义</strong></td>
			<td><strong>画质</strong>：<code>8K</code>、<code>4K</code>、<code>HDR</code>、<code>杜比视界</code>等 <br><strong>音质</strong>：<code>Hi-Res 无损</code>、<code>杜比全景声</code>等 <br><strong>编码</strong>：<code>AVC</code>、<code>HEVC</code>、<code>AV1</code><br>下载前可实时预览本次将要下载的媒体内容。 </td>
		</tr>
		<tr>
			<td>💬 <strong>弹幕与字幕</strong></td>
			<td><strong>弹幕</strong>：<code>xml</code>、<code>ass</code>、<code>json</code><br><strong>字幕</strong>：<code>srt</code>、<code>lrc</code>、<code>txt</code>、<code>ass</code>、<code>json</code><br>支持自定义弹幕与字幕样式、指定字幕语言，并可将 <code>ass</code> 格式的弹幕和字幕嵌入 <code>mkv</code> 容器中。</td>
		</tr>
		<tr>
			<td>🖼️ <strong>封面与章节</strong></td>
			<td>无损保存原图质量（<code>jpg</code>、<code>png</code>、<code>avif</code>、<code>webp</code>），原生支持将封面嵌入最终的视频文件（可选嵌入后删除原图），并支持写入视频的<strong>章节信息</strong>。</td>
		</tr>
		<tr>
			<td>🧩 <strong>NFO 元数据</strong></td>
			<td>自动刮削并生成符合 <strong>Kodi</strong>、<strong>Jellyfin</strong>、<strong>Emby</strong> 等媒体中心标准格式的本地媒体元数据。</td>
		</tr>
		<tr>
			<td>📁 <strong>分类与命名</strong></td>
			<td>内置强大规则引擎，可为投稿视频、番剧、课程、互动视频、收藏夹、个人空间、历史记录、稍后再看、每周必看、音乐等类型分别设置命名模板与多级目录分类存储模式。</td>
		</tr>
		<tr>
			<td>📦 <strong>封装格式转化</strong></td>
			<td>智能音视频流混合提取，支持封装输出为 <code>mp4</code> 或 <code>mkv</code>，充分满足不同播放设备的兼容需求。</td>
		</tr>
		<tr>
			<td>🚫 <strong>重复下载检测</strong></td>
			<td>自动记录下载历史，再次下载相同内容时给出提示并可直接跳过，避免重复占用带宽与磁盘空间。</td>
		</tr>
		<tr>
			<td>🌐 <strong>网络与代理</strong></td>
			<td>支持<strong>不使用代理</strong>、<strong>使用系统代理</strong>、<strong>手动设置</strong>三种代理模式，可根据地理位置选择 CDN 节点以改善下载速度，并支持自定义 User-Agent 与 Host。</td>
		</tr>
		<tr>
			<td>📋 <strong>剪贴板监控</strong></td>
			<td>自动识别复制到剪贴板中的 B 站链接，确认后即可直接进入解析下载流程。</td>
		</tr>
		<tr>
			<td>🌍 <strong>国际化支持</strong></td>
			<td>内置多语言界面，开箱可用：简体中文、繁体中文、English。</td>
		</tr>
		<tr>
			<td>🔒 <strong>账号安全登录</strong></td>
			<td>支持快捷安全的<strong>扫码登录</strong>、<strong>短信验证登录</strong>与 <strong>Cookie 登录</strong>。</td>
		</tr>
		<tr>
			<td>📖 <strong>完全开源免费</strong></td>
			<td>基于 <strong>GPL-3.0</strong> 协议发布，代码完全开源、无内购、无广告，拥抱社区共建。</td>
		</tr>
	</tbody>
</table>
