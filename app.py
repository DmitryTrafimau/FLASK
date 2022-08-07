from flask import Flask, request
import func

app = Flask(__name__)

@app.route('/')
def start_page():
    return f'''
        <html>
            <body>
                <center><h1>Добро из рук в руки</h1>
                <h2>Не жмись, отдай что-нибудь людям!</h2>
                <form action='/donate' method='post'>
                <label>Что хотите отдать?
                    <p><input type='text' name='goods' placeholder='введите название товара'></label><br><p>
                <label>Сколько?
                    <p><input type='number' name='qty' placeholder='введите количество'></label><p>
                <button type='submit'>ОТДАТЬ</button>
                </form><br><br>
                <h2>Если что-то нужно, просто попроси.</h2>
                <form action='/request/donation' method='post'>
                    <label><input type='radio' name='radio_button' value='fifo'checked> FIFO</label>
                    <label><input type='radio' name='radio_button' value='lifo'> LIFO</label>
                <br><br><br>
                    <button type='submit'>ПРОСИТЬ</button>
                </form>
            </body>
        </html>
        '''


@app.route('/request/donation', methods=['POST'])
def gift_page():
    strategy = request.form['radio_button']
    if strategy == 'fifo':
        func.fifo()
    else:
        func.lifo()
    return f'''
            <html>
                <body>
                    <center><h2>{func.reply}<h2>
                    <a href='/'><button type='submit'>Вернуться на главную</button></a>
                </body>
            </html>
            '''


@app.route('/donate', methods=['POST'])
def donate_page():
    goods = request.form['goods']
    qty = int(request.form['qty'])
    func.database.append({'name': goods, 'qty': qty})
    func.data_saver()
    return '''
            <html>
                <body>
                    <center><h2>Спасибо!</h2>
                    <a href='/'><button type='submit'>Вернуться на главную</button></a>
                </body>
            </html>
            '''


if __name__ == '__main__':
    app.run(debug=True)
