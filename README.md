#  Gesture Controlled LED Brightness using ESP32 & Python

Control LED brightness in real-time using hand gestures 🤯
This project uses **Computer Vision + IoT** to adjust LED brightness based on the distance between your fingers.

---

## 🚀 Features

* ✋ Hand gesture detection using Python (OpenCV + MediaPipe)
* 📏 Real-time finger distance measurement
* 💡 Smooth LED brightness control (PWM)
* 🌐 Wireless communication with ESP32 (WiFi)
* ⚡ Low-latency and smooth transitions

---

## 🧠 How It Works

1. Webcam captures your hand
2. Detects thumb and index finger positions
3. Calculates distance between fingers
4. Maps distance to brightness (0–255)
5. Sends value to ESP32 via WiFi
6. ESP32 adjusts LED brightness using PWM

---

## 🛠️ Tech Stack

* Python (OpenCV, MediaPipe)
* ESP32 (Arduino framework)
* WiFi Communication (Socket Programming)

---

## 🔌 Hardware Required

* ESP32
* LED
* 220Ω Resistor
* Breadboard & Jumper wires
* Laptop with webcam

---

## ⚡ Circuit Diagram

ESP32 GPIO 27 → Resistor → LED (+)
LED (–) → GND

---

## 💻 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gourab354/air-dimmer.git
 cd air-dimmer
```

---

### 2️⃣ Install Python dependencies

```bash
pip install opencv-python mediapipe
```

---

### 3️⃣ Upload ESP32 Code

* Open `.ino` file in Arduino IDE
* Select board: **ESP32 Dev Module**
* Select correct COM port
* Upload code

---

### 4️⃣ Update IP Address

* Open Serial Monitor after uploading
* Copy ESP32 IP address
* Paste it inside Python file:

```python
ESP32_IP = "192.168.x.x"
```

---

### 5️⃣ Run Python Script

```bash
python main.py
```

---

## 🎮 Usage

* Bring thumb and index finger close → LED dims 💡⬇️
* Move fingers apart → LED brightens 💡⬆️

---

## 🧪 Example Output

| Finger Distance | LED Brightness |
| --------------- | -------------- |
| Close           | Low            |
| Medium          | Medium         |
| Far             | High           |

---

## ⚠️ Troubleshooting

* ❌ ESP32 not responding → Check IP address
* ❌ LED not glowing → Check wiring
* ❌ Flickering → Ensure smoothing code is present
* ❌ Compilation error → Select correct ESP32 board

---

## 🚀 Future Improvements

* 🎮 Gesture ON/OFF control
* 🌈 RGB LED control using multiple fingers
* 📱 Mobile app integration
* 🤖 Integration with AI assistant projects

---

## 🤝 Contributing

Feel free to fork this repo and improve it!
Pull requests are welcome 🚀

---

## 📜 License

This project is open-source and free to use.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Gourab**
Electronics & Hardware Enthusiast ⚡
