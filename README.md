# Disaster Management Tracker (Final)

## Features
- Login page (username: admin, password: 1234)
- Map with real-time team markers
- Chennai (10), Madurai (5), Coimbatore (5), Trichy (5), Rajapalayam (2)
- Every team contact: Karuppasamy (Phone: 9345583758)

## Setup
1. Create virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac
   ```

2. Install requirements
   ```
   pip install -r requirements.txt
   ```

3. Run backend
   ```
   cd backend
   python app.py
   ```

4. Populate teams
   ```
   python add_all_teams.py
   ```

5. Open frontend/index.html in browser
