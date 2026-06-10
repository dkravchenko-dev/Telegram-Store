<div align="center">

# 🛒 Telegram Store

**Automated Digital Goods Store in Telegram**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)](https://docs.aiogram.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Description](#description) • [Features](#features) • [Tech Stack](#tech-stack) • [Installation](#installation) • [Configuration](#configuration)

---

</div>

## Description

**Telegram Store** is a Python-based Telegram bot built with the [aiogram](https://docs.aiogram.dev/) framework, designed to set up a fully automated digital goods store. The bot allows you to sell configuration files and other digital products for real money, featuring distinct access levels for standard users and administrators.

### Key Features

- **Full Automation** of digital product sales within Telegram
- **Built-in Payment Gateway** for seamless payment processing
- **Admin Dashboard** for comprehensive product and user management
- **Subscription System** with flexible renewal options
- **Robust Security** and granular access control
- **Intuitive Interface** optimized for a smooth user experience

---

## Demo

<video src="https://github.com/user-attachments/assets/e214934d-8b9b-49dc-aaaf-d3dff49f6774" controls width="600">
Your browser does not support the video tag. Download it <a href="assets/demonstration.mp4">here</a>.
</video>

---

## Features

### Standard Users

<div align="center">

| Feature | Description |
|:--------|:---------|
| **Service Overview** | View general information about the platform and setup guides |
| **Product Catalog** | Browse available items along with their descriptions and prices |
| **Purchase Items** | Buy the desired quantity of digital goods instantly |
| **Subscription Management** | Extend or purchase additional subscription tiers as needed |
| **Profile & History** | Manage personal account details and review purchase history |

</div>

### Administrators

<div align="center">

| Feature | Description |
|:--------|:---------|
| **Product Management** | Add, remove, and update digital goods |
| **User Administration** | View all registered users and track their orders |
| **Payment Verification** | Validate and confirm user payment statuses |
| **User Banning** | One-click user restriction in case of violations or fraudulent activity |
| **Financial Tracking** | Monitor and manage the store's revenue stream |
| **Broadcast Notifications** | Send bulk announcements and direct messages to users |

</div>

---

## Why Choose This Bot

- **Sales Automation:** Eliminates manual processing by completely automating the transaction pipeline within Telegram.
- **Simplified Management:** Streamlines how you organize your product listings and handle active subscriptions.
- **Enhanced Security:** Offers instant payment status monitoring to protect both the seller and the consumer.
- **Role Separation:** Enforces a clean division of privileges between customers and system administrators.

---

## Tech Stack

<div align="center">

| Technology | Version | Purpose |
|:----------|:-------|:-----------|
| **Python** | 3.11+ | Core programming language |
| **aiogram** | 3.x | Asynchronous framework for the Telegram Bot API |
| **JSON** | - | Local file-based storage for user data profiles |
| **Payment Gateway** | - | Custom integration for handling digital product transactions |

</div>

---

## Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Setup Steps

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Telegram-Store
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # or
   .venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   For **Linux**:
   ```bash
   pip install -r requirements_linux.txt
   ```

   For **macOS**:
   ```bash
   pip install -r requirements_mac.txt
   ```

---

## Configuration

### Obtaining a Bot Token

1. Find [@BotFather](https://t.me/BotFather) on Telegram.
2. Send the `/newbot` command.
3. Follow the instructions to configure your bot's name and username.
4. Copy the generated API token.

### Configuration Settings

Open `app/config.py` and populate the required parameters:

```python
TOKEN_BOT_USERS = "YOUR_BOT_TOKEN_HERE"  # Your Telegram bot token
ID_ADMIN = 123456789  # Your personal Telegram ID (retrieve via @userinfobot)
SUPPORT_PROFILE = "@your_support_username"  # Telegram handle for customer support
```

### Data Structure

Ensure that the `database/users.json` file is present. The bot will automatically initialize the required JSON structure on its initial run if it doesn't exist.

---

## Running the Bot

### Standard Launch

```bash
python main.py
```

### Running in the Background (Linux/macOS)

```bash
chmod +x start.sh
./start.sh
```

The `start.sh` script automatically handles the following:
- Terminates any previously running instance of the bot
- Activates the virtual environment
- Launches the bot execution process in the background
- Pipes all runtime logs into `output.log`

---

## Project Structure

```
Telegram-Store/
├── app/
│   ├── config.py              # Bot configuration settings
│   ├── router.py              # Handler routing layer
│   ├── handlers/              # Command and message handlers
│   │   ├── start.py           # /start command handler
│   │   ├── admin.py           # Administrative tools
│   │   ├── home.py            # Main navigation menu
│   │   ├── subscribe.py       # Subscription pathways
│   │   ├── subscription.py    # Subscription management
│   │   ├── extension.py       # Subscription renewal workflows
│   │   ├── settings.py        # Application settings
│   │   ├── edit.py            # Product updates
│   │   ├── add.py             # Product creation
│   │   ├── remove.py          # Product deletion
│   │   ├── description.py     # Product description templates
│   │   └── instruction.py     # Guide templates
│   ├── keyboards/             # Inline and reply UI keyboards
│   │   ├── admin_panel.py
│   │   ├── buy_configs.py
│   │   ├── edit_configs.py
│   │   ├── remove_configs.py
│   │   ├── subscription_form.py
│   │   └── ...
│   ├── services/              # Core business logic
│   │   ├── payments/          # Payment pipeline integrations
│   │   │   ├── add.py
│   │   │   ├── buy.py
│   │   │   └── renewal.py
│   │   ├── form_payment.py
│   │   ├── move_files.py
│   │   └── remove.py
│   ├── texts/                 # Static text copy and templates
│   │   ├── buttons.py
│   │   └── templates.py
│   └── img/                   # Graphic assets for instructions
│       ├── android/
│       ├── ios/
│       ├── windows/
│       └── mac os/
├── database/
│   ├── users.json             # Flat-file user database
│   ├── users_manager.py       # Database abstraction manager
│   └── configs/               # System configuration assets
│       ├── conf/              # .conf files
│       ├── png/               # Generated QR codes
│       ├── vless.txt          # VLESS configurations
│       └── creation_qr.py
├── main.py                    # Application entry point
├── requirements_linux.txt     # Linux environment dependencies
├── requirements_mac.txt       # macOS environment dependencies
├── start.sh                   # Process management script
└── README.md                  # System documentation
```

---

## Security

- **Never expose or commit** the `app/config.py` file containing active production tokens.
- Ensure `app/config.py` is safely appended to your `.gitignore` file.
- Manage sensitive tokens using system environment variables or secure vault secrets.
- Periodically inspect execution logs to monitor for unauthorized or anomalous activity.

---

## Support

If you encounter any issues or have inquiries:

1. Browse the repository's open/closed Issues to check if your problem has already been addressed.
2. Open a new Issue detailing your bug report or feature request.
3. Reach out to the support desk directly using the `SUPPORT_PROFILE` handle specified in your configuration.

---

## License

This project is open-source software licensed under the MIT License. For more information, please refer to the `LICENSE` file.

---

<div align="center">

**Built with ❤️ to streamline and automate your sales workflow**

⭐ If this repository helped you, consider giving it a star!

</div>
```
