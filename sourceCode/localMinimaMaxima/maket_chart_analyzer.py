import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to load image
def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError("Could not find the image. Verify the path.")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), image


# Resize and preprocess the image
def preprocess_and_resize_image(image, scale_percent=150):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred, resized


# Detect candlestick contours from the image
def detect_candlestick_contours(image):
    edges = cv2.Canny(image, 40, 120)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candlestick_data = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 20 or h < 1: #Change from w < 5 to w > 20, also h < 1
            continue
        candlestick_data.append({'x': x, 'y': y, 'width': w, 'height': h})
    return candlestick_data


# Calculate support and resistance
def calculate_support_resistance(candlestick_data):
    if len(candlestick_data) < 3:
        raise ValueError("Not enough candlestick data to compute support and resistance levels.")
    y_coords = np.array([candle['y'] for candle in candlestick_data])
    local_minima = []
    local_maxima = []
    for i in range(1, len(y_coords) - 1):
        if y_coords[i] < y_coords[i - 1] and y_coords[i] < y_coords[i + 1]:
            local_minima.append(y_coords[i])
        if y_coords[i] > y_coords[i - 1] and y_coords[i] > y_coords[i + 1]:
            local_maxima.append(y_coords[i])
    support = np.mean(local_minima) if local_minima else np.min(y_coords)
    resistance = np.mean(local_maxima) if local_maxima else np.max(y_coords)
    return support, resistance


# Draw support and resistance zones
def draw_support_resistance_zones(image, resistance, support, buffer=10):
    overlay = np.zeros_like(image, dtype=np.uint8)
    bottom_support_top = int(support - buffer)
    bottom_support_bottom = int(support + buffer)
    bottom_support_top = max(bottom_support_top, 0)
    bottom_support_bottom = min(bottom_support_bottom, image.shape[0])
    
    cv2.rectangle(overlay, (0, bottom_support_top), (image.shape[1], bottom_support_bottom), (0, 255, 0), -1)
    
    top_resistance_top = int(resistance - buffer)
    top_resistance_bottom = int(resistance + buffer)
    top_resistance_top = max(top_resistance_top, 0)
    top_resistance_bottom = min(top_resistance_bottom, image.shape[0])
    
    cv2.rectangle(overlay, (0, top_resistance_top), (image.shape[1], top_resistance_bottom), (255, 0, 0), -1)
    
    alpha = 0.3
    image_with_zones = cv2.addWeighted(image, 1 - alpha, overlay, alpha, 0)
    
    cv2.putText(
        image_with_zones,
        "Support",
        (20, bottom_support_bottom - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )
    cv2.putText(
        image_with_zones,
        "Resistance",
        (20, top_resistance_top + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0),
        2
    )
    return image_with_zones


# Visualize the processed image
def visualize_image(image):
    plt.figure(figsize=(12, 8))
    plt.imshow(image)
    plt.axis("off")
    plt.show()


# Process the loaded image
def process_analysis(file_path):
    try:
        image, original_image = load_image(file_path)
        preprocessed, resized_image = preprocess_and_resize_image(image, scale_percent=150)
        detected_candles = detect_candlestick_contours(preprocessed)
        support, resistance = calculate_support_resistance(detected_candles)
        image_with_zones = draw_support_resistance_zones(
            resized_image, support, resistance, buffer=15
        )
        visualize_image(image_with_zones)
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Select file dialog
def on_select_file():
    global selected_file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if file_path:
        selected_file_path = file_path
        file_label.config(text=file_path.split("/")[-1])


# Handle analysis submission
def on_submit():
    if not selected_file_path:
        messagebox.showwarning("No File Selected", "Please select an image file first.")
    else:
        process_analysis(selected_file_path)


# Handle back button
def on_back():
    root.destroy()


# Initialize global variables
selected_file_path = None

# GUI setup
root = tk.Tk()
root.title("Market Chart Analyzer")
root.geometry("600x400")
root.resizable(False, False)

# Main container frame
frame = ttk.Frame(root)
frame.pack(expand=True)

# Title
heading_label = ttk.Label(frame, text="Market Chart Analyzer", font=("Arial", 18, "bold"))
heading_label.grid(row=0, column=0, pady=10)

# File select area
file_select_frame = ttk.Frame(frame)
file_select_frame.grid(row=1, column=0, pady=10)

file_label = ttk.Label(file_select_frame, text="No file selected", anchor="w", relief="groove", padding="5")
file_label.grid(row=0, column=0, padx=5, sticky="ew")

select_file_button = ttk.Button(file_select_frame, text="Select File", command=on_select_file)
select_file_button.grid(row=0, column=1, padx=5)

# Buttons area
button_frame = ttk.Frame(frame)
button_frame.grid(row=2, column=0, pady=10)

submit_button = ttk.Button(button_frame, text="Submit", command=on_submit)
submit_button.grid(row=0, column=0, padx=5)

back_button = ttk.Button(button_frame, text="Back", command=on_back)
back_button.grid(row=0, column=1, padx=5)

root.mainloop()
