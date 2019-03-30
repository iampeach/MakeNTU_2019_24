import React, { Component } from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './contents/Home'
import Monitor from './contents/Monitor'
import Register from './contents/Register'

export default class Content extends Component {
	state = {
		monitor:[
			{ name: 'obj_name', time: '' }
		]
	}
	componentDidMount() {
		this.addMonitoringObject('obj_name2')
		this.setObjectTime('obj_name', '00:00:00')
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
			monitor[idx] = { name: monitor[idx].name, time: time }
			return { monitor : monitor }
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
