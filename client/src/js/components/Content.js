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
		this.updateInterval = undefined
	}
	componentDidMount() {
		const socket = io('/')
		socket.on('data_base', data_base => {
			this.setState( state => ({ monitor: data_base.monitor }))
		})
		socket.on('add_data_base', data_base => {
			for (let i = 0; i < data_base.monitor.length; ++i)
				this.addMonitoringObject(data_base.monitor[i])
		})
		socket.on('patch_data_base', data_base => {
			for (let i = 0; i < data_base.monitor.length; ++i)
				this.setObjectTime(data_base.monitor[i])
		})
		this.updateInterval = setInterval(() => {
			socket.emit('fetch', 'check')
		}, 1000)
	}
	componentWillUnmount() {
		clearInterval(this.updateInterval)
	}
	addMonitoringObject = object => {
		this.setState(state=>({monitor: [...state.monitor, object]}))
	}
	setObjectTime = object => {
		var idx = this.state.monitor.indexOf(this.state.monitor.find( obj => {
			return obj.name === object.name
		}))
		this.setState( state => {
			var monitor = state.monitor
			monitor.splice(idx, 1)
			return { monitor : [...monitor, object] }
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
