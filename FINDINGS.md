# 跨实验发现

> ⚠️ **本文件仅用户可改。** AI 起草新 finding 条目建议，由用户审查后手动追加。详见 CLAUDE.md "AI 写作权限边界"。

> 本文件沉淀**跨多次实验**的规律性发现，是 METHOD.md 与 REPORT.md 之间的中间层：
> - `METHOD.md` 说"方法应该怎么做"
> - `REPORT.md` 说"单次实验发生了什么"
> - `FINDINGS.md` 说"我们从多次实验中学到了什么共性规律"
>
> **规则**：
> 1. **Append-only**：不删除旧条目。即使后来被推翻，也只能追加"被实验 X 推翻"的注记
> 2. 每条 finding 必须引用 **≥1 个 `REPORT.md`** 作为证据
> 3. **AI 不直接编辑本文件** —— 只在 chat 里起草建议条目，由用户审查后手动追加
> 4. 一条 finding 入库后，应在下一次 METHOD 修订时考虑是否要把它体现进技术路线

---

## 条目模板

```
### Finding N — 一句话标题（YYYY-MM-DD）

**陈述**：……（一句话总结这个规律）

**证据**：
- `experiments/YYYY-MM-DD-name1/REPORT.md` — 哪部分支持？
- `experiments/YYYY-MM-DD-name2/REPORT.md` — 哪部分支持？

**适用范围 / 边界**：在什么条件下成立？什么条件下不成立？

**对 METHOD 的含义**：这个发现是否已经体现在 METHOD vN 中？还是仍待整合？
```

---

## 发现列表

> 首条 finding 由用户批准后追加于此。

（暂无）
