import pymongo # meng-import library pymongo yang sudah kita install
from flask import Flask
from flask import request
app = Flask(__name__)

password = 'userdb'
uri = f"mongodb+srv://dbuser:userdb@cluster0.zrgn8rk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(uri)
db = client['test_database'] # ganti sesuai dengan nama database kalian
my_collections = db['test_collection'] # gatnti sesuai dengan nama collections kalian

def kirim_data(beatsPerMinute, SpO2):
    sensor = {'SpO2':90, 'beatsPerMinute':88}
    results = my_collections.insert_many([sensor])
    print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan

@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/sensor/data',methods=['POST'])
def data():
    beatsPerMinute = request.args.get('beatsPerMinute')
    SpO2 = request.args.get('SpO2')

    if beatsPerMinute is not None:
        beatsPerMinute = float(beatsPerMinute)
    if SpO2 is not None:
        SpO2= int(SpO2)

    #mengirim data sensor ke db
    kirim_data(beatsPerMinute=beatsPerMinute, SpO2=SpO2)

    return f'beatsPerMinute: {beatsPerMinute}, SpO2: {SpO2}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')