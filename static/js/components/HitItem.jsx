var React = require('react');

var HitItem = React.createClass({
    render: function() {
        return (
            <li>
                <div>
                    <h3>{this.props.data.title}</h3>
                    <p>{this.props.data.highlights}</p>
                    <a href={this.props.data.link}>{this.props.data.link}</a>
                </div>
            </li>
        );
    }
});

module.exports = HitItem;
