import streamlit as st

st.title("Kalkulator BMI Klinik")

berat = st.text_input("Berat (kg)")
tinggi = st.text_input("Tinggi (meter)")

if st.button("Kira BMI"):
    try:
        berat = float(berat)
        tinggi = float(tinggi)

        bmi = berat / (tinggi * tinggi)

    except ValueError:
        st.error("Sila masukkan nombor yang sah.")

    except ZeroDivisionError:
        st.error("Tinggi tidak boleh menjadi 0.")

    except Exception:
        st.error("Ralat tidak dijangka berlaku.")

    else:
        st.success(f"BMI anda ialah {bmi:.2f}")

    finally:
        st.info("Sistem selesai memproses permintaan anda.")


st.subheader("Rekod Pesakit")

if st.button("Papar Rekod Lama"):
    try:
        with open("rekod_pesakit.txt", "r") as file:
            rekod = file.read()

        st.write(rekod)

    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan")