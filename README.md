# Resume Builder with AI

The Resume Builder is a Python-based application that allows users to create and generate resumes using a graphical user interface (GUI). This project aims to simplify the process of creating professional resumes by providing an easy-to-use interface for entering personal information, education, work experience, skills, and projects. The generated resumes are created in LaTeX format and can be converted to PDF for easy sharing.

## Features

- **User-Friendly Interface**: The application provides a user-friendly interface for entering resume details.

- **Resume Sections**: Users can input information for various resume sections, including Personal Information, Education, Work Experience, Skills, and Projects.

- **LaTeX Output**: The application generates resumes in LaTeX format, which allows for high-quality typesetting and customization.

- **PDF Export**: Users can easily export their resumes to PDF format for easy sharing and printing.

## Prerequisites

Before running the Resume Builder, ensure that you have the following prerequisites installed:

- Python 3.x
- Required Python libraries (e.g., Tkinter, OpenAI, etc.)
- A LaTeX distribution (e.g., TeX Live, MiKTeX)

## Getting Started

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/prashantkumar82/resume-builder.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Install a LaTeX distribution (e.g., TeX Live or MiKTeX) and ensure that `pdflatex` is in your system's PATH (as explained in the [Installation](#installation) section).

4. Run the `main.py` script to start the Resume Builder application:
   ```bash
   python main.py
   ```

5. Follow the on-screen instructions to input your resume details.

6. Click the "Submit" button to generate your resume in LaTeX format.

7. Navigate to the `result` directory to find your generated LaTeX file (`Resume.tex`).

8. To convert the LaTeX file to a PDF, navigate to the `result` directory and run:
   ```bash
   cd result
   pdflatex -interaction=nonstopmode Resume.tex
   ```

9. Your resume PDF (`Resume.pdf`) will be generated in the same directory.

## Usage

- Enter your personal information, including full name, email, phone number, LinkedIn URL, and GitHub URL.

- Add your educational background, including university name, location, degree, GPA, time period, and relevant coursework.

- Input your work experience, specifying company name, location, role, time period, and a detailed job description.

- Add your skills, including languages, frameworks, and tools you are proficient in.

- Include information about your projects, specifying project name, time period, your role, GitHub link, and a brief project description.

- Click the "Submit" button to generate your resume in LaTeX format.

- Navigate to the `result` directory to find your generated LaTeX file (`Resume.tex`).

- To convert the LaTeX file to a PDF, run `pdflatex -interaction=nonstopmode Resume.tex` in the `result` directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to [OpenAI](https://www.openai.com/) for providing the GPT-3 model used for text summarization.
- Credits to the LaTeX community for LaTeX typesetting.

## Author

- Your Name prashantkumar82
- Contact: prashant721025@gmail.com
- GitHub: [github.com/prashantkumar82](https://github.com/prashantkumar82)

Feel free to modify this README file to fit the specifics of your project. Include any additional sections or details that you think would be helpful for users and contributors.
