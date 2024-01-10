# DigitalMate 🤖💬

欢迎来到DigitalMate的代码仓库，这是一个与当前AI大模型进行互动的一站式项目。本项目利用Gradio创建了一个用户友好的网络界面，允许用户与AI进行文本和语音生成对话。目前，已经完成了文本对话部分，并计划未来集成AI对话、文本语音对话、绘图等多种功能。

## 特点 ✨

- **文本生成对话**：与GPT模型进行书面对话。
- **语音生成对话**：体验AI回答的语音形式（即将到来）。
- **自定义用户界面**：具有动态渐变背景的现代风格界面。
- **代理支持**：为网络请求配置HTTP和HTTPS代理。
- **个性化AI**：根据系统设置配置AI，使其回答带有特定风格。

## 安装 🛠️

在运行网络界面之前，您需要安装所需的依赖项。按照以下步骤开始：

```bash
pip install gradio librosa httpx openai pyyaml
```

## 配置 ⚙️

1. 将`config.yml.example`重命名为`config.yml`。
2. 在`config.yml`文件中输入您的OpenAI API密钥和代理设置。
3. 根据需要编辑`gpt_system`设置，以自定义AI的行为。

## 运行界面 🚀

要启动网络界面，只需运行以下命令：

```bash
uvicorn webui:demo --reload
```

默认情况下，界面将在`http://0.0.0.0:8888`上可用。

## 自定义 🎨

您可以自由修改`ui.css`文件以更改界面的外观和感觉。提供的CSS带有生动的界面设计和动画，为您的AI聊天体验增添个性。

## 贡献 🤝

贡献是使开源社区成为学习、启发和创造的绝佳场所的原因。您所做的任何贡献都是**非常感激**的。

1. Fork项目
2. 创建您的特性分支(`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个拉取请求

## 许可证 📜

根据MIT许可证分发。有关更多信息，请查看`LICENSE`文件。

## 联系方式 📧

[作者邮箱](snychng@gmail.com)

项目链接: [https://github.com/snychng/DigitalMate](https://github.com/snychng/DigitalMate)

---

如果您喜欢这个项目，请给我一个⭐️！