<div align="center">
 
  <h2 align="center">Cloudflare - Turnstile Solver</h2>
  <p align="center">
A Python-based solution for solving Cloudflare Turnstile challenges quickly (4-6 seconds solve time). The script uses undetected Playwright library to interact with web pages and solve the challenges without running additional browser instances.
    <br />
    <br />
    <a href="https://discord.cyberious.xyz">💬 Discord</a>
    ·
    <a href="https://github.com/sexfrance/Turnstile-Solver#-changelog">📜 ChangeLog</a>
    ·
    <a href="https://github.com/sexfrance/Turnstile-Solver/issues">⚠️ Report Bug</a>
    ·
    <a href="https://github.com/sexfrance/Turnstile-Solver/issues">💡 Request Feature</a>
  </p>
</div>

### ⚙️ Installation

- Requires: `Python 3.8+`
- Make a python virtual environment: `python3 -m venv venv`
- Source the environment: `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (macOS, Linux)
- Install the requirements: `pip install -r requirements.txt`
- Start: `Remove comments for testing in async and sync python files then run those`

---

### 🔥 Features
- **Debug Logging**: Detailed debug logs track actions and progress, making troubleshooting straightforward.
- **Automated CAPTCHA Solver**: Uses Playwright to launch a browser, navigate to the target page, and dynamically injects a CAPTCHA solver.
- **Customizable Browser Context**: Sets browser options like headless mode, sandboxing, and disabling unnecessary features to optimize performance.
- **Responsive CAPTCHA Interaction**: Adjusts CAPTCHA display, clicks on it, and retrieves the response through repeated attempts if necessary.
- **Timeout and Retries**: Implements a retry loop with configurable timeouts, ensuring robust attempts to retrieve the CAPTCHA token.
- **Elapsed Time Tracking**: Logs and returns elapsed time for solving CAPTCHA, providing an efficiency metric.
- **Error Handling**: Returns detailed status messages on success or failure, allowing for straightforward integration and feedback.

---
#### 📹 Preview

![Preview](https://i.imgur.com/YI6RZ5P.gif)

---
### ❗ Disclaimers

- I am not responsible for anything that may happen, such as API Blocking, IP ban, etc.
- This was a quick project that was made for fun and personal use if you want to see further updates, star the repo & create an "issue" [here](https://github.com/sexfrance/Turnstile-Solver/issues/)

---

### 📜 ChangeLog

```diff
v0.0.1 ⋮ 21/10/2024
! Initial release

v0.0.2 ⋮ 10/28/2024
! Modified the script, page.html is now in the scripts, made it faster and less resource intensive, modified the sync logic and made an async version, implemented logmagix logging, added timer...
```

---

<p align="center">
  <img src="https://img.shields.io/github/license/sexfrance/Turnstile-Solver.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=IOTA"/>
  <img src="https://img.shields.io/github/stars/sexfrance/Turnstile-Solver.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=IOTA"/>
  <img src="https://img.shields.io/github/languages/top/sexfrance/Turnstile-Solver.svg?style=for-the-badge&labelColor=black&color=f429ff&logo=python"/>
</p>


Inspired by [Turnaround](https://github.com/Body-Alhoha/turnaround)
