# Foldable-App-Testing
Unfolding State Loss Issues in Foldable Mobile Devices
# Foldable Device Application Testing Framework

## Overview
This repository contains the artifacts for the research paper titled "Unfolding State Loss Issues in Foldable Mobile Devices" (ICSE '26, April 12-18, 2026, Rio de Janeiro, Brazil), which evaluates the performance and stability of 20 popular shopping applications and 52 applications from the Google Play Store selected after carefully reviewing thousands of consumer reviews and identifying apps with issues reported specifically by users of foldable devices, the Samsung Galaxy Z Fold4 during mode transitions (e.g., folded to unfolded states). The study uses automated testing with Appium, Java, Python, and TestNG to identify issues such as UI reconfigurations, performance degradation, and state loss.

## Project Goals
- Assess application behavior on foldable devices (Samsung Galaxy Z Fold4, Google Pixel Fold, Samsung Galaxy Z Flip6, Motorola Razr 2023).


## Prerequisites
- **Operating System**: Linux, macOS, or Windows 10/11.
- **Software**:
  - Java Development Kit (JDK) 11 or later.
  - Python 3.8+.
  - Node.js (for Appium server).
  - Appium (install via `npm install -g appium`).
  - TestNG (via Maven or manual setup).
  - Android SDK with UIAutomator2 driver.
- **Hardware**: Access to foldable devices listed above with Android 15.
- **Dependencies**: Install required libraries 
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AnonymusUser2025/Foldable-App-Testing.git
   cd Foldable-App-Testing
2. Install dependencies (download Node.js and use it to install Appium)
   ```bash
   node -v
   npm -v
   npm install -g appium
3. Set up Appium Server
   ```bash
   appium 
