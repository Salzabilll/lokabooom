import streamlit as st
import random
import time

# CSS for custom styling
def add_custom_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
            border: 2px solid #4CAF50;
        }
        .stButton button:disabled {
            background-color: #9E9E9E;
            border: 2px solid #9E9E9E;
        }
        .stTitle {
            color: #4CAF50;
            font-family: Arial, sans-serif;
        }
        .stWarning {
            color: red;
            font-weight: bold;
        }
        .stInstructions {
            font-family: 'Courier New', Courier, monospace;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #4CAF50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def get_random_answer():
    answers = [
        "Ikuti Kata Hatimu.",
        "Kasian Anak Ini",
        "Menyerah Saja.",
        "Malaikatpun Bingung.",
        "Hmm...",
        "Jangan Menyerah. Berusahalah. Pikirkanlah Terus",
        "Coba Sholat Dulu, Siapa Tahu Ketemu Jawabannya.",
        "Ada Banyak Kesempatan.",
        "Menurutmu Aja Gimana?",
        "Coba Saja.",
        "Pelan-Pelan Aja.",
        "Sekarang.",
        "Pikir-Pikir Dulu Lagi Mending",
        "Hehehehehehe. Gila",
        "Astaghfirullah Dulu Aja si Kak.",
        "Serahkan Semuanya pada Tuhan Semesta Alam.",
        "Mundur.",
        "nt.",
        "tobat kak",
        "Kata gw Istirahat dulu Aja si.",
        "coba Pikir Baik-Baik",
        "Mungkin Jawabannya Ada di Dekatmu.",
        "Segera.",
        "Tahan.",
        "Waktu Yang Menjawabnya.",
        "Ga Tau. Namanya Juga Hidup.",
        "Mungkin Lain Waktu.",
        "Sulit si kalo ini.",
        "Siapin Diri Dulu Aja.",
        "Semua Hanya Sementara",
        "Waduh Waduh Waduh.",
        "Lihat Sekitarmu.",
        "Biarkan Waktu Yang Menjawabnya.",
        "Riweh Lu Kayak Soang.",
    ]
    return random.choice(answers)

def main():
    add_custom_css()
    
    st.markdown('<h1 class="stTitle">⋆PERCAYA atau NGGA itu Pilihanmuᵕ̈</h1>', unsafe_allow_html=True)
    st.write('# JUST FOR FUN 😎')
    st.markdown(
        """
        <div class="stInstructions">
        <p>Panduan:</p>
        <ol>
            <li>Pikirkan Pertanyaanmu (Terserah Apapun, Bebas).</li>
            <li>Tahan Pertanyaanmu selama 5 detik.</li>
            <li>Tekan tombol di bawah setelah 5 detik :</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Inisialisasi variabel untuk melacak jumlah pengeklikan
    if 'jumlah_klik' not in st.session_state:
        st.session_state['jumlah_klik'] = 0

    # Tampilkan tombol dan panggil fungsi Jawaban() ketika tombol ditekan
    if st.button('👉"Jawaban dari Pertanyaanmu"👈', disabled=st.session_state['jumlah_klik'] >= 3):
        random_answer = get_random_answer()
        placeholder = st.empty()
        placeholder.text("⤷ " + random_answer)
        time.sleep(8)
        placeholder.empty()
        st.session_state['jumlah_klik'] += 1
    st.write("")
    st.write("Teks menghilang setelah 8 detik. ***'Resapi Jawaban Yang Diterima Sebaik Mungkin.'***")
    st.write("Jangan Klik Tombol Saat Jawaban Masih Ada. Gunakan Waktu yang ada Untuk Memahaminya~")
    st.write("*Note : Hanya ada Sekian Kesempatan Bertanya")

    # Tampilkan peringatan setelah 3 kali pengeklikan
    if st.session_state['jumlah_klik'] == 3:
        st.markdown('<p class="stWarning">dAH AH, Capek</p>', unsafe_allow_html=True)

    # Tampilkan peringatan setelah 4 kali pengeklikan
    if st.session_state['jumlah_klik'] == 4:
        st.markdown('<p class="stWarning">ANJERR LUU NANYA TEROSS, MALES GW!!</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
