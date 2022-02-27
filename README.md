# markdown2ubb
基于python的mistune库解析markdown语法，自定义渲染成UBB代码

本项目基于 [https://github.com/sel-fish/md2ubb](https://github.com/sel-fish/md2ubb) 代码修改而来

# 环境
- Python 3.x
- mistune

```bash
    pip install mistune
```

# 使用

```bash
git clone https://github.com/shanhaishi/markdown2ubb
cd markdown2ubb
python md2ubb.py input.md output.txt
```

# 支持语法
- 标题
- 无序列表
- 有序列表
- 粗体/斜体
- 链接
- 引用
- 分割线
- 删除线
- 表格
- 图片（网络图片）
- 代码块

# TODO
- 支持可配置颜色样式
- 支持图片宽高属性