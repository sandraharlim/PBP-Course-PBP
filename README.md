# midtermprojectPBP_F03

## Anggota Kelompok F03:
- Anne Aisyah Azka (NPM: 2006484993)
- Johanes Raka Triadana Nikaputra (NPM: 2006463326)
- Muhammad Raihan Adliputra (NPM: 2006485680)
- Nico Fathi Rizqi (NPM: 2006485724)
- Puti Adiva (NPM: 2006484835)
- Sandra Harlim (NPM: 2006464303)
- Zundullah B. Djibat (NPM: 2006464505)

## Link Herokuapp :
https://pbp-midtermproject-f03.herokuapp.com 

## Cerita singkat aplikasi :
**Pandemic Based Productivity(PBP)**
Website ini dibuat untuk membantu pengguna menghadapi budaya-budaya baru saat pandemi seperti PJJ, WFJ, SFH, dan Prokes. Di dalam website ini terdapat fitur berita terkini terkait pandemi seperti tingkat kesembuhan, perkembangan vaksin, dan aturan baru. Untuk mendukung pengguna saling bertukar informasi, kami juga menyiapkan ruang diskusi berupa forum yang dapat diposting oleh pengguna. Terdapat quiz interaktif seputar protokol kesehatan dalam masa pandemi untuk mendukung pengguna menerapkan prokes.

Khusus user dengan status murid, kami menyediakan fitur susun jadwal kegiatan belajar serta deadline tugas dan ujian. Diharapkan fitur ini membantu murid untuk menghadapi PJJ.

## Persona : 
- Guest (akses cuma bisa liat berita, pokonya yg ga perlu input-input)
- User non student (bisa input-input, tetapi tidak bisa memakai fitur jadwal kuliah/sekolah pada modul scheduling)
- User student (bisa input-input, bisa scheduling juga)
- Admin

## Daftar modul :
1. Website perencanaan kuliah (PJJ)
Scheduling (Jadwal kegiatan, Tanggal Ujian, Deadline tugas, Jadwal rapat)<br>
Case 1 = mirip susunjadwal ristek, user memilih matkul dengan dosen tertentu, nnt otomatis ke integrate di tabel jadwalnya, jadi otomatis kebikin selama hari senin-minggu, bakal ada kuliah/kegiatan apa saja. Kalo mau nambahin jadwal rapat tetap, bikin tempat khusus aja buat input manual. Bisa remove jadwal juga, andaikan gaperlu/drop matkul/rapat udh gaada lg.<br>
Case 2 = User menginput jadwal kuliahnya. Format keluaran : Nama Mata Kuliah (Waktu Pelajaran). Contoh: Aljabar Linear (08:00 - 10:30). Setiap kolom mewakili hari yang berbeda. Misal kolom pertama untuk jadwal kuliah hari senin, kolom kedua untuk hari selasa, dst.

2. To-do list
Ya to-do list biasa.

3. Info terkini terkait pendidikan
Bisa di connect lewat api suatu website gitu, nanti ada pilihan berita apa aja yg mau diliat, nnt kaya pake card misalnya headline nya ada di depan, sama author+tanggal mungkin, kaya line today

4. Forum tentang pandemi
Dalam forum user bisa membuat diskusi baru dan memposting pendapatnya
(mirip seperti stack overflow cuman versi pandemi)<br>
Kategorinya ada 3 : tips kesehatan, informasi pandemi (tentang covid, wfh, dll,), pertanyaan2 

5. Quiz: Seberapa siapkah anda menghadapi pandemi covid-19?
Akan ada quiz seputar prokes dalam  pandemi covid-19 <br>
Ada leaderboard hasil quiz<br>
Mungkin akan ada artikel tentang prokes<br>
Mini games covid (arcade), masih tentative<br>


6. Live chart Covid dunia dan Indonesia dengan News Terkinic
About Us(masih maybe)

### Template repo disediakan oleh : https://github.com/laymonage/django-template-heroku


