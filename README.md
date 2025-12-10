# Lightweight Offline Currency Converter (HCI and Systems Design)

## Description
This project is a simple, standalone desktop and mobile application that converts currencies using locally stored exchange rates, prioritizing reliability and usability in environments with intermittent or expensive internet connectivity.
It serves as a strong demonstration of foundational software development skills, focusing on creating a robust user experience despite resource constraints.
The core goal is to provide a user-centric tool that maintains conversion even when disconnected,which is needed in many developing regions.

# 🎯 Status: Complete

# 💡 Core Technical & Design Contributions
This project highlights key principles in system design and Human-Computer Interaction (HCI):
1. Offline Functionality: Implemented a persistent local storage mechanism (exchange_rates.json) to save and load all exchange rates. This ensures the application is fully functional and reliable, even when the network is unavailable.
2. User-Centric GUI Design (HCI): Developed a clean, intuitive Graphical User Interface (GUI) using Python's tkinter. Features like Swap Currencies, Update Rate, and Add New Currency were included to maximize user control and adaptability without requiring developer interaction.
3. Modular Architecture: Structured the Python code with clear, well-commented functions for rate loading, saving, conversion, and rate management, demonstrating clean and maintainable software engineering practices.
4. Error Handling: Implemented try...except blocks to handle common user errors (e.g., non-numeric input) and file loading issues, ensuring application stability.

# 💻 Technologies Used
1. Category :Tools & Libraries
2. Language : Python
3. GUI Framework : tkinter (Standard Python GUI library)
4. Data Persistence : json (For local rate storage)
5. Key Concepts : Offline Caching, User Interface Design (HCI), Modular Programming

# 🚀 Setup and Installation
Prerequisites : Python 3.x (The project uses standard library modules only)

# Running the Application
Clone the repository.
Navigate to the project directory.
Run the main script: python "Currency Converter.py"
Note: The application will automatically create an exchange_rates.json file upon first run if it doesn't already exist.

# 🖼️ Visuals
In visuals.png

# 🔑 Skills Demonstrated
Offline System Design, Human-Computer Interaction (HCI), Python Programming, GUI Development (tkinter), File I/O (JSON), Robust Error Handling.
