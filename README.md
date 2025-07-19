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
4. Connect devices via USB. To check if the devices are connected, use
 ```bash
    adb devices
```
## Usage
1. Edit config/devices.json with your device details
2. Run test. (e.g. To run test on Best Buy)
   ``` bash
   python scripts/test_bestbuy.py
3. View results in data/logs and data/ui_dumps/. directory

## Directory Structure 
•  scripts/: Test files (e.g., FoldableTest.java, test_bestbuy.py).
•  config/: Configuration files (devices.json, testng.xml).
•  data/: Logs, UI hierarchy XML dumps, and analysis results.
•  pom.xml: Maven build file for Java.

## Device configuration for Test activity
---

## config/devices.json
Device configurations for test execution.

```json
{
  "devices": [
    {
      "deviceName": "Samsung Galaxy Z Fold4",
      "platformVersion": "14",
      "appPackage": "com.bestbuy.android",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Samsung Galaxy Z Flip6",
      "platformVersion": "14",
      "appPackage": "com.bestbuy.android",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Google Pixel 9 Pro Fold",
      "platformVersion": "14",
      "appPackage": "com.aliexpress.app",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Motorola Razr 2023",
      "platformVersion": "13",
      "appPackage": "com.temu.app",
      "appActivity": ".MainActivity"
    }
  ]
}
```
## pom.xml
Maven configuration setup for Java/TestNG
``` XML
---

config/devices.json
Device configurations for test execution.
```
```json
{
  "devices": [
    {
      "deviceName": "Samsung Galaxy Z Fold4",
      "platformVersion": "14",
      "appPackage": "com.bestbuy.android",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Samsung Galaxy Z Flip6",
      "platformVersion": "14",
      "appPackage": "com.bestbuy.android",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Google Pixel 9 Pro Fold",
      "platformVersion": "14",
      "appPackage": "com.aliexpress.app",
      "appActivity": ".MainActivity"
    },
    {
      "deviceName": "Motorola Razr 2023",
      "platformVersion": "13",
      "appPackage": "com.temu.app",
      "appActivity": ".MainActivity"
    }
  ]
}
```
## testng.xml
TestNG suite Configuration
```XML
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="FoldableTestSuite" parallel="tests" thread-count="2">
    <test name="BestBuyTest">
        <parameter name="deviceName" value="Samsung Galaxy Z Flip6"/>
        <parameter name="appPackage" value="com.bestbuy.android"/>
        <parameter name="appActivity" value=".MainActivity"/>
        <classes>
            <class name="com.foldable.testing.FoldableTest"/>
        </classes>
    </test>
    <test name="AliExpressTest">
        <parameter name="deviceName" value="Motorola Razr 2023"/>
        <parameter name="appPackage" value="com.aliexpress.app"/>
        <parameter name="appActivity" value=".MainActivity"/>
        <classes>
            <class name="com.foldable.testing.FoldableTest"/>
        </classes>
    </test>
</suite>
```
## Results
Sample analysis output
```MARKDOWN
# Analysis Results

## Best Buy on Samsung Galaxy Z Flip6
- **Pre-Unfold UI Dump**: Elements aligned, no overlap.
- **Post-Unfold UI Dump**: Button "Add to Cart" shifted 50px right, text size increased from 14sp to 18sp.
- **Issues**: Loss of relative position, no crash.

## AliExpress on Motorola Razr 2023
- **Pre-Unfold UI Dump**: Navigation menu visible on cover.
- **Post-Unfold UI Dump**: Menu clipped, lag of 2.3s.
- **Issues**: Resize error, I/O lag.
```
