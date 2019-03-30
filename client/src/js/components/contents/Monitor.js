import React, { Component } from 'react'
import MonitorObject from './MonitorObject'

export default class Monitor extends Component {
	render() {
		var objects = []
		for (let i = this.props.objects.length-1; i >= 0; --i){
			objects.push(<MonitorObject object={this.props.objects[i]} isObject={true} key={i}/>)
		}
		return (
			<div className='fl-col align-center'>
				<MonitorObject object={{name: 'Monitoring Object', time: 'Time'}}/>
				<hr className='w-700 mr-0 d-mr-30 grey b-solid' />
				{objects}
			</div>
		)
	}
}
