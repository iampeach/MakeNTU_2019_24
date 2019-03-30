import React, { Component } from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './contents/Home'
import Edit from './contents/Edit'

export default class Content extends Component {
	render() {
		return(
			<div>
				<Switch>
					<Route exact path='/' render={() => <Home />} />
					<Route path='/edit' render={() => <Edit />} />
				</Switch>
			</div>
		)
	}
}
