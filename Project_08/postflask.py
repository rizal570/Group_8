import pymongo # meng-import library pymongo yang sudah kita install
from flask import Flask
from flask import request
app = Flask(__name__)

data = []
# password = 'userdb'
# uri = f"mongodb+srv://dbuser:userdb@cluster0.zrgn8rk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# client = pymongo.MongoClient(uri)
# db = client['test_database'] # ganti sesuai dengan nama database kalian
# my_collections = db['test_collection'] # gatnti sesuai dengan nama collections kalian

# def kirim_data(beatsPerMinute, SpO2):
#     sensor = {'SpO2': 0, 'beatsPerMinute': 0}
#     results = my_collections.insert_many([sensor])
#     print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan

@app.route('/sensor/data',methods=['POST'])
def post():
    beatsPerMinute = request.args.get('beatsPerMinute')
    SpO2 = request.args.get('SpO2')
    print(f"Received beatsPerMinute: {beatsPerMinute}")
    print(f"Received SpO2: {SpO2}")
    if beatsPerMinute is not None:
        beatsPerMinute = float(beatsPerMinute)
    if SpO2 is not None:
        SpO2= float(SpO2)
    if beatsPerMinute is not None and SpO2 is not None:
        beatsPerMinute = float(beatsPerMinute)
        SpO2= float(SpO2)
        subData = [beatsPerMinute, SpO2]
        data.append(subData)
        return 'berhasil disimpan ke server', 200
    else:
        return 'Failed to receive data', 400
    #mengirim data sensor ke db
    # kirim_data(beatsPerMinute=beatsPerMinute, SpO2=SpO2)

    # return f'beatsPerMinute: {beatsPerMinute}, SpO2: {SpO2}'

@app.route('/',methods=[ 'GET'])
def get():
    return 'GET METHOD'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
