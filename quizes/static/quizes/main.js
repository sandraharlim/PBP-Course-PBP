console. log("Hellow World")

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const nama = modalBtn.getAttribute('data-quiz')
    const totalSoal = modalBtn.getAttribute('data-questions')
    const Kesulitan = modalBtn.getAttribute('data-difficulty')
    const PassingGrade = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML =  `
        <div class="h5 mb-3">Apa anda siap untuk memulai "<b>${nama}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>Tingkat Kesulitan: <b>${Kesulitan}</b></li>
                <li>Jumlah Soal: <b>${totalSoal}</b></li>
                <li>Passing Grade (dalam %): <b>${PassingGrade}%</b></li>
                <li>Waktu (dalam menit): <b>${time} min</b></li>

            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk
    })
    
}))