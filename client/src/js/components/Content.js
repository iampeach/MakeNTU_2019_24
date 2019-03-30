import React, { Component } from 'react'
import io from 'socket.io-client'
import { Switch, Route } from 'react-router-dom'
import Home from './contents/Home'
import Monitor from './contents/Monitor'
import Register from './contents/Register'

export default class Content extends Component {
	constructor(props) {
		super(props)
		this.state = {
			monitor: []
		}
	}
	componentDidMount() {
		const socket = io('/')
		socket.on('data_base', data_base => {
			this.setState( state => ({ monitor: data_base.monitor }))
		})
	}
	addMonitoringObject = name => {
		var object = {name: name, time: ''}
		this.setState(state=>({monitor: [...state.monitor, object]}))
	}
	setObjectTime = (name, time) => {
		var idx = this.state.monitor.indexOf(this.state.monitor.find( obj => {
			return obj.name === name
		}))
		this.setState( state => {
			var monitor = state.monitor
			var obj = { name: monitor[idx].name, time: time }
			monitor.splice(idx, 1)
			return { monitor : [...monitor, obj] }
		})
	}
	render() {
		return(
			<div>
				<Switch>
					<Route exact path='/' render={() => <Home />} />
					<Route path='/monitor' render={() => <Monitor objects={this.state.monitor}/>} />
					<Route path='/register' render={() => <Register />} />
				</Switch>
			</div>
		)
	}
}
