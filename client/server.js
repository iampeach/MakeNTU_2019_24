var express = require('express')
var path = require('path')
var app = express()
var bodyParser = require('body-parser')
var port = process.env.PORT || 3000

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

app.listen(port , () => console.log('Listening on port ' + port))
