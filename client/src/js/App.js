import React, {Component} from 'react'
import Header from './components/Header'
import Content from './components/Content'

class App extends Component {
	constructor(props) {
		super(props)
		this.state = {
			curPage: 0,
			contents: [
				{ url: '/' },
				{ url: '/edit' } 
			]
		}
	}
	render() {
		return (
			<div className='mg-0 pd-0 fl-col'>
				<Header />
				<Content />
			</div>
		)
	}
}

export default App
