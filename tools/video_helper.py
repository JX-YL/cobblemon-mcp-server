"""
视频制作辅助工具
用于生成视频脚本、演示数据和录制清单
"""

import json
import sys
import io
from pathlib import Path
from datetime import datetime

# 确保输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class VideoHelper:
    """视频制作辅助类"""
    
    def __init__(self, output_dir="video_production"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def generate_episode_script(self, episode_number: int, topic: str, duration: int = 10):
        """
        生成分集脚本模板
        
        Args:
            episode_number: 第几期
            topic: 主题（如"项目介绍"、"基础功能"）
            duration: 预计时长（分钟）
        """
        script_dir = self.output_dir / "01_scripts"
        script_dir.mkdir(exist_ok=True)
        
        script_content = f"""# 【第{episode_number}期】{topic}

**预计时长**: {duration} 分钟  
**制作日期**: {datetime.now().strftime('%Y-%m-%d')}  
**状态**: 📝 脚本编写中

---

## 🎬 时间轴规划

| 时间段 | 内容 | 画面 | 旁白/字幕 |
|--------|------|------|-----------|
| 0:00-0:10 | 片头 | 项目Logo + 标题动画 | BGM |
| 0:10-0:40 | 引入 |  |  |
| 0:40-2:00 | 主体1 |  |  |
| 2:00-4:00 | 主体2 |  |  |
| 4:00-6:00 | 演示 |  |  |
| 6:00-8:00 | 总结 |  |  |
| 8:00-{duration}:00 | 片尾 | 下期预告 + 关注提示 |  |

---

## 📝 详细脚本

### 【片头】(0:00-0:10)
**画面**：
- 

**字幕**：
- 

**旁白**：
- 

---

### 【正文】

#### 第一部分 (0:10-X:XX)

**画面**：
- 

**操作步骤**：
1. 
2. 
3. 

**旁白**：
「」

**字幕要点**：
- 
- 

---

## 🎥 录制素材清单

### 屏幕录制
- [ ] 素材1：
- [ ] 素材2：
- [ ] 素材3：

### 游戏录制
- [ ] 场景1：
- [ ] 场景2：
- [ ] 场景3：

### 静态截图
- [ ] 图片1：
- [ ] 图片2：

---

## 🎨 后期制作要点

### 字幕
- [ ] 时间轴同步
- [ ] 关键词高亮
- [ ] 特效字幕（如"重要！"）

### 特效
- [ ] 转场效果
- [ ] 画面缩放
- [ ] 高亮框选

### 音效
- [ ] BGM（音量 -20dB）
- [ ] 点击音效
- [ ] 成功提示音

---

## 📋 发布检查清单

- [ ] 脚本完成
- [ ] 素材录制完成
- [ ] 粗剪完成
- [ ] 字幕校对
- [ ] 封面设计
- [ ] 简介编写
- [ ] 标签设置
- [ ] 定时发布设置

---

**制作进度**: ⬜⬜⬜⬜⬜ 0%
"""
        
        script_file = script_dir / f"episode_{episode_number:02d}_{topic}.md"
        script_file.write_text(script_content, encoding='utf-8')
        
        return f"✅ 脚本模板已生成: {script_file}"
    
    def generate_demo_checklist(self):
        """生成演示录制检查清单"""
        checklist_dir = self.output_dir / "03_assets"
        checklist_dir.mkdir(exist_ok=True)
        
        checklist_content = """# 🎥 录制前检查清单

## 环境准备

### 系统设置
- [ ] 关闭所有通知（Windows通知中心 + 应用）
- [ ] 清理桌面（移除私人文件/截图）
- [ ] 隐藏任务栏不必要的图标
- [ ] 设置高性能电源模式
- [ ] 关闭自动更新

### 录制软件（OBS Studio）
- [ ] 分辨率：1920x1080
- [ ] 帧率：60 FPS
- [ ] 编码器：NVENC H.264
- [ ] 码率：8000-12000 Kbps
- [ ] 音频：48kHz, 192kbps
- [ ] 热键设置测试（开始/停止录制）

### 游戏设置（Minecraft）
- [ ] 分辨率：1920x1080 全屏
- [ ] 帧率：60+ FPS（F3 检查）
- [ ] 视频设置：最高画质
- [ ] 着色器：开启（如 BSL/Complementary）
- [ ] 资源包：美化纹理（可选）
- [ ] F1 隐藏 UI 快捷键测试

### 开发环境（VS Code/Cursor）
- [ ] 字体：Fira Code / Consolas（大号，易读）
- [ ] 主题：Dark+（深色）或 One Dark Pro
- [ ] 缩放：125%-150%（便于观看）
- [ ] 关闭侧边栏（录制时 Ctrl+B）
- [ ] 扩展：禁用不必要的弹窗

---

## 演示数据准备

### Minecraft 游戏环境
- [ ] 创建测试世界：「MCP_Demo_World」
- [ ] 加载 Cobblemon 模组（版本：1.5.2+）
- [ ] 清空 datapacks 文件夹
- [ ] 准备测试区域（平坦地形，良好光照）
- [ ] 设置快捷栏（空精灵球 x64）

### MCP Server 环境
- [ ] Python 环境激活
- [ ] 依赖安装完成（`pip install -r requirements.txt`）
- [ ] server.py 可正常运行
- [ ] Cursor MCP 配置正确（测试连接）

### 演示脚本
- [ ] `generate_showcase_mcp.py` 可运行
- [ ] 输出目录清空（`output/`）
- [ ] 测试生成一个宝可梦（确保无错误）

### 命令准备（复制到记事本）
```bash
# 重载数据包
/reload

# 生成测试宝可梦
/pokespawn venomtail gender=female level=32
/pokespawn voltbaby nature=hardy level=29
/pokespawn flamepup level=15
/pokespawn omnidivine

# 编辑宝可梦等级（触发进化）
/pokeedit 1 level=33
/pokeedit 2 level=30
/pokeedit 3 level=16

# 给予道具
/give @s cobblemon:water_stone

# 清空队伍
/pc releaseall

# 查看宝可梦属性
右键打开宝可梦面板
```

---

## 录制场景清单

### 场景 1：项目介绍（VS Code）
- [ ] 打开项目根目录
- [ ] 展示 README.md（滚动浏览）
- [ ] 展示 docs/ 文件结构
- [ ] 高亮显示核心文件（server.py, tools/, services/）
- [ ] **时长**: 30-60秒

### 场景 2：生成宝可梦（终端 + VS Code）
- [ ] 打开终端（Ctrl+`）
- [ ] 运行 `python docs/examples/generate_showcase_mcp.py`
- [ ] 展示生成过程（输出日志）
- [ ] 打开 output/ 目录，查看生成的文件夹
- [ ] 打开一个 species.json 文件，滚动查看
- [ ] **时长**: 2-3分钟

### 场景 3：复制到游戏目录（文件管理器）
- [ ] 打开 output/ 目录
- [ ] 全选所有宝可梦文件夹（Ctrl+A）
- [ ] 复制（Ctrl+C）
- [ ] 打开游戏存档的 datapacks 目录
- [ ] 粘贴（Ctrl+V）
- [ ] **时长**: 20-30秒

### 场景 4：游戏内加载（Minecraft）
- [ ] 进入游戏世界
- [ ] 按 T 打开聊天栏
- [ ] 输入 `/reload` 并回车
- [ ] 等待重载完成（显示成功消息）
- [ ] **时长**: 10-15秒

### 场景 5：生成宝可梦（游戏内）
- [ ] `/pokespawn venomtail gender=female level=32`
- [ ] 右键查看宝可梦属性（展示性别、等级）
- [ ] 关闭面板
- [ ] 重复生成其他 2-3 只宝可梦
- [ ] **时长**: 1-2分钟

### 场景 6：进化演示（游戏内 - 重点）
- [ ] **性别进化**：
  - 选中 Venomtail（雌性，32级）
  - `/pokeedit 1 level=33`
  - 观看进化动画（完整录制，不要切掉）
  - 展示进化后的 Toxempress
- [ ] **性格进化**：
  - 选中 Voltbaby（Hardy，29级）
  - `/pokeedit 2 level=30`
  - 观看进化动画
  - 展示进化后的 Ampedrocker
- [ ] **道具进化**（如有）：
  - 选中 Aquagem
  - 给予水之石
  - 右键使用
  - 观看进化动画
- [ ] **时长**: 3-5分钟（核心内容）

### 场景 7：属性对比（游戏内）
- [ ] 打开宝可梦面板
- [ ] 展示种族值、性别比例
- [ ] 查看招式列表
- [ ] 查看特性
- [ ] **时长**: 1-2分钟

---

## 音频录制

### 旁白录制
- [ ] 麦克风测试（电平 -12dB 至 -6dB）
- [ ] 环境噪音检查（关闭风扇、空调）
- [ ] 使用防喷罩
- [ ] 录音软件：Audacity / Adobe Audition
- [ ] 后期处理：降噪、均衡、压缩

### BGM 准备
- [ ] 片头 BGM（10秒，激昂）
- [ ] 正文 BGM（轻快，不抢风头）
- [ ] 片尾 BGM（温和，引导关注）
- [ ] 音效：点击音、成功提示音、错误提示音

---

## 录制技巧

### 屏幕录制技巧
1. **鼠标移动**：慢速、平滑，避免突然跳跃
2. **打字速度**：正常或稍慢，确保观众能看清
3. **滚动页面**：慢速滚动，停留 2-3 秒
4. **高亮重点**：用鼠标框选或光标悬停

### 游戏录制技巧
1. **视角控制**：平稳旋转，避免快速甩视角
2. **移动速度**：正常行走，不要疾跑（除非必要）
3. **光线**：白天录制，或使用夜视药水
4. **距离**：保持合适距离，能看清宝可梦模型

### 避免的错误
- ❌ 录制时弹出通知
- ❌ 录制到私人信息（浏览器历史、文件名）
- ❌ 音频有杂音或爆音
- ❌ 帧率突然下降（卡顿）
- ❌ 游戏内快速切换场景（让人头晕）

---

## 录制后处理

### 文件整理
- [ ] 重命名文件（episode_01_screen_01.mp4）
- [ ] 备份到云盘（阿里云盘/百度网盘）
- [ ] 检查完整性（播放无损坏）

### 素材标记
- [ ] 用播放器打记录关键时间点
- [ ] 标记精彩片段（用于预告）
- [ ] 标记失误片段（剪掉）

---

## 📅 录制时间规划

**建议录制时间段**：
- 🌅 上午 9-11点（精力充沛，环境安静）
- 🌙 晚上 8-10点（白天工作，晚上录制）

**避免时间段**：
- ❌ 午饭后（容易困倦）
- ❌ 深夜（噪音控制难，精力不足）

**录制顺序**：
1. 先录所有屏幕演示（VS Code + 终端）
2. 再录所有游戏演示（Minecraft）
3. 最后补录特写镜头（如特定属性展示）

---

## 紧急备用方案

### 如果录制中断
- [ ] 记录当前进度（时间点、场景）
- [ ] 保存当前录制文件
- [ ] 重新开始时保持一致性（光线、音量、语速）

### 如果出现错误
- [ ] 不要停止录制，继续往下走
- [ ] 后期剪辑时处理
- [ ] 严重错误再重录该片段

---

**最后检查**：录制前通读此清单 3 遍！

**制作日期**: {datetime}
**状态**: ✅ 准备就绪 / ⏳ 准备中
"""
        
        checklist_file = checklist_dir / "recording_checklist.md"
        checklist_file.write_text(checklist_content, encoding='utf-8')
        
        return f"✅ 录制检查清单已生成: {checklist_file}"
    
    def generate_timeline_template(self):
        """生成视频时间轴模板（用于剪辑软件）"""
        timeline_dir = self.output_dir / "04_project_files"
        timeline_dir.mkdir(exist_ok=True)
        
        timeline_content = {
            "project_name": "Cobblemon_MCP_Episode_01",
            "duration": "10:00",
            "timeline": [
                {
                    "start": "0:00",
                    "end": "0:10",
                    "type": "intro",
                    "content": "片头动画",
                    "tracks": {
                        "video": "logo_animation.mp4",
                        "audio": "intro_music.mp3",
                        "subtitle": "Cobblemon MCP Server v1.5.0"
                    }
                },
                {
                    "start": "0:10",
                    "end": "0:40",
                    "type": "hook",
                    "content": "问题引入",
                    "tracks": {
                        "video": "game_showcase.mp4",
                        "audio": "voiceover_hook.mp3",
                        "subtitle": "想在Minecraft中添加自己的宝可梦吗？"
                    }
                },
                {
                    "start": "0:40",
                    "end": "2:00",
                    "type": "introduction",
                    "content": "项目介绍",
                    "tracks": {
                        "video": "screen_recording_01.mp4",
                        "audio": "voiceover_intro.mp3 + bgm_soft.mp3 (-20dB)",
                        "subtitle": "Cobblemon MCP Server 功能介绍"
                    }
                }
            ],
            "effects": {
                "transitions": ["fade", "slide", "zoom"],
                "text_animations": ["typewriter", "fade_in", "bounce"],
                "color_grading": "standard"
            },
            "export_settings": {
                "format": "MP4",
                "codec": "H.264",
                "resolution": "1920x1080",
                "framerate": 60,
                "bitrate": "10 Mbps"
            }
        }
        
        timeline_file = timeline_dir / "timeline_template.json"
        timeline_file.write_text(json.dumps(timeline_content, indent=2, ensure_ascii=False), encoding='utf-8')
        
        return f"✅ 时间轴模板已生成: {timeline_file}"
    
    def generate_all_templates(self):
        """一键生成所有模板"""
        results = []
        
        # 生成5期脚本模板
        topics = [
            ("项目介绍", 10),
            ("基础功能", 12),
            ("进化机制", 15),
            ("高级技巧", 12),
            ("版本演进", 8)
        ]
        
        for i, (topic, duration) in enumerate(topics, 1):
            result = self.generate_episode_script(i, topic, duration)
            results.append(result)
        
        # 生成检查清单
        results.append(self.generate_demo_checklist())
        
        # 生成时间轴模板
        results.append(self.generate_timeline_template())
        
        # 创建其他必要目录
        (self.output_dir / "02_recordings/screen_recordings").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "02_recordings/game_footage").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "02_recordings/audio").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "03_assets/thumbnails").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "03_assets/graphics").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "03_assets/music").mkdir(parents=True, exist_ok=True)
        (self.output_dir / "05_exports").mkdir(parents=True, exist_ok=True)
        
        results.append(f"\n✅ 目录结构已创建: {self.output_dir}/")
        
        return "\n".join(results)


def main():
    """主函数：生成所有视频制作模板"""
    print("=" * 80)
    print("                    视频制作辅助工具")
    print("=" * 80)
    
    helper = VideoHelper()
    result = helper.generate_all_templates()
    
    print("\n" + result)
    
    print("\n" + "=" * 80)
    print("                    ✅ 模板生成完成！")
    print("=" * 80)
    
    print("\n📁 生成的文件：")
    print("  - video_production/01_scripts/       # 5个分集脚本模板")
    print("  - video_production/03_assets/        # 录制检查清单")
    print("  - video_production/04_project_files/ # 时间轴模板")
    
    print("\n📝 下一步：")
    print("  1. 编辑脚本模板（填充具体内容）")
    print("  2. 按照检查清单准备录制环境")
    print("  3. 开始录制素材")
    print("  4. 使用时间轴模板进行剪辑")
    
    print("\n💡 提示：运行此脚本不会覆盖已存在的文件")


if __name__ == "__main__":
    main()

