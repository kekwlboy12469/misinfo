# 🛡️ Misinformation Detection Browser Extension

**Team:** Code-benders  
**Team Members :** Nitish kumar,  Rupesh Ranjan Shetty , Akshat Singh ,  Madhvi 
**Project:** AI-powered tool for detecting misinformation and educating users on credible content

---

## 💡 The Idea

Misinformation spreads faster than truth. We developed a browser extension powered by **Gemini 1.5 Flash** that analyzes articles, posts, and headlines in real time, providing instant credibility assessment to help users navigate the internet with confidence.

## ⚡️ Key Features

- **🎯 Real-time Analysis**: Instant credibility scoring of web content
- **📊 Credibility Classification**: Content rated as Trusted/Questionable/Fake
- **🧠 AI-Driven Reasoning**: Transparent explanations for each assessment
- **💬 Interactive Chatbot**: Deep-dive exploration of content credibility
- **🔒 Privacy-First**: Analysis done without compromising user data
- **🌐 Seamless Integration**: Works directly within your browsing experience

---

## 🏗️ Architecture Overview

### Backend Layer
- **Flask** - Lightweight Python web framework
- **Flask-CORS** - Cross-origin request handling

### AI/GenAI Layer  
- **Google Generative AI SDK** - Gemini 1.5 Flash integration
- **Multimodal Processing** - Text and image analysis capabilities

### Image Processing
- **Pillow (PIL)** - Image processing and format conversion
- **OpenCV** - Advanced computer vision tasks
- **NumPy** - Array and tensor operations

### Networking & Data
- **Requests** - HTTP API calls
- **JSON** - Structured data exchange

---

## 📋 Prerequisites

Before installation, ensure you have:

- **Python 3.8+** installed on your system
- **Google Chrome** or **Chromium-based browser**
- **Google AI Studio API Key** (for Gemini access)
- **Git** for cloning the repository

---

## 🚀 Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/kekwlboy12469/misinfo.git
cd misinfo
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# If requirements.txt doesn't exist, install manually:
pip install flask flask-cors google-generativeai pillow opencv-python numpy requests
```

### Step 4: Configure API Keys

1. **Get Google AI Studio API Key:**
   - Go to [Google AI Studio](https://makersuite.google.com/)
   - Create a new project or select existing one
   - Generate an API key for Gemini access

2. **Create Environment Configuration:**
   ```bash
   # Create .env file in project root
   touch .env
   ```

3. **Add your API key to .env:**
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   FLASK_DEBUG=True
   FLASK_PORT=5000
   ```

### Step 5: Start the Backend Server

```bash
# Make sure you're in the project directory and virtual environment is active
python app.py

# Server should start at http://localhost:5000
```

### Step 6: Install Browser Extension

#### For Chrome/Chromium Browsers:

1. **Open Chrome Extension Management:**
   - Go to `chrome://extensions/`
   - Enable "Developer mode" (toggle in top-right)

2. **Load Extension:**
   - Click "Load unpacked"
   - Select the `extension` folder from your cloned repository
   - The extension should now appear in your extensions list

3. **Pin Extension:**
   - Click the puzzle piece icon in Chrome toolbar
   - Find "Misinformation Detector" and pin it

#### For Firefox (if supported):

1. **Open Firefox Add-on Management:**
   - Go to `about:debugging`
   - Click "This Firefox"

2. **Load Extension:**
   - Click "Load Temporary Add-on"
   - Select the `manifest.json` file from the extension folder

---

## 🔧 Configuration

### Backend Configuration

Edit `config.py` or environment variables:

```python
# Server settings
HOST = '127.0.0.1'
PORT = 5000
DEBUG = True

# AI Model settings
GEMINI_MODEL = 'gemini-1.5-flash'
MAX_TOKENS = 1000
TEMPERATURE = 0.7
```

### Extension Configuration

Edit `extension/config.js`:

```javascript
const CONFIG = {
    API_ENDPOINT: 'http://localhost:5000',
    TIMEOUT: 10000,
    MAX_CONTENT_LENGTH: 5000
};
```

---

## 🎯 How to Use

### 1. **Automatic Analysis**
   - Browse any website normally
   - Extension automatically analyzes content
   - Credibility score appears as a badge

### 2. **Manual Check**
   - Select text on any webpage
   - Click the extension icon
   - Get instant credibility assessment

