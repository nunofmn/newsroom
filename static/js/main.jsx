var Search = React.createClass({

    getInitialState: function() {
        return { searchString: '' };
    },

    handleChange:function(event) {
        this.setState({ searchString: event.target.value });
        console.log("Search updated!");
    },

    render: function() {
        return (
            <div>
                <div className="input-group stylish-input-group">
                    <input type="text" value={this.state.searchString} onChange={this.handleChange} className="form-control"  placeholder="Search">
                        <span className="input-group-addon">
                            <button type="submit">
                                <i className="fa fa-search"></i>
                            </button>
                        </span>
                    </input>
                </div>
                <p>Searched for: {this.state.searchString}</p>
            </div>
        )

    }

});

React.render(
    <Search />,
    document.getElementById('app-search')
);
