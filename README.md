# midtermprojectPBP_F03

[![Test and Deploy][actions-badge]][commits-gh]
[![pipeline status][pipeline-badge]][commits-gl]
[![coverage report][coverage-badge]][commits-gl]
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
**Pandemic Based Productivity (PBP)**<br>
Website ini dibuat untuk membantu pengguna menghadapi budaya-budaya baru saat pandemi seperti PJJ, WFJ, SFH, dan Prokes. Di dalam website ini terdapat fitur berita terkini terkait pandemi seperti tingkat kesembuhan, perkembangan vaksin, dan aturan baru. Untuk mendukung pengguna saling bertukar informasi, kami juga menyiapkan ruang diskusi berupa forum yang dapat diposting oleh pengguna. Terdapat quiz interaktif seputar protokol kesehatan dalam masa pandemi untuk mendukung pengguna menerapkan prokes.

Khusus user dengan status murid, kami menyediakan fitur susun jadwal kegiatan belajar serta deadline tugas dan ujian. Diharapkan fitur ini membantu murid untuk menghadapi PJJ.

## Persona : 
- Guest (akses cuma bisa liat berita, pokonya yg ga perlu input-input)
- User non student (bisa input-input, tetapi tidak bisa memakai fitur jadwal kuliah/sekolah pada modul scheduling)
- User student (bisa input-input, bisa scheduling juga)
- Admin

## Daftar modul :
1. App perencanaan kuliah (PJJ)<br>
Pengguna **student** dapat menambahkan jadwal kuliah/sekolah, tanggal Ujian, ataupun deadline tugas. Kemudian hal ini akan ditampilkan dalam bentuk **calender**<br>

2. To-do list<br>
to-do list biasa.<br>

3. Info terkini terkait pendidikan<br>
Bisa di connect lewat api suatu website gitu, nanti ada pilihan berita apa aja yg mau diliat, nnt kaya pake card misalnya headline nya ada di depan, sama author+tanggal mungkin, kaya line today.

4. Forum tentang pandemi<br>
Dalam forum user bisa membuat diskusi baru dan memposting pendapatnya
(mirip seperti stack overflow cuman versi pandemi)<br>
Kategorinya ada 3 : tips kesehatan, informasi pandemi (tentang covid, wfh, dll,), pertanyaan2 

5. Quiz: Seberapa siapkah anda menghadapi pandemi covid-19?<br>
Akan ada quiz seputar prokes dalam  pandemi covid-19 <br>
Ada leaderboard hasil quiz<br>
Mungkin akan ada artikel tentang prokes<br>
Mini games covid (Arcade), masih tentative<br>


6. Live Chart Covid Dunia dan Indonesia dengan News Terkini.<br>

7. App scheduling biasa<br>
Pengguna dapat menambahkan **event** seperti jadwal rapat, hari ulang tahun, ataupun reminder, yang kemudian akan ditampilkan dalam bentuk **calender** (seperti app 1, tetapi tidak eksklusif untuk **student**)

### Template repo disediakan oleh : https://github.com/laymonage/django-template-heroku

[actions-badge]: https://github.com/laymonage/django-template-heroku/workflows/Test%20and%20Deploy/badge.svg
[commits-gh]: https://github.com/laymonage/django-template-heroku/commits/master
[pipeline-badge]: https://gitlab.com/laymonage/django-template-heroku/badges/master/pipeline.svg
[coverage-badge]: https://gitlab.com/laymonage/django-template-heroku/badges/master/coverage.svg
[commits-gl]: https://gitlab.com/laymonage/django-template-heroku/-/commits/master

