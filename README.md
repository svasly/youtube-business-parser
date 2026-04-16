# YouTube Business Channel Scraper & Processor

Automated toolset to search, filter, and categorize YouTube channels within specific niches (e.g., Law, Real Estate, Finance). Built with Python and YouTube Data API v3.

## 🚀 Features
- **Smart Search:** Deep-parsing using multiple keywords and pagination (collects 1000+ results).
- **Activity Filter:** Automatically filters out channels that haven't posted in the last 4 months.
- **Geo-Targeting:** Focused on the Russian-speaking market and RU region.
- **Data Processing:** Includes a dedicated script to clean data and remove specific sub-niches (e.g., removing "accounting" from "legal" results).
- **Secure Configuration:** Uses environment variables to keep API keys safe.

## 🛠 Tech Stack
- **Python 3.12**
- **Pandas** (Data manipulation)
- **Google API Client** (YouTube Data API v3)
- **Python-dotenv** (Environment management)
- **Openpyxl** (Excel export)

## 📁 Project Structure
- `parcer.py`: The main scraping engine that connects to YouTube API.
- `split_base.py`: Post-processing script to clean results and split them into separate Excel files.
- `.env.example`: Template for your API credentials.
- `requirements.txt`: List of required Python libraries.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd youtube-business-parser
