# Update detail and Build mkdocs
# author: @probiusofficial
# date: 2023-09-25
import os

# 从docs/CNAME中获取CNAME
CNAME = "starlink.tjsec.cn" #默认
with open("docs/CNAME", "r") as f:
    CNAME = f.read()
    f.close()
print("Got CNAME: " + CNAME)

url = "https://" + CNAME # https://starlink.tjsec.cn/

# Update docs/detial/index.md
'''
- 移动 docs/home/allprojects.md 到 docs/detail/index.md
- 移除 docs/detail/index.md 中“----------------------------------------”以上的内容 替换为 "# 全部项目 / All_Projects"
- 替换 docs/detail/index.md 中 "/detail" 为 ""(空)
'''

# Update Raiders/index.md
'''
- 移动 docs/column/starlink_project_video.md 到 docs/Raiders/index.md
'''

# Update docs/index.md
'''
- 替换 docs/README.md 中 "/detail" 为 url+"/detail"
- 删除docs/README.md中的 ".md"

- 项目动态 / Project News更新：获取 docs/README.md 中 "**1.项目动态**" 到 "**2.StarRank**" 之间的内容，替换 docs/index.md 中 "<!-- insert Project News -->" 到 "<!-- Project News End-->" 之间的内容

- StarRank更新：获取 docs/README.md 中 "**2.StarRank**" 到 "**3.项目列表**" 之间的内容，替换 docs/index.md 中 "<!-- insert StarRank -->" 到 "<!-- StarRank End-->" 之间的内容

- 更新动态 / Update News更新：获取 docs/README.md 中 "**3.项目列表**" 到 "**4.新项目加入**" 之间的内容，替换 docs/index.md 中 "<!-- insert Update News -->" 到 "<!-- Update News End-->" 之间的内容

- 新项目加入 / New Project_in更新：获取 docs/README.md 中 "**4.新项目加入**" 到 "**5.[分类:甲方工具](party_a.md)**" 之间的内容，替换 docs/index.md 中 "<!-- insert New Project_in -->" 到 "<!-- New Project_in End-->" 之间的内容
'''
# Update mkdocs.yml
'''
遍历docs下面的所有文件：
- 使用docs中的md文件来构建 主页
- 使用docs/detail中的md文件来构建 项目目录及细节
- 使用docs/column来中的文件来构建 Kcon兵器谱
- 使用docs/Raiders中的文件来构建 星际奇兵
具体规则如下：
'''
## nav start

### update 主页
'''
参考data.json中的
'''
### update 项目目录及细节

### update Kcon兵器谱

### update 星际奇兵

## nav end