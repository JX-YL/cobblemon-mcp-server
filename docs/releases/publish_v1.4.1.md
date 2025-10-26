# v1.4.1 发布指南

## ⚠️ 网络问题说明

目前 Git push 遇到网络连接问题：
```
fatal: unable to access 'https://github.com/JX-YL/cobblemon-mcp-server.git/'
Failed to connect to github.com port 443
```

---

## 📋 发布步骤

### 方法 1：稍后重试自动推送

等待网络恢复后，在项目目录执行：

```bash
cd "E:\AI Super Personal Studio\Workspace\Cobblemon\Cobblemon_mcp_server"

# 推送提交
git push origin main

# 推送标签
git push origin v1.4.1
```

---

### 方法 2：手动发布（如果网络持续有问题）

#### 1️⃣ 检查本地提交
```bash
git log --oneline -3
```

应该看到：
```
861a86f docs: Add v1.4.1 GitHub release notes
78ae0af v1.4.1: Add MCP-based test package generator
d6d71f1 v1.4.1: Fix v1.4.0 game loading issue
```

#### 2️⃣ 创建并推送标签
```bash
# 如果标签已存在，先删除
git tag -d v1.4.1
git push origin :refs/tags/v1.4.1

# 重新创建标签
git tag -a v1.4.1 -m "v1.4.1: Bug fix release - Fix game loading issue"

# 推送标签（稍后网络恢复时）
git push origin v1.4.1
```

#### 3️⃣ 推送代码
```bash
git push origin main
```

#### 4️⃣ 在 GitHub 创建 Release

1. 打开浏览器访问：
   ```
   https://github.com/JX-YL/cobblemon-mcp-server/releases/new
   ```

2. 选择标签：`v1.4.1`

3. Release 标题：
   ```
   v1.4.1 - Bug Fix Release
   ```

4. 复制 `GITHUB_RELEASE_v1.4.1.md` 的内容到描述框

5. 点击 "Publish release"

---

## ✅ 当前状态

### 本地提交状态
- ✅ v1.4.1 代码修复已提交
- ✅ MCP 测试包生成器已提交  
- ✅ GitHub Release 说明已提交
- ⏳ 等待推送到 GitHub

### 待完成事项
- [ ] 推送代码到 GitHub (`git push origin main`)
- [ ] 创建并推送标签 (`git tag -a v1.4.1 && git push origin v1.4.1`)
- [ ] 在 GitHub 创建 Release

---

## 🎯 快速命令（网络恢复后执行）

```bash
# 进入项目目录
cd "E:\AI Super Personal Studio\Workspace\Cobblemon\Cobblemon_mcp_server"

# 推送代码
git push origin main

# 创建标签（如果不存在）
git tag -a v1.4.1 -m "v1.4.1: Bug fix release"

# 推送标签
git push origin v1.4.1
```

然后访问：https://github.com/JX-YL/cobblemon-mcp-server/releases/new

---

## 📝 Release 内容预览

请将 `GITHUB_RELEASE_v1.4.1.md` 的内容复制到 GitHub Release 描述中。

关键内容：
- 🐛 修复 v1.4.0 游戏无法加载的问题
- ✨ height/weight 单位说明（分米/百克）
- 📦 5 个测试包示例
- 🔧 从 v1.4.0 升级指南

---

## 🔍 验证发布成功

发布后，检查：
1. https://github.com/JX-YL/cobblemon-mcp-server/releases - 应该看到 v1.4.1
2. https://github.com/JX-YL/cobblemon-mcp-server/tags - 应该看到 v1.4.1 标签
3. `README.md` 中的 badge 应该显示 v1.4.1

---

**当前已在浏览器中打开 GitHub 仓库页面，请稍后手动完成发布！**


