var express = require('express')
var path = require('path')
var app = express()
var bodyParser = require('body-parser')
var socket = require('socket.io')
var port = process.env.PORT || 3000

var dataBase = [
	{ name: 'obj_name1', time: '00:00:00' },
	{ name: 'obj_name2', time: '00:00:00' },
	{ name: 'obj_name3', time: '00:00:00' }
]

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
	if (dataBase.find(req.body.name) === -1)
		dataBase.push(req.body)
	else dataBase[dataBase.indexOf(dataBase.find(req.body.name))] = req.body
})

server = app.listen(port , () => console.log('Listening on port ' + port))

io = socket(server)

io.on('connection', client => {
	console.log('client connected')
	io.emit('data_base', { monitor: dataBase })
	client.on('fetch', data => {
		io.emit('data_base', { monitor: dataBase })
	})
})
