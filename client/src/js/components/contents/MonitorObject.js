import React, { Component } from 'react'

export default class MonitorObject extends Component {
	state = {
		isObject: this.props.isObject || false
	}
	render() {
		var nameStyle = 'w-200 pd-20 mr-10 bold f4'
		if (this.state.isObject) nameStyle = nameStyle + ' bg-washed-blue'
		return(
			<div className='mr-0-100 fl-row align-center'>
				<h2 className={nameStyle}>{this.props.object.name}</h2>
				<h3 className='w-100 pd-20 light f5'>{this.props.object.time}</h3>
				<h3 className='w-100 pd-20 light f5'>{this.props.object.lat}</h3>
				<h3 className='w-100 pd-20 light f5'>{this.props.object.long}</h3>
			</div>
		)
	}
}
