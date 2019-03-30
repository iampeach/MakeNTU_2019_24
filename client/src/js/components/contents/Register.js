import React, { Component } from 'react'
import Webcam from 'react-webcam'

export default class Register extends Component {
	constructor(props) {
		super(props)
		this.ref = React.createRef()
	}
	render() {
		return (
			<div className='fl-col align-center'>
				<Webcam
					ref={ref => this.ref = ref}
					audio={false}
					width={500}
					height={375}
					screenshotFormat="image/jpeg"
				/>
				<div className='w-500 fl-row align-center'>
					<input 
						type='text'
						className='w-300 pd-10 mr-30 f4 fl-1-1'
						placeholder="What's your item name"
					/>
					<div className='w-30 fl-0-1 h-30 mr-30 bg-dark-red circle' />
				</div>
			</div>
		)
	}
}