### 3. **Deep Analysis**
   - Click "Analyze Full Page"
   - Get comprehensive content evaluation
   - Access reasoning explanations

### 4. **Interactive Chat**
   - Use built-in chatbot for questions
   - Get context about credibility factors
   - Learn about misinformation patterns

---

## 🧪 Testing the Installation

### Test Backend Server:

```bash
# Test API endpoint
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "Test article content", "url": "https://example.com"}'
```

### Test Extension:
1. Visit a news website
2. Click the extension icon
3. Verify credibility score appears
4. Test chatbot functionality

---

## 📁 Project Structure

```
misinfo/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
├── config.py             # Configuration settings
├── models/               # AI model integration
│   ├── gemini_client.py  # Gemini API wrapper
│   └── analyzer.py       # Content analysis logic
├── extension/            # Browser extension files
│   ├── manifest.json     # Extension configuration
│   ├── popup.html        # Extension popup UI
│   ├── popup.js          # Popup functionality
│   ├── content.js        # Content script
│   ├── background.js     # Background script
│   └── styles.css        # Extension styling
├── static/               # Web assets
└── templates/            # HTML templates
```

---

## 🛠️ Troubleshooting

### Common Issues:

**1. Extension Not Loading:**
- Ensure manifest.json is valid
- Check browser console for errors
- Verify all required files exist

**2. Backend Connection Issues:**
- Confirm Flask server is running on correct port
- Check CORS configuration
- Verify API endpoints in extension config

**3. API Key Problems:**
- Validate Google AI Studio API key
- Check .env file configuration
- Ensure API key has proper permissions

**4. Content Not Analyzing:**
- Check network requests in browser dev tools
- Verify content length limits
- Review server logs for errors

### Debug Mode:

```bash
# Run backend in debug mode
export FLASK_DEBUG=1
python app.py

# Check extension console
# Right-click extension icon → Inspect popup
```

---

## 🔄 Updates and Maintenance

### Updating the Extension:
1. Pull latest changes: `git pull origin main`
2. Restart backend server
3. Reload extension in browser: `chrome://extensions/` → Reload

### Updating Dependencies:
```bash
pip install --upgrade -r requirements.txt
```

---

## 🌟 Features Showcase

### AI-Driven Accuracy
- **Credibility Scoring**: 0-100 scale with detailed breakdowns
- **Content Classification**: Clear Trusted/Questionable/Fake labels
- **Multi-factor Analysis**: Source credibility, content quality, factual accuracy

### Intuitive User Experience
- **One-Click Analysis**: Simple extension popup interface
- **Visual Indicators**: Color-coded credibility badges
- **Interactive Elements**: Expandable reasoning sections

### Actionable Intelligence
- **Detailed Explanations**: Why content received its score
- **Source Verification**: Publisher reputation analysis
- **Context Awareness**: Related fact-checks and references

---

## 📈 Innovation & Impact

### What Makes It Unique:
- **Real-time Processing**: Instant analysis without page refresh
- **Educational Approach**: Teaches users to identify misinformation
- **Privacy-Focused**: No personal data collection
- **Transparent AI**: Explainable reasoning for all decisions

### Real-World Impact:
- Reduces misinformation spread
- Improves digital literacy
- Enhances informed decision-making
- Builds critical thinking skills

---

## 🚀 Scalability & Future Scope

### Immediate Enhancements:
- Multi-language support
- Mobile app development
- Social media platform integration
- Collaborative fact-checking features

### Long-term Vision:
- Educational institution partnerships
- News organization integration
- Government advisory deployment
- Global misinformation tracking

---

## 👥 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit pull request

---

## 📞 Support

### Team Contact:
- **Email**: nitshkumar44470@gmail.com  
- **Repository**: https://github.com/kekwlboy12469/misinfo
- **Issues**: Open GitHub issues for bug reports

### Getting Help:
1. Check troubleshooting section above
2. Review GitHub issues
3. Contact team via repository

---

## 🏆 Hackathon Submission

**Event**: GenAI Exchange Hackathon  
**Problem Statement**: Build an AI-powered tool that detects potential misinformation and educates users on identifying credible, trustworthy content.

**Mentorship Support**: Technical and strategic guidance received from hackathon mentors for AI integration and user experience optimization.

---

*Built with ❤️ by Code-benders team during GenAI Exchange Hackathon*
