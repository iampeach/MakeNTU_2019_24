import React, {Component} from 'react'
import Header from './components/Header'
import Content from './components/Content'
import { withRouter } from 'react-router'

class App extends Component {
	state = {
		contents: [
			{ url: '/', text: 'Home' },
			{ url: '/monitor', text: 'Monitor' },
			//{ url: '/register', text: 'Register' },
		]
	}
	changePage = id => {
		this.props.history.push(this.state.contents[id].url)
	}
	render() {
		return (
			<div className='mg-0 pd-0 fl-col'>
				<Header changePage={this.changePage} contents={this.state.contents}/>
				<Content />
			</div>
		)
	}
}

export default withRouter(App)
