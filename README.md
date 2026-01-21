# Cold Email Generation Tool using AI

An AI-powered automation system that generates personalized cold outreach emails by extracting job postings from company career pages, matching job requirements with portfolio projects, and generating tailored email content using large language models.

---

## Project Overview

This project implements an **end-to-end AI automation pipeline** for cold email generation. It integrates web scraping, natural language processing, semantic matching, and LLM-based content generation into a single interactive web application.

The system significantly reduces manual effort involved in writing customized cold emails while maintaining professional tone and relevance.

---

## Business Problem

Job seekers and professionals often spend significant time manually drafting personalized cold emails for job applications and outreach. This process is repetitive, time-consuming, and prone to inconsistency.

### Key Challenges:

- Manual job description reading  
- Repetitive email writing  
- Poor personalization quality  
- Low outreach efficiency  

### Solution:

Automate the entire cold email generation process using AI by extracting job requirements, matching relevant portfolio projects, and generating professional personalized emails.

---

## Solution Architecture
<img width="326" height="456" alt="image" src="https://github.com/user-attachments/assets/27ec8bc4-637e-4721-8451-fcdc92ff1d89" />


---

## Core Functional Components

The application is built using the following modular components:

- **Web Scraper Module**
  - Extracts job page content from URLs

- **Text Cleaning Module**
  - Removes noise, HTML tags, and unwanted characters

- **LLM Processing Module**
  - Extracts job information
  - Generates personalized emails

- **Portfolio Matching Module**
  - Matches required skills with portfolio links

- **Streamlit UI Module**
  - Provides real-time interactive web interface

---

## Technology Stack

### Programming Language
- Python

### Frameworks and Libraries

- Streamlit (Web Interface)  
- LangChain (LLM orchestration)  
- Groq API (LLM inference engine)  
- Regular Expressions (Text preprocessing)  
- dotenv (Environment variable management)  

### AI Model Used

- LLaMA 3 (70B parameter model via Groq)

---
## Data Processing and NLP Pipeline

The system performs multiple natural language processing steps to convert raw job web pages into structured and usable information:

### Text Cleaning

Raw scraped content is cleaned using regular expressions to:

- Remove HTML tags  
- Remove URLs and web artifacts  
- Remove special characters  
- Normalize whitespace  

This ensures clean and consistent text input for the language model.

---

## Job Extraction using Large Language Models

LangChain is used to prompt the LLM to extract structured job information from scraped content.

The extracted job data includes:

- Job role  
- Required experience  
- Required skills  
- Job description  

The output is returned in JSON format for downstream processing.

This enables automatic conversion of unstructured job postings into structured data.

---

## Semantic Portfolio Matching

The portfolio module matches job-required skills with relevant project links.

This allows the system to:

- Automatically select relevant portfolio projects  
- Maintain personalization in cold emails  
- Improve recruiter engagement  

This step simulates semantic matching between job requirements and candidate experience.

---

## Cold Email Generation Pipeline

The system uses prompt engineering to generate personalized outreach emails.

The email generation logic ensures:

- Professional tone  
- Individual candidate voice (not agency style)  
- Clear skill alignment  
- Inclusion of relevant portfolio links  
- Human-like natural language output  

Each email is dynamically generated based on the extracted job information.

---

## Interactive Streamlit Web Interface

A user-friendly web interface is built using Streamlit that allows:

- Input of job posting URL  
- One-click email generation  
- Real-time output display  
- Error handling and feedback  

This enables easy usage without requiring command-line interaction.

---
## System Benefits and Impact

This automation system significantly improves productivity and outreach efficiency.

### Key Benefits

- Reduces manual email writing effort by over 70%  
- Improves email personalization quality  
- Ensures consistent professional tone  
- Accelerates job outreach process  
- Minimizes repetitive manual work  

---

## Project Structure
<img width="623" height="317" alt="image" src="https://github.com/user-attachments/assets/27bf58fd-459f-49df-953e-a8873353ae83" />


---

## How To Run The Project

### Step 1: Clone Repository

git clone https://github.com/your-username/cold-email-generator.git


---

### Step 2: Install Dependencies


---

### Step 3: Configure Environment Variables

Create a `.env` file in the root directory and add:

groq_api_key=YOUR_GROQ_API_KEY

---

### Step 4: Run Streamlit Application

streamlit run app.py

---

### Step 5: Use The Application

1. Enter a company career page URL  
2. Click the Submit button  
3. View generated personalized cold email  
4. Copy and use the email for outreach  

---

##  Project Summary
Cold Email Generator | Nov 2025
Python, LangChain, NLP, Streamlit

• Designed end-to-end AI automation pipeline for personalized cold email generation.
• Integrated semantic matching between job skills and portfolio data.
• Reduced manual email drafting effort by over 70% through automated content generation pipeline.
• Deployed web-based UI using Streamlit for real-time interaction and output generation.


---

## Future Enhancements

Planned improvements include:

- Vector database integration (FAISS / Pinecone)  
- Resume parsing integration  
- Multi-language email generation  
- Email tone customization (formal / casual / aggressive outreach)  
- Email sending automation using SMTP or APIs  
- Analytics dashboard for outreach performance  

---

## Author

Satyam Kumar  
Data Analytics and AI Automation Enthusiast  

---

## License

This project is intended for educational and portfolio demonstration purposes.


