import streamlit as st


# Define functions to handle the conversion between different units

def convert_length(value, from_unit, to_unit):
    length_conversions = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'metric_ton': 1000.0,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

def convert_data(value, from_unit, to_unit):
    data_conversions = {
        'byte': 1.0,
        'kilobyte': 1024,
        'megabyte': 1024**2,
        'gigabyte': 1024**3,
        'terabyte': 1024**4,
        'petabyte': 1024**5,
        'bit': 0.125,
        'kibibyte': 1024,
        'mebibyte': 1024**2,
        'gibibyte': 1024**3
    }
    return value * data_conversions[from_unit] / data_conversions[to_unit]

def convert_pressure(value, from_unit, to_unit):
    pressure_conversions = {
        'pascal': 1.0,
        'kilopascal': 1000,
        'bar': 100000,
        'psi': 6894.76,
        'atmosphere': 101325,
        'torr': 133.322,
        'millimeter_mercury': 133.322,
        'inch_mercury': 3386.39
    }
    return value * pressure_conversions[from_unit] / pressure_conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    energy_conversions = {
        'joule': 1.0,
        'kilojoule': 1000,
        'calorie': 4.184,
        'kilocalorie': 4184,
        'watt_hour': 3600,
        'kilowatt_hour': 3.6e6,
        'electron_volt': 1.602e-19,
        'british_thermal_unit': 1055.06
    }
    return value * energy_conversions[from_unit] / energy_conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    time_conversions = {
        'second': 1.0,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2592000,  # average month (30.44 days)
        'year': 31536000,  # non-leap year
        'decade': 315360000,
        'century': 3153600000,
        'millisecond': 0.001,
        'microsecond': 0.000001,
        'nanosecond': 1e-9
    }
    return value * time_conversions[from_unit] / time_conversions[to_unit]

def main():
    st.set_page_config(page_title="Unit Converter Pro", page_icon="🔄", layout="wide")

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
    }
    .stSelectbox, .stNumberInput {
        background-color: white !important;
        border-radius: 10px !important;
        padding: 10px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #2196F3, #00BCD4) !important;
        color: white !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
    }
    .success-msg {
        background: linear-gradient(135deg, #2196F3, #00BCD4);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
    }
    .result-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .unit-label {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    .unit-value {
        font-size: 2.2rem;
        font-weight: 600;
        margin: 0.5rem 0;
        color: white;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .arrow-icon {
        font-size: 2rem;
        margin: 1rem 0;
        color: rgba(255, 255, 255, 0.9);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar with gradient background
    st.sidebar.markdown("""
    <div style='
        background: linear-gradient(45deg, #1976D2, #64B5F6);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    '>
        <h1 style='color: white; text-align: center; margin: 0;'>🔄 Smart Unit Converter ✨</h1>
    </div>
    """, unsafe_allow_html=True)

    categories = {
        "📏 Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
        "⚖️ Weight": ["kilogram", "gram", "milligram", "metric_ton", "pound", "ounce"],
        "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
        "💾 Data Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte", "bit"],
        "📊 Pressure": ["pascal", "kilopascal", "bar", "psi", "atmosphere", "torr"],
        "⚡ Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour"],
        "⏰ Time": ["second", "minute", "hour", "day", "week", "month", "year", "decade", "century"]
    }

    unit_type = st.sidebar.selectbox(
        "Select Category",
        list(categories.keys()),
        help="Choose the type of unit you want to convert"
    )

    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 style='color: #1976D2;'>🚀 Advanced Unit Converter Pro 🌟</h1>
        <p style='color: #666; font-size: 18px;'>✨ Convert between different units with high precision ✨</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", categories[unit_type], key="from")
        try:
            value = float(st.text_input("Enter Value", value="1.0", key="value"))
        except ValueError:
            st.error("Please enter a valid number")
            value = 1.0

    with col2:
        to_unit = st.selectbox("To", categories[unit_type], key="to")

    convert_functions = {
        "📏 Length": convert_length,
        "⚖️ Weight": convert_weight,
        "🌡️ Temperature": convert_temperature,
        "💾 Data Storage": convert_data,
        "�� Pressure": convert_pressure,
        "⚡ Energy": convert_energy,
        "⏰ Time": convert_time
    }

    if st.button("Convert", key="convert"):
        result = convert_functions[unit_type](value, from_unit, to_unit)
        
        # Create three columns for better layout
        col1, col2, col3 = st.columns([1, 0.2, 1])
        
        with col1:
            st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.1); 
                        padding: 20px; 
                        border-radius: 10px; 
                        text-align: center;
                        background-color:#D3D3D3;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                <p style='color: #666; font-size: 16px;'>From</p>
                <h2 style='color: #1976D2; font-size: 28px; margin: 10px 0;'>{}</h2>
                <p style='color: #666; font-size: 18px;'>{}</p>
            </div>
            """.format(value, from_unit.replace('_', ' ').title()), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='text-align: center; padding: 20px;'>
                <h1 style='color: #1976D2; font-size: 24px;'>➜</h1>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style='background: rgba(255, 255, 255, 0.1); 
                        padding: 20px; 
                        border-radius: 10px; 
                        text-align: center;
                        background-color:#D3D3D3;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                <p style='color: #666; font-size: 16px;'>To</p>
                <h2 style='color: #1976D2; font-size: 28px; margin: 10px 0;'>{}</h2>
                <p style='color: #666; font-size: 18px;'>{}</p>
            </div>
            """.format(result, to_unit.replace('_', ' ').title()), unsafe_allow_html=True)

if __name__ == "__main__":
    main()

