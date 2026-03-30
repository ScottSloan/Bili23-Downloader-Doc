import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Bili23 Downloader",
  description: "跨平台的 B 站视频下载工具，支持现代UI、音视频流分离下载、多线程下载、弹幕与字幕获取、封面提取及元数据刮削，可自定义文件命名与分类，兼容 Windows（含 Win7）、Linux 和 macOS。",

  lastUpdated: true,
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '首页', link: '/' },
      { text: '文档', link: '/doc/introduction' },
      { text: '博客', link: 'https://www.scott-sloan.cn' }
    ],

    sidebar: [
      {
        text: '简介',
        collapsed: false,
        items: [
          { text: '项目介绍', link: '/doc/introduction' },
          { text: '下载发行版', link: '/doc/releases' },
          { text: '从源码安装', link: '/doc/manual-installation' }
        ]
      },
      {
        text: '使用指南',
        collapsed: false,
        items: [
          { text: '基础使用', link: '/doc/basic-usage' },
          { text: '常见问题 (FAQ)', link: '/doc/faq' },
          { text: '进阶：自定义命名与归类', link: '/doc/advanced-usage' }
        ]
      },
      {
        text: '支持与社区',
        collapsed: false,
        items: [
          { text: '社区交流', link: '/doc/community' },
          { text: '使用协议', link: '/doc/terms' },
          { text: '关于与支持', link: '/doc/about' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/ScottSloan/Bili23-Downloader' },
      { icon: 'qq', link: 'https://qm.qq.com/q/KX3uJIFIYK' }
    ],

    footer: {
      copyright: 'Copyright © 2025-2026 Scott Sloan. All Rights Reserved.',
      message: '<a href="https://beian.miit.gov.cn/" target="_blank">滇ICP备2023007640号-1</a>'
    },
    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            searchBoxPlaceholder: '搜索文档',
            displayDetails: '显示详情',
            backButtonTitle: '后退',
            resetButtonTitle: '清除查询条件',
            footer: {
              selectText: '选择',
              closeText: '关闭',
              navigateText: '导航'
            }
          }
        }
      }
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    },
    
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    outlineTitle: '页面导航'
  }
})
