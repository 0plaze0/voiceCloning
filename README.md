Here is the **`README.md`** file that provides all necessary instructions to set up the project, create a virtual environment, install dependencies, and run the script.

---

### `README.md`

```markdown
# Voice Cloning Script

This script allows you to clone a voice from a YouTube video or a local `.wav` file and synthesize custom text using the cloned voice. It uses [Coqui TTS](https://github.com/coqui-ai/TTS) for text-to-speech synthesis and [ffmpeg](https://ffmpeg.org/) for audio processing.

## Requirements

- Python 3.7+
- ffmpeg (system-wide installation)
- A working internet connection to download models and YouTube audio.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/voice-cloning.git
cd voice-cloning
```

### 2. Set Up a Virtual Environment

To keep the project dependencies isolated, it's recommended to use a virtual environment.

#### On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Install ffmpeg

**macOS (Homebrew)**:
```bash
brew install ffmpeg
```

**Ubuntu/Debian**:
```bash
sudo apt install ffmpeg
```

**Windows**:
- Download and install from [ffmpeg.org](https://ffmpeg.org/download.html).
- Add the `bin/` directory to your system’s PATH.

### 5. Run the Script

After setting up your environment and installing dependencies, you can run the voice cloning script.

#### Clone voice from YouTube video:

```bash
python voice_clone.py --url "https://www.youtube.com/watch?v=xyz" --duration 20 --text "Hello, I am a cloned voice!"
```

#### Clone voice from a local `.wav` file:

```bash
python voice_clone.py --reference path/to/your/reference.wav --text "This is a voice cloned from a local file."
```

### 6. Output

The cloned audio will be saved in the `audios/` directory with a name like `audio_20230423215638(clone).wav`.

### 7. Deactivate Virtual Environment

After running the script, deactivate the virtual environment:

```bash
deactivate
```

## Notes

- **ffmpeg** is used for audio processing. Make sure it's installed on your system (see installation instructions above).
- The script uses the **`your_tts`** model for voice cloning, which can be slow on CPU-based systems. If you have a compatible GPU, you can modify the script to enable CUDA by setting `use_cuda=True` in the script.
- The `audios/` folder is automatically created if it doesn't exist.
