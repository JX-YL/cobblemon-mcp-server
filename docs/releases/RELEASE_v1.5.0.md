# 🎉 v1.5.0 Release Notes - Gender and Nature Evolution Support

**发布日期**: 2025-10-25  
**版本**: v1.5.0  
**类型**: 功能更新

---

## 🌟 主要更新

### ⭐ Properties 进化条件支持

v1.5.0 为 Cobblemon MCP Server 带来了两个重要的进化条件：**性别进化**和**性格进化**！

#### 🚺 性别进化（Gender Evolution）
现在可以创建只有特定性别才能进化的宝可梦！

**特性**:
- 支持 `male`（雄性）、`female`（雌性）、`genderless`（无性别）
- 官方格式：`{"variant": "properties", "target": "gender=female"}`
- 完美模拟官方宝可梦（如 Salandit → Salazzle）

**使用示例**:
```python
create_complete_package(
    name="Venomtail",
    dex=99001,
    primary_type="poison",
    secondary_type="fire",
    maleRatio=0.875,  # 87.5% 雄性
    evolution_target="toxempress",
    evolution_level=33,
    evolution_gender="female"  # 只有雌性才能进化
)
```

**游戏中测试**:
```
/pokespawn venomtail gender=female level=32
/pokeedit 1 level=33  # 进化成 Toxempress ✅
```

#### 🎭 性格进化（Nature Evolution）
根据性格决定进化形态！

**特性**:
- 支持所有 25 种官方性格（hardy, adamant, modest, timid 等）
- 官方格式：`{"variant": "properties", "target": "宝可梦名 nature=hardy"}`
- 完美模拟官方宝可梦（如 Toxel → Toxtricity 形态）

**使用示例**:
```python
create_complete_package(
    name="Voltbaby",
    dex=99003,
    primary_type="electric",
    secondary_type="poison",
    evolution_target="ampedrocker",
    evolution_level=30,
    evolution_nature="hardy"  # 只有 Hardy 性格才能进化
)
```

**游戏中测试**:
```
/pokespawn voltbaby nature=hardy level=29
/pokeedit 1 level=30  # 进化成 Ampedrocker ✅
```

---

## 🔧 技术细节

### 新增参数

| 参数 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `evolution_gender` | str | 性别进化条件 | "male", "female", "genderless" |
| `evolution_nature` | str | 性格进化条件 | "hardy", "adamant", "modest" |

### 新增验证器

- **PropertiesValidator** - 验证性别和性格条件
  - 检查性别值是否有效
  - 检查性格值是否在 25 种官方性格中
  
- **BiomeValidator** - 验证生物群系条件（预留给 v1.5.1）
- **DamageValidator** - 验证伤害条件（预留给 v1.5.1）

### EvolutionValidator 增强

- 新增 `properties` 进化变体支持
- 集成 PropertiesValidator 进行深度验证
- 提供详细的错误提示和建议

---

## ✅ 测试报告

### 测试方法：渐进式验证

经过多轮测试和优化，我们采用了**渐进式测试方法**：

1. **简单测试** - GenderPup → GenderWolf（基础性别进化）✅
2. **双属性测试** - Venomtail → Toxempress（性别进化）✅
3. **性格测试** - Voltbaby → Ampedrocker（性格进化）✅
4. **完整测试** - 4 个进化链同时运行 ✅

### 测试结果：100% 通过

| 进化链 | 类型 | 状态 |
|--------|------|------|
| Venomtail → Toxempress | 性别（雌性，33级） | ✅ 成功 |
| Voltbaby → Ampedrocker | 性格（Hardy，30级） | ✅ 成功 |
| Fairypup → Pixiedragon | 性别（雌性，25级） | ✅ 成功 |
| Moonpup → Lunarwolf | 性格（Timid，22级） | ✅ 成功 |

### 关键发现

1. ✅ **`behaviour` 字段不是必需的** - 简化了配置
2. ✅ **自定义宝可梦进化链完全可行** - 无需依赖原版宝可梦
3. ✅ **Properties 进化格式经过官方验证** - 与官方完全兼容

---

## 📦 示例数据包

v1.5.0 包含一个完整的功能展示包，包括：

