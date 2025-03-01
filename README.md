# Unit Converter Pro

Unit Converter Pro is an advanced web-based unit conversion application built using **Streamlit**. It allows users to seamlessly convert units across multiple categories, including length, weight, temperature, data storage, pressure, energy, and time.

## 🚀 Features

- **Supports multiple unit categories**: Length, Weight, Temperature, Data Storage, Pressure, Energy, and Time.
- **Elegant UI**: Stylish and user-friendly interface using custom CSS.
- **Real-time conversion**: Instant unit conversions with high precision.
- **Interactive layout**: Sidebar selection, intuitive input, and conversion results displayed in a structured format.
- **Fully responsive**: Works seamlessly on different screen sizes.

## 🛠️ Installation

To run the Unit Converter Pro locally, follow these steps:

### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/unit-converter-pro.git
cd unit-converter-pro
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 📌 Usage

1. **Select a category** from the sidebar (e.g., Length, Weight, Temperature, etc.).
2. **Choose the units** you want to convert from and to.
3. **Enter the value** to be converted.
4. Click on the **Convert** button to see the results.

## 📂 Project Structure
```plaintext
unit-converter-pro/
│── app.py                # Main application file
│── requirements.txt      # Required dependencies
│── README.md             # Documentation file
│── .gitignore            # Git ignore file
```

## 📜 Dependencies

- **Streamlit**: Web framework for creating the app.
- **Python 3.7+**

You can install all dependencies using:
```sh
pip install -r requirements.txt
```

## 🌍 Deployment

To deploy the app on **Streamlit Cloud**, **Heroku**, or **Render**, follow these steps:

### Deploy on Streamlit Cloud
1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and connect your GitHub repository.
3. Configure the app to run `app.py`.
4. Deploy and share the link!

### Deploy on Heroku
```sh
heroku create unit-converter-pro
heroku git:remote -a unit-converter-pro
git push heroku main
```

## 👨‍💻 Author
- **Your Name** Rida Azam
- **GitHub**: [Your GitHub Profile](https://github.com/Rida-Azam)



---

Enjoy using **Unit Converter Pro**! 🚀

