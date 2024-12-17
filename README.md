# 📄 Invoice Number Processor

## Overview

A simple Streamlit web application that helps you process invoice numbers by removing the 'i' character and ensuring Excel-safe formatting for large numbers.

## 🌟 Features

- Upload multiple CSV or Excel files simultaneously
- Remove 'i' character from 'InvNo' column
- Convert invoice numbers to Excel-safe text format
- Download processed files individually
- User-friendly web interface

## 🛠️ Prerequisites

### Software Requirements
- Python 3.7+
- Streamlit
- Pandas

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/invoice-number-processor.git
cd invoice-number-processor
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📦 Required Libraries

Install the following libraries:
```bash
pip install streamlit
pip install pandas
```

## 🚀 How to Run

```bash
streamlit run app.py
```

## 💡 How to Use

1. Open the web application in your browser
2. Click on "Upload your files" button
3. Select one or multiple CSV or Excel files
4. Application will automatically process files
5. Download processed files with modified invoice numbers

### Processing Details
- Removes 'i' from 'InvNo' column
- Converts numbers to Excel-safe text format
- Saves processed files as CSV

## 🔍 Example

Input File (`invoice.xlsx`):
```
InvNo     | Amount
i12345    | $500
i67890    | $750
```

Output File (`processed_invoice.csv`):
```
InvNo     | Amount
="12345"  | $500
="67890"  | $750
```

## 🚨 Troubleshooting

- Ensure files have an 'InvNo' column
- Supports CSV and Excel formats
- Large files might take longer to process

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

---

**Happy Invoice Processing! 📊✨**
