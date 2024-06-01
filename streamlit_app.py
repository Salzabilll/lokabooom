import streamlit as st
import random
import time

def get_random_answer():
    answer = [
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
    return random.choice(answer)

def main():
    st.title('⋆PERCAYA atau NGGA itu Pilihanmuᵕ̈      𓂃 ࣪˖ ִֶָ🐇་༘࿐ִֶָ𓂃 ࣪˖ ִֶָ🐇་༘࿐ִֶָ𓂃 ࣪˖ ִֶָ🐇་༘࿐ִֶָ𓂃 ࣪˖ ')
    st.write('#JUST FOR FUN😎')
    st.write("Panduan:\n1. Pikirkan Pertanyaanmu (Terserah Apapun, Bebas).\n2. Tahan Pertanyaanmu selama 5 detik.\n3. Tekan tombol di bawah setelah 5 detik :")

    # Inisialisasi variabel 
    if 'jumlah_klik' not in st.session_state:
        st.session_state['jumlah_klik'] = 0

    # Tampilkan tombol 
    if st.button('👉"Jawaban dari Pertanyaanmu"👈', disabled=st.session_state['jumlah_klik'] >= 3):
        random_answer = get_random_answer()
        placeholder = st.empty()
        placeholder.text("⤷"f" {random_answer}")
        time.sleep(8)
        placeholder.empty()
        st.session_state['jumlah_klik'] += 1
        
def panduan():
    st.write("")
    st.write("Jawaban akan menghilang setelah 8 detik. ***'Resapi Jawaban Yang Diterima Sebaik Mungkin.'***")
    st.write("Jangan Klik Tombol Saat Jawaban Masih Ada. Gunakan Waktu yang ada Untuk Memahaminya~")
    st.write("*Note : Hanya ada Sekian Kesempatan Bertanya")

    # Peringatan saat 3x pengeklikan
    if st.session_state['jumlah_klik'] == 3:
        st.warning("dAH AH, Capek")

    # Peringatan saat 4x pengeklikan
    if st.session_state['jumlah_klik'] == 4:
        st.warning("ANJERR LUU NANYA TEROSS, MALES GW!!")

if __name__ == '__main__':
    main()


