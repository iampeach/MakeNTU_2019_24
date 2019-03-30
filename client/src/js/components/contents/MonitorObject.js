import React, { Component } from 'react'

export default class MonitorObject extends Component {
	state = {
		isObject: this.props.isObject || false
	}
	map = _ => {
		if (this.state.isObject)
			window.open('https://www.google.com/maps/place/'+this.props.object.lat+this.props.object.long)
	}
	render() {
		var nameStyle = 'w-300 pd-20 mr-10 bold'
		if (this.state.isObject) nameStyle = nameStyle + ' bg-washed-blue cursor-point'
		return(
			<div className='mr-0-100 fl-row align-center'>
				<h2 className={nameStyle} onClick={()=>this.map()}>{this.props.object.name}</h2>
				<h3 className='w-300 pd-20 light'>{this.props.object.time}</h3>
			</div>
		)
	}
}
