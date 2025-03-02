<p align="center">
  <img src="https://github.com/user-attachments/assets/3d5e525a-538e-4b55-8481-575d9485e5af" width="250" />
</p>

# Interface  

## Overview  
**Interface** is a privacy-preserving tool for interacting with cloud-hosted Large Language Models (LLMs). It ensures user data remains protected by leveraging an on-device Small Language Model (SLM) for initial queries.  

If the SLM cannot generate a satisfactory response, the query is automatically routed to a cloud-hosted LLM. However, before sending the query, all Personally Identifiable Information (PII) is replaced with synthetic data to maintain privacy. Once the response is received, the tool reverses this process, restoring the original information seamlessly.  

## Key Features  
- **On-Device Processing:** Provides a local SLM for handling queries without external data exposure.  
- **Intelligent Query Routing:** Automatically forwards complex queries to cloud LLMs only when necessary.  
- **Privacy Protection:** Anonymizes sensitive data before transmission and restores it upon response.  
- **Seamless Integration:** Ensures a smooth user experience without compromising security.  

## Why Use Interface?  
- Protects user privacy while leveraging powerful cloud-based AI models.  
- Reduces reliance on cloud resources, minimizing costs and latency.  
- Ensures sensitive data never leaves the local environment in an identifiable form.  

## Getting Started  
Follow the [installation instructions](#installation) to set up Interface on your system.  

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

4. **Install en_core_web_lg which is a pretrained english language model for tasks like semantic understanding and text classification**  
   - Run the following command:  
     ```sh
     python -m spacy download en_core_web_lg
     ```

5. **Run the Project**  
   - Start the project using:  
     ```sh
     python main.py
     ``` 

5. **Start Chatting**
   
   <br> <img width="1000" alt="image" src="https://github.com/user-attachments/assets/d53d40bf-9375-4e30-b9d8-e59164a8ad46" />


