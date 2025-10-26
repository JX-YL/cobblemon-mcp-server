# 📤 v1.5.0 发布指南

由于 GitHub 连接问题，请按以下步骤手动发布 v1.5.0：

---

## ✅ 已完成的步骤

- [x] 更新 README.md
- [x] 更新 CHANGELOG.md
- [x] 更新 server.py（添加性别和性格进化支持）
- [x] 创建新的验证器（PropertiesValidator, BiomeValidator, DamageValidator）
- [x] 生成测试包并验证成功
- [x] 提交到本地 Git（commit: 526188a）
- [x] 创建标签 v1.5.0
- [x] 创建 Release Notes（RELEASE_v1.5.0.md）

---

## 🚀 待完成的步骤

### 1. 推送到 GitHub

当网络恢复后，运行以下命令：

```bash
cd "E:\AI Super Personal Studio\Workspace\Cobblemon\Cobblemon_mcp_server"

# 推送提交
git push origin main

# 推送标签
git push origin v1.5.0
```

### 2. 创建 GitHub Release

#### 方法 1: 使用 GitHub Web 界面

1. 访问 https://github.com/JX-YL/cobblemon-mcp-server/releases/new
2. 选择标签：`v1.5.0`
3. 标题：`v1.5.0 - Gender and Nature Evolution Support`
4. 描述：复制 `RELEASE_v1.5.0.md` 的内容
5. 点击 "Publish release"

#### 方法 2: 使用 GitHub CLI（如果已安装）

```bash
cd "E:\AI Super Personal Studio\Workspace\Cobblemon\Cobblemon_mcp_server"

gh release create v1.5.0 \
  --title "v1.5.0 - Gender and Nature Evolution Support" \
  --notes-file RELEASE_v1.5.0.md
```

---

## 📝 Release Notes 预览

已创建完整的 Release Notes：`RELEASE_v1.5.0.md`

### 核心内容

✨ **新功能**:
- 性别进化（Gender Evolution）
- 性格进化（Nature Evolution）
- PropertiesValidator, BiomeValidator, DamageValidator

✅ **测试**:
- 4 个进化链全部测试通过
- 9 个宝可梦数据包生成成功

📦 **示例**:
- Venomtail → Toxempress（性别进化）
- Voltbaby → Ampedrocker（性格进化）
- Omnidivine（传说宝可梦）
- Flamepup → Blazetiger（御三家）
- Aquagem → Tidalcrystal（道具进化）

---

## 🔍 验证清单

发布前请确认：

- [ ] README.md 已更新为 v1.5.0
- [ ] CHANGELOG.md 包含 v1.5.0 条目
- [ ] 测试包可以在游戏中正常加载
- [ ] 所有进化链都能正常工作
- [ ] Git 提交已完成
- [ ] Git 标签已创建
- [ ] GitHub 推送成功
- [ ] GitHub Release 已创建

---

## 🎯 快速命令

### 查看本地状态

```bash
git log --oneline -5
git tag -l
git status
```

### 重试推送（网络恢复后）

```bash
# 推送主分支
git push origin main

# 推送标签
git push origin v1.5.0

# 查看远程状态
git ls-remote --tags origin
```

---

## 🐛 常见问题

### Q: 推送时提示 "Failed to connect to github.com"

**A**: 网络连接问题，可以：
1. 检查 VPN/代理设置
2. 等待网络恢复
3. 使用 GitHub Desktop 推送

### Q: 标签已存在

**A**: 删除旧标签：
```bash
git tag -d v1.5.0
git push origin :refs/tags/v1.5.0
```

### Q: Release 创建失败

**A**: 确保：
1. 标签已推送到 GitHub
2. 使用正确的仓库权限
3. Release Notes 格式正确

---

## 📊 提交信息

```
Commit: 526188a
Author: JX-YL
Date: 2025-10-25
Message: v1.5.0: Add gender and nature evolution support

Changes:
- README.md (updated)
- CHANGELOG.md (updated)
- server.py (updated)
- tools/validators/properties_validator.py (new)
- tools/validators/biome_validator.py (new)
- tools/validators/damage_validator.py (new)
- docs/design/V1.5.0_DESIGN.md (new)
- generate_showcase_mcp.py (new)
- V1.5.0_SUCCESS_FINAL.md (new)
```

---

## 🎉 完成后

发布成功后：

1. ✅ 更新 Issue/Discussion 通知用户
2. ✅ 在项目 README 徽章中会自动更新版本号
3. ✅ 用户可以通过 `git clone` 或 GitHub Releases 获取

---

**祝发布顺利！🚀**

---

*最后更新: 2025-10-25*

