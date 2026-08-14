<div align="center">
 
  <h2 align="center">Cloudflare - Turnstile Solver</h2>
  <p align="center">
A Python-based Turnstile solver using the patchright library, featuring multi-threaded execution, API integration, and support for different browsers. It solves CAPTCHAs quickly and efficiently, with customizable configurations and detailed logging.
    <br />
    <br />
    <a href="https://github.com/Theyka/Turnstile-Solver#-changelog">📜 ChangeLog</a>
    ·
    <a href="https://github.com/Theyka/Turnstile-Solver/issues">⚠️ Report Bug</a>
    ·
    <a href="https://github.com/Theyka/Turnstile-Solver/issues">💡 Request Feature</a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/LICENSE-CC%20BY%20NC%204.0-red?style=for-the-badge"/>
    <img src="https://img.shields.io/github/stars/Theyka/Turnstile-Solver.svg?style=for-the-badge&color=red"/>
    <img src="https://img.shields.io/github/issues/Theyka/Turnstile-Solver?style=for-the-badge&color=red"/>
    <a href="https://t.me/codarea">
     <img src="https://img.shields.io/badge/Telegram%20Channel-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
    </a>
  </p>
</div>

---

### 🎁 Donation

- **USDT (TRC20)**: ``TWXNQCnJESt6gxNMX5oHKwQzq4gsbdLNRh``
- **USDT (Arbitrum One)**: ``0xd8fd1e91c8af318a74a0810505f60ccca4ca0f8c``
- **BTC**: ``13iiMaYFpCfNdcyFycSdSVmD2yfQciD7AQ``
- **LTC**: ``LSrLQe2dfpDhGgVvDTRwW72fSyC9VsXp9g``

---

### ❓ Looking for a Cheap or Custom CAPTCHA Solution?
- Need cheap captcha solution as low as 0.1$ per 1k ? Contact me on Telegram:

  <a href="https://t.me/tlb_sh">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
  </a>

---

