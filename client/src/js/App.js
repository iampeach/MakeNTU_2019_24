import React, {Component} from 'react'
import Header from './components/Header'
import Content from './components/Content'

class App extends Component {
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
