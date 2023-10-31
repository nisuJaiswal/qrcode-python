import streamlit as st
from io import BytesIO
import qrcode
import base64


# Function to generate QR code
def generate_qr_code(data, foreground, background):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=foreground, back_color=background)
    return img


# Download the Image
def get_binary_file_downloader_html(bin_data, label="Download"):
    bin_data = bin_data.read()
    b64 = base64.b64encode(bin_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{label}" target="_blank">{label}</a>'
    return href


def main():
    # Streamlit app
    st.title("QR Code Generator")

    # Input data
    data = st.text_input("Enter data for which you want to generate a QR code:")

    foreground = st.color_picker("QR Code Color: ", "#000000")
    background = st.color_picker("Background Color: ", "#FFFFFF")

    if st.button("Generate QR Code"):
        if data:
            qr_img = generate_qr_code(data, foreground, background)
            img_io = BytesIO()
            qr_img.save(img_io, format="PNG")
            st.image(
                img_io,
                caption="Generated QR Code",
            )
            st.markdown(
                get_binary_file_downloader_html(img_io, "Download"),
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please enter data before generating a QR code.")


if __name__ == "__main__":
    main()
