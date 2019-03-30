import React, { Component } from 'react'

export default class Header extends Component {
	changePage = id => {
		this.props.changePage(id)
	}
	render() {
		var caption_style = 'grey light up-mr-10 d-mr-10 pd-20 fl-0-1 f4 cursor-point'
		var captions = this.props.contents.map((content, idx) => 
			<h2 className={caption_style} 
					onClick={()=>this.changePage(idx)}
					key={idx}>
						{content.text}
			</h2>
		)
		return (
			<div className='mr-0 d-mr-50 pd-0 fl-row fl-end font-pri'>
				{captions}
			</div>
		)
	}
}
