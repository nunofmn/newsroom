var React = require('react')
var Search = React.createClass({

    getInitialState: function() {
        return { searchString: '' };
    },

    handleChange:function(event) {
        this.setState({ searchString: event.target.value });
    },

    render: function() {
        return (
            <div>
                <div className="input-group stylish-input-group">
                    <input type="text" value={this.state.searchString} onChange={this.handleChange} onKeyDown={this.props.onKeyDown.bind(null, this.state.searchString)} className="form-control"  placeholder="Search">
                        <span className="input-group-addon">
                            <button type="submit">
                                <i className="fa fa-search"></i>
                            </button>
                        </span>
                    </input>
                </div>
                <p className={this.state.searchString === '' ? 'search-info hide' : 'search-info' }>Searched for: {this.state.searchString}</p>
            </div>
        );

    }
});

module.exports = Search;
