import streamlit as st
from PIL import Image
import io
import os

# Page title aur icon set karein
st.set_page_config(page_title="AI Image Compressor", page_icon="🖼️", layout="centered")

st.title("🖼️ Smart Image Compressor")
st.write("Upload your image and put the size you want to apply!")

# 1. Image Uploader widget
uploaded_file = st.file_uploader("Select your image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Original file details nikalna
    original_bytes = uploaded_file.getvalue()
    original_size_kb = len(original_bytes) / 1024
    
    # Image ko open karna display ke liye
    image = Image.open(uploaded_file)
    
    # Data columns banana do hisson mein dikhane ke liye
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)
        st.info(f"Original Size: **{original_size_kb:.2f} KB**")

    st.write("---")
    st.subheader("🔧 Compression Settings")
    
    # 2. Size type select karna (KB ya MB)
    size_type = st.selectbox("Select size unit:", ["KB", "MB"])
    
    # Default value set karna unit ke hisab se
    max_val = float(original_size_kb) if size_type == "KB" else float(original_size_kb / 1024)
    target_size = st.number_input(f"Target Size ({size_type}):", min_value=1.0, max_value=max_val, value=max_val/2, step=1.0)

    # Size ko bytes mein convert karna logical check ke liye
    target_bytes = target_size * 1024 if size_type == "KB" else target_size * 1024 * 1024

    if st.button("🚀 Compress Image"):
        # Image transparency handle karna (PNG to JPG background fix)
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')

        # Smart Compression Loop (Binary Search logic to target exact file size)
        low, high = 1, 95
        best_quality = 75
        output_buffer = io.BytesIO()
        
        with st.spinner("Adjust image size..."):
            # 7 rounds mein sub se perfect quality match mil jata hai
            for _ in range(7):
                mid = (low + high) // 2
                test_buffer = io.BytesIO()
                image.save(test_buffer, format="JPEG", optimize=True, quality=mid)
                test_size = len(test_buffer.getvalue())
                
                if test_size <= target_bytes:
                    best_quality = mid
                    output_buffer = test_buffer  # Agar size target se kam hai toh save kar lein
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Agar loop khatam hone par bilkul chota size na ban paaye toh safe fallback
            if output_buffer.getvalue() == b'':
                image.save(output_buffer, format="JPEG", optimize=True, quality=5)

        compressed_bytes = output_buffer.getvalue()
        final_size_kb = len(compressed_bytes) / 1024

        with col2:
            st.subheader("Compressed Image")
            st.image(compressed_bytes, use_container_width=True)
            st.success(f"Final Size: **{final_size_kb:.2f} KB**")

        st.write("---")
        # 3. Download Button
        st.download_button(
            label="📥 Download Compressed Image",
            data=compressed_bytes,
            file_name="compressed_output.jpg",
            mime="image/jpeg"
        )
