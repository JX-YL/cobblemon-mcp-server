# v1.4.0 回退说明

**回退时间**: 2025-10-23  
**原因**: 导入游戏后无法加载  
**回退至**: v1.3.0

---

## ✅ 已完成的本地回退操作

### 1. Git 回退
- ✅ 硬重置到 v1.3.0 标签 (commit: 74fe8b5)
- ✅ 删除本地 v1.4.0 标签
- ✅ 清理所有 v1.4.0 测试包

### 2. 清理的文件
已删除以下 v1.4.0 相关文件：
- `output/toxel_package/`
- `output/blissey_package/`
- `output/eevee_package/`
- `output/mewtwo_package/`
- `output/V1.4.0_TEST_REPORT.md`

### 3. 当前状态
```
当前提交: 74fe8b5 (v1.3.0)
当前标签: v1.0.0, v1.1.0, v1.2.0, v1.3.0
工作区状态: 干净
```

---

## ⚠️ 待完成的 GitHub 操作

由于网络问题，以下操作需要在网络恢复后手动完成：

### 方法 1: 使用提供的脚本（推荐）
双击运行 `push_to_github.bat`

### 方法 2: 手动执行命令
```bash
# 1. 强制推送 main 分支
git push -f origin main

# 2. 删除远程 v1.4.0 标签
git push origin :refs/tags/v1.4.0
```

### 方法 3: 在 GitHub 网页操作
1. 打开 https://github.com/JX-YL/cobblemon-mcp-server/releases
2. 找到 v1.4.0 Release
3. 点击 Delete 删除

---

## 🔍 v1.4.0 问题分析

可能导致游戏无法加载的原因：

### 1. JSON 格式问题
v1.4.0 新增字段可能与 Cobblemon 当前版本不兼容：
- `secondaryType` - 双属性字段
- `abilities` - 特性数组格式
- `evYield` - 努力值对象
- `maleRatio` - 性别比例

### 2. 字段顺序
Cobblemon 可能对 JSON 字段顺序敏感，v1.4.0 改变了字段排列

### 3. 数据类型
某些字段的数据类型可能不正确（如 float vs int）

---

## 📋 v1.3.0 功能（当前版本）

### ✅ 支持的功能
- ✅ 基础宝可梦配置（名称、图鉴号、属性、种族值）
- ✅ 招式配置（等级招式、TM招式）
- ✅ 等级进化（level_up）
- ✅ 道具进化（item_interact）
- ✅ 交换进化（trade）
- ✅ 复合进化条件（level, friendship, time_range, has_move_type, biome）
- ✅ 进化验证器（防止配置错误）

### ❌ 不支持的功能（v1.4.0 功能已回退）
- ❌ 双属性（secondaryType）
- ❌ 自定义特性（abilities）
- ❌ 性别比例（maleRatio）
- ❌ 努力值产出（evYield）
- ❌ 捕获率（catchRate）
- ❌ 初始亲密度（baseFriendship）
- ❌ 体型配置（height, weight, baseScale）
- ❌ 孵蛋周期（eggCycles）

---

## 🚀 后续计划

### 短期（保持 v1.3.0）
1. 测试 v1.3.0 在游戏中的稳定性
2. 确认所有进化类型正常工作
3. 收集用户反馈

### 中期（修复 v1.4.0）
1. 分析具体的加载失败原因
2. 逐个测试新增字段的兼容性
3. 查阅 Cobblemon 官方文档确认字段格式

### 长期（重新发布）
1. 创建小规模测试版本（仅添加1-2个字段）
2. 在游戏中充分测试
3. 逐步添加更多字段
4. 发布稳定的 v1.4.0 或 v1.5.0

---

## 📝 经验教训

1. **充分测试**: 在发布新版本前，必须在实际游戏环境中测试
2. **增量更新**: 不要一次性添加太多新字段
3. **官方文档**: 需要参考 Cobblemon 官方 species 格式文档
4. **向后兼容**: 考虑字段的可选性和默认值

---

## ✅ 验证步骤

回退完成后，请验证：
- [ ] 本地 git 状态是 v1.3.0
- [ ] GitHub 的 main 分支是 v1.3.0
- [ ] GitHub Releases 中没有 v1.4.0
- [ ] 生成的测试包可以在游戏中正常加载

---

**备注**: 此文档记录了回退过程，便于未来参考和问题分析。

