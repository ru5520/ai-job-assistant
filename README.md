# AI Job Assistant · 招聘 JD 筛选

轻量级 Python 小工具：用**可配置关键词与权重**对招聘 **JD（职位描述）** 做方向归类与得分，辅助快速筛选 AI 相关岗位；并支持简历与 JD 的关键词匹配报告、雷达图可视化。

## 功能概览

- **`taxonomy.py`**：定义岗位类别与关键词（支持按词加权）。
- **`classifier.py`**：对 JD 文本打分，输出主方向、置信度与各维度占比；结果写入 `report.txt`。
- **`app.py`**：读取 `resume.txt` 与 `jd.txt`，做关键词提取与匹配/缺失分析，写入 `output.txt`。
- **`visualize.py`**：基于分类得分生成雷达图 `radar_chart.png`（无界面环境也可保存图片）。

脚本内路径均相对**项目根目录**解析，在任意当前目录下运行均可。

## 环境

```bash
cd /path/to/ai_job_assistant
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 运行示例

```bash
python classifier.py
python app.py
python visualize.py
```

## 在 Cursor / VS Code 里避免「文件找不到」

1. **优先用工作区文件打开项目**：双击或打开仓库里的 `ai_job_assistant.code-workspace`，工作区根目录即为本项目，侧边栏与相对路径一致。
2. 已开启 **自动保存**（约 0.4s 延迟）与 **热退出**（关闭窗口时尽量保留未保存缓冲）。重要修改可再按一次 **Ctrl+S**。
3. 请尽量**固定只打开本仓库这一层目录**，不要长期把 `d:\cursor` 等上级大目录当工作区又去找子文件夹里的路径，容易和会话里已关闭的旧路径混淆。

## 上传到 GitHub（本地已 `git init` 时）

1. 在 [GitHub](https://github.com/new) 新建仓库（例如 `ai-job-assistant`），**不要**勾选添加 README / .gitignore（避免冲突）。
2. 在本项目目录执行（将 `YOUR_USER` / `YOUR_REPO` 换成你的）：

```bash
cd /path/to/ai_job_assistant
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

若使用 SSH：

```bash
git remote add origin git@github.com:YOUR_USER/YOUR_REPO.git
git push -u origin main
```

首次推送前确保已提交：

```bash
git add -A
git status
git commit -m "Initial publish: JD screening assistant"
git push -u origin main
```

## 类别示例

- Model_Algo · AI_Infra · Perception · Decision_Planning · Engineering_Tooling  

可在 `taxonomy.py` 中按业务增删类别与关键词。