### ❗ Disclaimers
- I am not responsible for anything that may happen, such as API Blocking, IP ban, etc.
- This was a quick project that was made for fun and personal use if you want to see further updates, star the repo & create an "issue" [here](https://github.com/Theyka/Turnstile-Solver/issues/)

---

### ⚙️ Installation Instructions

1. **Ensure Python 3.9+ is installed** on your system. Python 3.8 is not supported.

2. **Create a Python virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Select the browser to install**:
   You can choose between **Chromium**, **Chrome**, **Edge** or **Camoufox**:
   - To install **Chromium**:
     ```bash
     python -m patchright install chromium
     ```
   - To install **Chrome**:
     - On **macOS/Windows**: [Click here](https://www.google.com/chrome/)  
     - On **Linux (Debian/Ubuntu-based)**:
       ```bash
       apt update
       wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
       apt install -y ./google-chrome-stable_current_amd64.deb
       apt -f install -y  # Fix dependencies if needed
       rm ./google-chrome-stable_current_amd64.deb
       ```
   - To install **Edge**:
     ```bash
     python -m patchright install msedge
     ```
   - To install **Camoufox**:
     ```bash
     python -m camoufox fetch
     ```

6. **Start testing**:
   - Run the script (Check [🔧 Command line arguments](#-command-line-arguments) for better setup):
     ```bash
     python api_solver.py
     ```
     
---

### 🔧 Command line arguments
| Parameter     | Default   | Type      | Description                                                                                   |
|--------------|-----------|-----------|-----------------------------------------------------------------------------------------------|
| `--headless`   | `False`  | `boolean` | Runs the browser in headless mode. Requires the `--useragent` argument to be set. Accepts `--headless`, `--headless True`, or `--headless False`. |
| `--useragent`  | `None`   | `string`  | Specifies a custom User-Agent string for the browser. (No need to set if camoufox used)                                        |
| `--debug`      | `False`  | `boolean` | Enables or disables debug mode for additional logging and troubleshooting. Accepts `--debug`, `--debug True`, or `--debug False`. |
| `--browser_type` | `chromium`  | `string` | Specify the browser type for the solver. Supported options: chromium, chrome, msedge, camoufox      |
| `--thread`     | `1`      | `integer` | Sets the number of browser threads to use in multi-threaded mode.                           |
| `--host`       | `127.0.0.1` | `string`  | Specifies the IP address the API solver runs on.                                            |
| `--port`       | `5000`   | `integer` | Sets the port the API solver listens on.                                                    |
| `--proxy`       | `False`   | `boolean` | Select a random proxy from proxies.txt for solving captchas. Accepts `--proxy`, `--proxy True`, or `--proxy False`. |

---

### 🐳 Docker Image
#### Running the Container
To start the container, use:
- Change the TZ environment variable and ports to the correct one for yourself:
```sh
docker run -d -p 3389:3389 -p 5000:5000 -e TZ=Asia/Baku --name turnstile_solver theyka/turnstile_solver:latest
```

#### Connecting to the Container
1. Use an **RDP client** (like Windows Remote Desktop, Remmina, or FreeRDP)
2. Connect to `localhost:3389`
3. Login with the default user:
   - **Username:** root
   - **Password:** root
4. After this, you can start the solver by navigating to the `Turnstile-Solver` folder.

---

### 📡 API Documentation
#### Solve turnstile
```http
  GET /turnstile?url=https://example.com&sitekey=0x4AAAAAAA
```
#### Request Parameters:
| Parameter  | Type    | Description                                                                 | Required |
|------------|---------|-----------------------------------------------------------------------------|----------|
| `url`      | string  | The target URL containing the CAPTCHA. (e.g., `https://example.com`) | Yes      |
| `sitekey`  | string  | The site key for the CAPTCHA to be solved. (e.g., `0x4AAAAAAA`) | Yes      |
| `action`   | string  | Action to trigger during CAPTCHA solving, e.g., `login`            | No       |
| `cdata`    | string  | Custom data that can be used for additional CAPTCHA parameters.    | No       |

#### Response:

If the request is successfully received, the server will respond with a `task_id` for the CAPTCHA solving task:

```json
{
  "task_id": "d2cbb257-9c37-4f9c-9bc7-1eaee72d96a8"
}
```

#### Get Result
```http
  GET /result?id=f0dbe75b-fa76-41ad-89aa-4d3a392040af
```

#### Request Parameters:

| Parameter  | Type    | Description                                                                 | Required |
|------------|---------|-----------------------------------------------------------------------------|----------|
| `id`       | string  | The unique task ID returned from the `/turnstile` request.                   | Yes      |

#### Response:

Pending tasks return HTTP 200:

```json
{
  "status": "pending",
  "value": "CAPTCHA_NOT_READY"
}
```

Successful solves return HTTP 200:

```json
{
  "status": "success",
  "elapsed_time": 7.625,
  "value": "0.KBtT-r"
}
```

Failed solves return HTTP 422:

```json
{
  "status": "error",
  "elapsed_time": 7.625,
  "value": "CAPTCHA_FAIL"
}
```

Cloudflare dummy sitekeys are useful for local API checks. The always-pass key is `1x00000000000000000000AA`; the always-block key is `2x00000000000000000000AB`.

---

### 🎉 Sponsor
<a href="https://dashboard.capsolver.com/passport/register?inviteCode=7_Dvkat0RVqc">
    <img src="https://github.com/user-attachments/assets/176d2a43-2d08-4aa6-bc9d-5e1eb5c3d1a4" alt="Description">
</a>

---

Inspired by [Turnaround](https://github.com/Body-Alhoha/turnaround)
Original code by [Theyka](https://github.com/Theyka/Turnstile-Solver)
Changes by [Sexfrance](https://github.com/sexfrance)
