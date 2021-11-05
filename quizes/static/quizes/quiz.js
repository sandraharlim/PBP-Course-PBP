console.log("hello world quiz")
const url = window.location.href

const quizBox = document.getElementById("quiz-box")
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')

const actTime = (time) =>{
    console.log(time)

    if (time.toString().length <= 2){
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let menit = time - 1
    let detik = 60
    let liatDetik
    let liatMenit

    const timer = setInterval(()=>{
        detik --
        console.log("running")
        if (detik < 0) {
            detik = 59
            menit --
        }
        if (menit.toString().length < 2) {
            liatMenit = '0'+ menit
        } else {
            liatMenit = menit
        }
        if (detik.toString().length < 2) {
            liatDetik = '0' + detik
        } else {
            liatDetik = detik
        }
        if (menit === 0 && detik === 0){
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert('Waktu Sudah Habis :(')
                sendData()
            }, 500)
           
        }

        timerBox.innerHTML = `<b>${liatMenit}:${liatDetik}</b>`

    }, 1000)

}


$.ajax({
    type: 'GET',
    url: `${url}data/`,
    success: function(response){
        // console.log(response)
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer =>{
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>    
                    ` 
                })
            }
        });
        actTime(response.time)
    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
//const elements = [...document.getElementsByClassName('ans')]


const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el =>{
        if (el.checked){
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })
    
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            // console.log(response)
            const Hasil = response.Hasil
            console.log(Hasil)
            quizForm.classList.add('not-visible')

            scoreBox.innerHTML = `${response.Lolos ? 'Selamat yaa! :)' :'Ups..:('} Hasil Quiz Anda adalah ${response.Skor.toFixed(2)}%`

            Hasil.forEach(res =>{
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)){
                    //console.log(question)
                    //console.log(resp)
                    //console.log("1111111")

                    resDiv.innerHTML += question
                    const cls = ['container','p-3', 'text-light', 'h3']
                    resDiv.classList.add(...cls)

                    if (resp =='Belum dijawab'){
                        resDiv.innerHTML += '-Belum dijawab'
                        resDiv.classList.add('bg-danger')
                    }
                    else{
                        const answer = resp['Terjawab']
                        const correct = resp['Jawaban_benar']

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` Jawaban: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += `| Jawaban yang benar: ${correct}`
                            resDiv.innerHTML += `| Jawaban: ${answer}`
                        }
                    }
                }
                // const body = document.getElementsByTagName('BODY')[0]
                resultBox.append(resDiv)
            })
        
        },
        error: function(error){
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})