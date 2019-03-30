import React, { Component } from 'react'
import MonitorObject from './MonitorObject'

export default class Monitor extends Component {
	render() {
		var objects = this.props.objects.map((obj, idx)=>
			<MonitorObject object={obj} isObject={true} key={idx}/>
		)
		return (
			<div className='fl-col align-center'>
				<MonitorObject object={{name: 'Monitoring Object', time: 'Time'}}/>
				<hr className='w-700 mr-0 d-mr-30 grey b-solid' />
				{objects}
			</div>
		)
	}
}
