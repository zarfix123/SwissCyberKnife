# CyberSecurity Swiss Army Tool

<div align="center">

  ![GitHub Last Commit](https://img.shields.io/github/last-commit/zarfix123/SwissCyberKnife)
  ![GitHub](https://shields.io/github/license/zarfix123/SwissCyberKnife)
  
  ![Cool Logo hehe](src/extra/image.webp)

</div>


## Description

***SwissCyberKnife is a multi-functional cybersecurity toolkit that combines a variety of tools commonly used in cybersecurity and penetration testing. This toolkit includes tools for port scanning, IP lookup, password generation, encryption/decryption, and password strength analysis.***

## Installation

### Option 1: Using a Virtual Environment (Recommended)

Using a virtual environment is recommended, especially if you have other Python projects or need to manage dependencies separately.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zarfix123/SwissCyberKnife.git
    cd SwissCyberKnife
    ```

2. **Set up a virtual environment**:
    - For Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - For Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. **Install dependencies and the project**:
    ```bash
    pip install -e .
    ```
4. **Set Up ```rockyou.txt``` wordlist:**
   - **Option A: Automated Download (recommended):**
    ```bash
    curl -L https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt -o src/extra/rockyou.txt
    ```
    This command downloads ```rockyou.txt``` directly to the required directory

   - **Option B: Using Git-LFS**: You can also fetch ```rockyou.txt``` with git-lfs:
    ```bash
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    sudo apt-get install git-lfs
    git lfs fetch src/extra/rockyou.txt
    ```
   - **Option C: Manual Download**: Download ```rockyou.txt``` from [here](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) and place it into:
    ```plaintext
    src/extra/rockyou.txt
    ```


### Option 2: Installing Directly Without a Virtual Environment

If you prefer not to use a virtual environment, you can install the project and its dependencies directly in your Python environment. This is a good option if you have no conflicting dependencies with other projects.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zarfix123/SwissCyberKnife.git
    cd SwissCyberKnife
    ```

2. **Install dependencies and the project directly**:
    ```bash
    pip install -e .
    ```
3. **Download and place** ```rockyou.txt```:

     Follow the steps under Option 1, step 4 to set up ```rockyou.txt``` in the required directory.