### 🔥 1. 性别进化
- **Venomtail** (#99001) - 毒/火，87.5%♂
  - → **Toxempress** (#99002) - 33级+雌性进化，100%♀

### ⚡ 2. 性格进化
- **Voltbaby** (#99003) - 电/毒
  - → **Ampedrocker** (#99004) - 30级+Hardy性格进化

### 🌟 3. 传说宝可梦
- **Omnidivine** (#99005) - 超能力/妖精
  - 种族值 700，捕获率 3，无性别

### 🦊 4. 御三家（等级进化）
- **Flamepup** (#99006) - 火系，87.5%♂
  - → **Blazetiger** (#99007) - 16级进化，火/格斗

### 💎 5. 道具进化
- **Aquagem** (#99008) - 水/岩石
  - → **Tidalcrystal** (#99009) - 水之石进化

---

## 🎮 快速开始

### 1. 安装

```bash
git clone https://github.com/JX-YL/cobblemon-mcp-server.git
cd cobblemon-mcp-server
pip install -r requirements.txt
```

### 2. 生成测试包

```bash
python generate_showcase_mcp.py
```

### 3. 游戏中测试

将 `output/` 下的数据包复制到 `.minecraft/saves/<世界名>/datapacks/`，然后：

```
/reload
/pokespawn venomtail gender=female level=32
/pokeedit 1 level=33
```

看到 Venomtail 进化成 Toxempress，恭喜你！🎉

---

## 🚀 完整功能列表

### 进化系统

| 功能 | 版本 | 状态 |
|------|------|------|
| 等级进化 | v1.1.0 | ✅ |
| 道具进化 | v1.3.0 | ✅ |
| 交换进化 | v1.3.0 | ✅ |
| 亲密度条件 | v1.3.0 | ✅ |
| 时间条件 | v1.3.0 | ✅ |
| 招式类型条件 | v1.3.0 | ✅ |
| **性别条件** | **v1.5.0** | ✅ ⭐ |
| **性格条件** | **v1.5.0** | ✅ ⭐ |

### 基础配置（v1.4.1）

- ✅ 双属性（secondaryType）
- ✅ 自定义特性（abilities，1-3个）
- ✅ 性别比例（maleRatio）
- ✅ 努力值产出（evYield）
- ✅ 捕获率（catchRate）
- ✅ 初始亲密度（baseFriendship）
- ✅ 孵蛋周期（eggCycles）
- ✅ 体型配置（height, weight, baseScale）

---

## 📝 文档更新

- ✅ README.md - 添加 v1.5.0 功能介绍
- ✅ CHANGELOG.md - 详细变更日志
- ✅ 快速检验指令.md - 完整测试指南
- ✅ V1.5.0_SUCCESS_FINAL.md - 开发历程总结

---

## 🎓 经验总结

### 开发历程

v1.5.0 的开发经历了多次迭代：

1. **首次尝试** - 添加了所有预期功能，但无法加载 ❌
2. **排查问题** - 分析官方文件，发现 `behaviour` 可选
3. **回退重试** - 回到 v1.4.1，重新设计
4. **渐进式测试** - 一步步验证每个功能
5. **完全成功** - 所有进化链都能工作 ✅

### 关键经验

1. **参考官方格式** - 官方文件是最好的参考
2. **渐进式测试** - 从简单到复杂逐步验证
3. **不放弃精神** - 遇到问题不退缩，找到解决方案
4. **持续优化** - 每次失败都是学习机会

---

## 🔮 未来计划

### v1.5.1 - 生物群系与伤害进化

- [ ] 生物群系进化条件（biome）
- [ ] 伤害进化条件（damage_taken）
- [ ] 复合条件优化

### v1.6.0 - 完整进化系统

- [ ] 所有官方进化变体
- [ ] 多形态进化分支
- [ ] 更多特殊进化条件

### v2.0.0 - 终极目标

- [ ] 完整的官方格式支持
- [ ] Web UI 界面
- [ ] 批量生成工具
- [ ] 模板系统

---

## 🙏 致谢

感谢所有参与测试和反馈的用户！

特别感谢：
- 耐心的测试和详细的反馈
- 提供宝贵的官方参考数据
- 不放弃的精神和持续支持

没有你们的帮助，v1.5.0 不可能这么快完成！

---

## 📊 统计数据

- **开发时间**: ~8 小时
- **测试包数量**: 20+
- **新增代码**: 2000+ 行
- **成功测试**: 4 个进化链，9 个宝可梦
- **文档更新**: 5 个文件

---

## 🔗 链接

- **GitHub**: https://github.com/JX-YL/cobblemon-mcp-server
- **Issue Tracker**: https://github.com/JX-YL/cobblemon-mcp-server/issues
- **详细文档**: [README.md](README.md)
- **变更日志**: [CHANGELOG.md](CHANGELOG.md)

---

## 📥 下载

**完整源码**: [cobblemon-mcp-server-v1.5.0.zip]

**测试数据包**: 运行 `python generate_showcase_mcp.py` 生成

---

**🎊 祝使用愉快！🎊**

---

*Cobblemon MCP Server v1.5.0 - Gender and Nature Evolution Support*  
*Released: 2025-10-25*  
*License: MIT*

