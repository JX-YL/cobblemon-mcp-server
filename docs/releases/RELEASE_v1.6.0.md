# v1.6.0 发布指南

## 📦 发布信息

- **版本**: v1.6.0
- **发布日期**: 2025-10-28
- **标题**: Move System Enhancement（招式系统完善）
- **类型**: Feature Release

---

## ✅ 发布前检查清单

- [x] 代码已提交（commit 556a62b）
- [x] 标签已创建（v1.6.0）
- [ ] 代码已推送到 GitHub
- [ ] 标签已推送到 GitHub
- [ ] GitHub Release 已创建

---

## 🚀 手动推送步骤

由于网络问题，需要手动推送：

### 1. 推送代码
```bash
cd "E:\AI Super Personal Studio\Workspace\Cobblemon\Cobblemon_mcp_server"
git push origin main
```

### 2. 推送标签
```bash
git push origin v1.6.0
```

### 3. 创建 GitHub Release

访问：https://github.com/JX-YL/cobblemon-mcp-server/releases/new

**Tag**: `v1.6.0`

**Release Title**: `v1.6.0 - Move System Enhancement`

**Description**:

```markdown
## 🎯 v1.6.0 - 招式系统完善

### ✨ 新功能

**完整招式分类系统** - 支持所有官方 Cobblemon 招式分类：

- ✅ **等级招式（Level Moves）** - 升级自动学会
- ✅ **蛋招式（Egg Moves）** - 遗传招式
- ✅ **TM招式（TM Moves）** - 技能机器招式
- ✅ **教学招式（Tutor Moves）** - 教学招式
- ✅ **遗留招式（Legacy Moves）** - 旧版本招式
- ✅ **特殊招式（Special Moves）** - 特殊事件招式

### 🔧 技术特性

- **515个官方招式验证** - 自动验证招式是否存在
- **智能拼写检查** - 拼写错误时提供相似招式建议
- **自动格式化** - 自动转换为官方格式（`1:tackle`, `egg:bellydrum`）
- **自动排序** - 等级招式按等级自动排序

### 📊 使用示例

```python
create_pokemon_with_stats(
    name="Charmander",
    dex=4,
    primary_type="fire",
    
    # v1.6.0: 完整招式系统
    level_moves={
        1: ["scratch", "growl"],
        4: ["ember"],
        17: ["firefang"],
        40: ["flareblitz"]
    },
    egg_moves=["bellydrum", "dragontail"],
    tm_moves=["flamethrower", "fireblast"],
    tutor_moves=["blastburn", "heatwave"],
    legacy_moves=["attract", "return"],
    special_moves=["celebrate"]
)
```

### 🧪 测试验证

- ✅ 游戏内验证通过
- ✅ 所有招式正确加载
- ✅ 招式按等级自动学习
- ✅ 6种分类全部正确显示

### 📈 覆盖率提升

**62% → 75%** (+13%)

### 📚 文档

- [设计文档](docs/design/V1.6.0_DESIGN.md)
- [测试指南](docs/tests/V1.6.0_TEST_GUIDE.md)
- [覆盖率分析](docs/design/DATAPACK_COVERAGE_ANALYSIS.md)

### 🔗 相关链接

- [完整更新日志](CHANGELOG.md#v160---2025-10-28)
- [README](README.md)

---

**安装方式**: 参见 [README.md](README.md#-安装)
```

---

## 📋 发布后任务

- [ ] 在 Discord/论坛 发布更新公告
- [ ] 更新项目主页
- [ ] 准备演示视频（可选）

---

## 📝 版本亮点

1. **完整招式系统** - 6种分类，515个官方招式
2. **智能验证** - 自动检查和建议
3. **游戏内验证** - 已测试可用
4. **覆盖率大幅提升** - 从62%到75%

---

## 🎉 完成标志

所有任务完成后，更新此清单：

- [x] ✅ 代码提交完成
- [x] ✅ 标签创建完成
- [x] ✅ 文档更新完成
- [ ] ⏳ GitHub 推送待完成（网络问题）
- [ ] ⏳ Release 创建待完成

---

**准备就绪！** 等待网络恢复后推送到 GitHub。

