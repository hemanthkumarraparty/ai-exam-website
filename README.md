# AI-Based Class Test Evaluation System

## Overview
The AI-Based Class Test Evaluation System is a web application developed to automate the evaluation of short descriptive answers in online class tests.

Traditional online exams mainly support multiple-choice questions, while descriptive answers still require manual evaluation by faculty members. This project solves that problem by allowing students to write answers in their own words and automatically evaluating them using semantic similarity techniques.

The system compares student answers with predefined model answers using Natural Language Processing (NLP) and assigns marks based on similarity scores.

---

## Problem Statement
Educational institutions can easily conduct MCQ-based exams online, but evaluating short descriptive answers remains a challenge because it requires manual correction.

Manual evaluation:
- Consumes time
- Requires significant faculty effort
- May lead to inconsistent grading

This project addresses these issues by automating the evaluation process.

---

## Objectives
- Automate descriptive answer evaluation
- Reduce manual correction effort
- Provide instant feedback
- Ensure consistent grading
- Create a simple online testing platform

---

## Features
- Online descriptive test system
- Countdown timer
- Auto submission when time expires
- AI-based answer evaluation
- Semantic similarity scoring
- Instant result generation
- Progress tracking
- Session persistence after refresh

---

## Technology Stack
### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### AI/NLP
- Sentence Transformers
- Cosine Similarity

### Data Processing
- Pandas

---

## System Workflow
1. Student starts the test
2. Questions are displayed
3. Timer starts automatically
4. Student submits answers
5. Backend processes the answer
6. SentenceTransformer converts answers into embeddings
7. Cosine similarity is calculated
8. Marks are assigned
9. Final grade is displayed

---

## Project Structure
ai-exam-website/
│
├── app.py  
├── requirements.txt  
├── ai_student_grading_dataset.csv  

├── templates/  
│   └── index.html  

└── static/  
    └── style.css  

---

## Future Enhancements
- Database integration
- User authentication
- Admin dashboard
- Multi-subject support
- Improved AI accuracy

---

## Conclusion
This project demonstrates how AI and NLP can be used to automate descriptive answer evaluation in educational institutions and reduce manual workload while maintaining fair grading.
