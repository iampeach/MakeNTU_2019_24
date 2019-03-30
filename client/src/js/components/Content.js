import React, { Component } from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './contents/Home'
import Monitor from './contents/Monitor'
import Register from './contents/Register'

export default class Content extends Component {
	render() {
		return(
			<div>
				<Switch>
					<Route exact path='/' render={() => <Home />} />
					<Route path='/monitor' render={() => <Monitor />} />
					<Route path='/register' render={() => <Register />} />
				</Switch>
			</div>
		)
	}
}
