# GitHelper

## Recent changes
#### 2025-31-01 – Improved project initialization flow
I was working on a friend's project and noticed he needed some help with github. After a bit of troubleshooting, I decided to simplify the setup and made these major changes

```bash

- Replaced simple `git init` with guided setup wizard (menu option 3)  
- Now handles: repository init, initial commit, remote origin setup, and optional first push  
- Cleaner onboarding for new projects – fewer manual steps required

```  

[![GitHelper Screenshot](banner.JPG)](https://githelper.pages.dev)


## About

GitHelper is a Python-based application that provides a nostalgic, retro-computing inspired interface for managing Git repositories. It simplifies common Git operations into an intuitive menu system, making version control more accessible and visually engaging.

## Features

- Visual menu-based interface for Git commands
- Support for all essential Git operations
- GitHub/GitLab/Bitbucket integration
- Quick-commit functionality
- Branch management
- Repository status visualization

## Installation

```bash
# Clone the repository
git clone https://github.com/paolowu5/githelper.git

# Navigate to directory
cd githelper

# Install dependencies
pip install -r requirements.txt

# Run GitHelper
python githelper.py
```

## Usage

GitHelper presents a simple menu interface for common Git operations:

1. Repository status (git status)
2. View commit history (git log)
3. Initialize repository (git init)
4. Manage remote origin (git remote)
5. Manage branches (git branch)
6. Add all files (git add .)
7. Create commit (git commit)
8. Push code (git push)
9. Quick update (add, commit, push)

## Requirements

- Python 3.6+
- Git (installed and in PATH)
- Required Python packages (see requirements.txt)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by retro computing interfaces of the 80s and 90s
- Thanks to all contributors who have helped shape this project

---

Created by [Paolo Allegretti](https://paoloallegretti.com)
