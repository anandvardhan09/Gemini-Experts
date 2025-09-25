# Gemini Experts 🚀

A comprehensive multi-purpose web application powered by Google's Gemini AI that provides specialized AI-driven tools for various productivity tasks.

## 🌟 Live Demo
**App Link:** [https://geminiexperts.streamlit.app/](https://geminiexperts.streamlit.app/)

## 📋 Overview

Gemini Experts is a versatile Streamlit-based web application that combines multiple AI-powered tools into a single platform. Each "Expert" is designed to solve specific real-world problems using Google's Gemini AI capabilities.

## 🛠️ Features

### 1. 📄 ATS Expert
- **Purpose**: Analyzes resumes against job descriptions
- **Functionality**: 
  - Upload PDF resume and paste job description
  - Get percentage match score
  - Identify missing keywords
  - Receive profile improvement suggestions
- **Use Case**: Job seekers wanting to optimize their resumes for Applicant Tracking Systems

### 2. 🍎 Nutrition Expert
- **Purpose**: Analyzes food images for nutritional information
- **Functionality**:
  - Upload food images (JPG, JPEG, PNG)
  - Get detailed calorie breakdown
  - Item-wise nutritional analysis
- **Use Case**: Health-conscious individuals tracking their diet

### 3. 📚 PDF Expert (RAG System)
- **Purpose**: Chat with PDF documents using AI
- **Functionality**:
  - Upload multiple PDF files
  - Ask questions about PDF content
  - Get accurate, context-aware answers
  - Uses vector embeddings for intelligent search
- **Use Case**: Researchers, students, professionals working with large documents

### 4. 🎥 YouTube Transcripter
- **Purpose**: Convert YouTube videos to detailed notes
- **Functionality**:
  - Input YouTube video URL
  - Generate complete transcript
  - Create summarized notes (within 250 words)
  - Display video thumbnail
- **Use Case**: Content creators, students, researchers

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google API Key for Gemini AI

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gemini-experts.git
cd gemini-experts
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 4. Streamlit Secrets (for deployment)
Create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_google_gemini_api_key_here"
```

### 5. Run the Application
```bash
streamlit run main.py
```

## 📁 Project Structure

```
gemini-experts/
├── main.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── .env                           # Environment variables (local)
├── .streamlit/
│   └── secrets.toml               # Streamlit secrets (deployment)
└── Experts/
    ├── ats.py                     # ATS Expert functionality
    ├── nutritionExpert.py         # Nutrition Expert functionality
    ├── anyPdfExpert.py           # PDF Expert with RAG
    └── youtubeTranscripter.py    # YouTube Transcripter
```

## 🔧 Technical Implementation

### Core Technologies
- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro & Gemini 1.5 Pro
- **PDF Processing**: PyPDF2
- **Vector Database**: FAISS
- **Embeddings**: Google Generative AI Embeddings
- **Video Processing**: YouTube Transcript API
- **Image Processing**: PIL (Python Imaging Library)

### Key Components

#### ATS Expert (`ats.py`)
- Uses Gemini Pro for resume analysis
- JSON response parsing for structured output
- Percentage matching algorithm

#### Nutrition Expert (`nutritionExpert.py`)
- Gemini 1.5 Pro Vision for image analysis
- Multi-modal input processing (text + image)
- Structured calorie breakdown

#### PDF Expert (`anyPdfExpert.py`)
- Retrieval-Augmented Generation (RAG) implementation
- FAISS vector store for similarity search
- LangChain integration for question-answering
- Recursive text splitting for optimal chunking

#### YouTube Transcripter (`youtubeTranscripter.py`)
- YouTube Transcript API integration
- Gemini 1.5 Flash for summarization
- Video thumbnail display

## 🔑 Getting Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new project or select existing one
3. Generate API key
4. Add key to your environment variables

## 📦 Dependencies

```txt
streamlit              # Web framework
PyPDF2                # PDF processing
google.generativeai    # Gemini AI integration
python-dotenv          # Environment variables
youtube_transcript_api # YouTube transcript extraction
pathlib               # Path handling
langchain             # LLM framework
pdf2image             # PDF to image conversion
faiss-cpu             # Vector similarity search
langchain_google_genai # Google AI integration for LangChain
chromadb              # Vector database
langchain-community   # Community LangChain components
```

## 🚀 Deployment

### Streamlit Cloud Deployment
1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Add `GOOGLE_API_KEY` to Streamlit secrets
4. Deploy application

### Local Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GOOGLE_API_KEY="your_api_key"

# Run application
streamlit run main.py
```

## 🎯 Use Cases

- **Job Seekers**: Optimize resumes with ATS Expert
- **Health Enthusiasts**: Track nutrition with Nutrition Expert
- **Researchers**: Extract insights from documents with PDF Expert
- **Content Creators**: Summarize videos with YouTube Transcripter
- **Students**: Study materials analysis and note-taking

## 🛡️ Security Considerations

- API keys stored in environment variables
- No sensitive data stored in code
- Secure file handling for uploads
- Input validation for all user inputs


## 🙏 Acknowledgments

- Streamlit team for excellent web framework
- LangChain community for RAG implementations

