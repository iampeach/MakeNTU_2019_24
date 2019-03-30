var express = require('express')
var path = require('path')
var app = express()
var bodyParser = require('body-parser')
var socket = require('socket.io')
var port = process.env.PORT || 3000

var dataBase = []
var addData = []
var patchData = []

app.use(express.static(path.join(__dirname, 'public')))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/', (req, res) => {
	res.sendFile(path.join(__dirname, 'public', 'index.html'))
})
app.get('/monitor', (req, res) => {
	res.sendFile(path.join(__dirname, 'public', 'index.html'))
})
app.get('/register', (req, res) => {
	res.sendFile(path.join(__dirname, 'public', 'index.html'))
})
app.post('/data', (req,res) => {
	if (dataBase.find(d=>{return d.name === req.body.name}) === undefined){
		dataBase.push(req.body)
		addData.push(req.body)
	}else {
		dataBase[dataBase.indexOf(dataBase.find(d=>{return d.name === req.body.name}))] = req.body
		patchData.push(req.body)
	}
	res.json('finished')
})

server = app.listen(port , () => console.log('Listening on port ' + port))

io = socket(server)

io.on('connection', client => {
	console.log('client connected')
	io.emit('data_base', { monitor: dataBase })
	client.on('fetch', data => {
		io.emit('add_data_base', { monitor: addData })
		io.emit('patch_data_base', { monitor: patchData })
		addData = []
		patchData = []
	})
})
