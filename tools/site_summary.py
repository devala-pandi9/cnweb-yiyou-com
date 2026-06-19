SITE_DATA = {
    "title": "易游体育",
    "url": "https://cnweb-yiyou.com",
    "keywords": ["易游体育", "体育资讯", "赛事数据"],
    "tags": ["体育", "赛事", "资讯", "数据"],
    "description": "易游体育专注于提供国内外体育赛事资讯与数据分析服务。"
}

def format_summary(data: dict) -> str:
    kw = ", ".join(data["keywords"])
    tags = ", ".join(data["tags"])
    lines = [
        f"网站名称：{data['title']}",
        f"网站地址：{data['url']}",
        f"核心关键词：{kw}",
        f"标签分类：{tags}",
        f"简要说明：{data['description']}",
    ]
    return "\n".join(lines)

def render_html_card(data: dict) -> str:
    kw_html = " ".join(f"<span class='kw'>{k}</span>" for k in data["keywords"])
    tag_html = " ".join(f"<span class='tag'>{t}</span>" for t in data["tags"])
    return f"""
<div class="site-card">
  <h3>{data['title']}</h3>
  <p><strong>URL:</strong> <a href="{data['url']}">{data['url']}</a></p>
  <p><strong>关键词:</strong> {kw_html}</p>
  <p><strong>标签:</strong> {tag_html}</p>
  <p><strong>简介:</strong> {data['description']}</p>
</div>
"""

def print_structured_summary(data: dict) -> None:
    print("=" * 42)
    print(format_summary(data))
    print("=" * 42)

def print_html_preview(data: dict) -> None:
    print(render_html_card(data))

if __name__ == "__main__":
    site = SITE_DATA.copy()
    print_structured_summary(site)
    print()
    print_html_preview(site)