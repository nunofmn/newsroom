var React = require('react');
var Search = require('./components/Search.jsx');
var HitList = require('./components/ListHits.jsx');
var request = require('superagent');

var App = React.createClass({

    getInitialState: function() {
        return (
            { data: [] }
        );
    },

    render: function() {
        return (
            <div>
                <Search onKeyDown={this.handleKeyDown} />
                <HitList data={this.state.data}/>
            </div>
        );
    },

    handleKeyDown: function(query, e) {
        if(e.keyCode === 13) {
            this._fetchData(query);
        }

    },

    _fetchData: function(query) {
        console.log("Getting data for: " + query);
        request
        .post('/search')
        .type('form')
        .send({ 'query': query })
        .end(this._applyData);
    },

    _applyData: function(err, res) {
        if(!err) {
            this.setState({ data: res.body.results });
            console.log(res.body.results);
        }else{
            console.log(err);
        }
    }
});


React.render(
    <App />,
    document.getElementById('app-search')
);
