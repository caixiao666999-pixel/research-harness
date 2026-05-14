# 科研 AI 协作 Harness

一个**可复用的科研项目模板**，专为"研究者 + AI"迭代协作设计。

## 快速开始

```bash
# 1. 克隆模板到新项目目录
git clone <this-repo-url> my-new-project
cd my-new-project

# 2. 清空模板的 git 历史，开始新项目
rm -rf .git && git init

# 3. 在 METHOD.md 中填写你的研究目标和初始技术路线

# 4. 启动 Claude Code（或其他 AI agent）
#    AI 会自动读取 CLAUDE.md / AGENTS.md / STATUS.md / METHOD.md 进入工作流
```

## 核心理念

科研代码 ≠ 传统软件。科研代码是**为了验证想法**，方向会反复调整。这个 harness 围绕以下迭代循环设计：

```
你给方案 → AI 规划 → AI 执行 → AI 报告 → 你评估 → 调整方案 → 下一轮
```

## 五个阶段

AI 每次回复开头都会声明当前阶段：

| 阶段 | 含义 |
|------|------|
| `[planning]` | 规划下一次实验 |
| `[executing]` | 编码、跑实验 |
| `[reporting]` | 写实验报告 |
| `[awaiting-review]` | 等你评估 |
| `[revising]` | 根据你的反馈更新方法文档 |

详见 [CLAUDE.md](./CLAUDE.md)。

## 目录结构

```
.
├── CLAUDE.md / AGENTS.md   # AI 启动指令（两份内容必须完全一致；pre-commit hook 校验）
├── METHOD.md               # 研究目标 + 技术路线 + 修订历史（append-only）
├── STATUS.md               # 当前阶段 + 活跃实验（可多个） + blocker
├── FINDINGS.md             # 跨实验沉淀的规律性发现（append-only）
├── src/                    # 跨实验复用的代码（仅当代码已被 ≥2 个实验复用才提升）
├── experiments/            # 所有实验，按日期命名
│   └── YYYY-MM-DD-name/
│       ├── REPORT.md       # ✅ git（含预测对比、复现配方、负面结果标记）
│       ├── plan.md         # ✅ git（含 pre-registration 预测段，冻结）
│       ├── code/           # ✅ git
│       ├── data/           # ❌ 本地保留
│       └── results/        # ❌ 本地保留
├── archive/                # 大结构改动时整体归档旧版本
├── templates/              # REPORT 和实验目录的模板
├── scripts/                # 维护脚本（如 check_docs_sync.py）
└── .githooks/              # 仓库级 git hooks（需手动启用，见下）
```

### 启用 pre-commit hook（首次克隆后做一次）

```bash
git config core.hooksPath .githooks
```

启用后，每次 commit 会自动校验 `CLAUDE.md` 和 `AGENTS.md` 是否同步。
若没启用 hook，可手动运行：

```bash
python scripts/check_docs_sync.py
```

## 工作流示例

1. **写 METHOD.md**：填写目标、技术路线、评估方式
2. **告诉 AI**："请帮我规划第一次实验" → AI 进入 `[planning]`
3. **批准实验计划** → AI 进入 `[executing]`，在 `experiments/2026-05-14-xxx/` 下编码
   - plan.md 的"实验前预测"段在开跑前填写并**冻结**（避免 HARKing）
4. **实验跑完** → AI 进入 `[reporting]`，写 REPORT.md（含预测对比、复现配方、负面结果标记），进入 `[awaiting-review]`
5. **你评估报告**：
   - 满意 → 进入下一轮规划
   - 发现跨实验规律 → AI 会问是否追加到 `FINDINGS.md`
   - 需要调整方案 → AI 进入 `[revising]`，**追加**新版本到 METHOD.md
6. **如果 AI 在执行阶段卡住**：会切到 `[awaiting-review]` 并在 STATUS.md 写明 blocker，等你回应
7. **如果是结构性改动**：AI 会询问是否归档当前 src/ 到 archive/

## Git 约定

- AI **不会自动 commit/push**，但会在关键节点（写完 REPORT、更新 METHOD 等）主动询问
- `experiments/*/data/` 和 `experiments/*/results/` 默认本地保留（不进 git）
- REPORT.md、plan.md、code/ 默认进 git，便于版本化追溯叙事

## 多 AI 评估

本 harness 假设你会**手动**在多个 AI 工具（Claude / GPT / Gemini）和真人之间切换收集评估意见，AI 不会自动调用其他模型的 API。
