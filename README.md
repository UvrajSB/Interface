<p align="center">
  <img src="https://github.com/user-attachments/assets/3d5e525a-538e-4b55-8481-575d9485e5af" width="250" />
</p>

# Steps to Run

1. **Install Requirements**  
   - Use the following command:  
     ```sh
     pip install -r requirements.txt
     ```

2. **Get a Free Gemini Key**  
   - Obtain a free API key from [Gemini Key](https://aistudio.google.com/app/apikey?_gl=1*10cf8pf*_ga*NTk3ODcwNzMuMTczODY1MDI4NQ..*_ga_P1DBVKWT6V*MTczOTQ4MTI1My40LjAuMTczOTQ4MTI1My42MC4wLjE4MTQ4NzU3MDI.)  
   - Add it as an environment variable:  
     ```sh
     export GEMINI_API_KEY=your_api_key_here
     ```

3. **Install deepseek-r1:1.5b**  
   - Run the following command:  
     ```sh
     ollama pull deepseek-r1:1.5b
     ```

4. **Run the Project**  
   - Start the project using:  
     ```sh
     python main.py
     ```

