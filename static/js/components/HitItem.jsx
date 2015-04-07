var React = require('react');

var HitItem = React.createClass({
    render: function() {
        return (
            <li className="hit-item">
                <div>
                    <h3>{this.props.item.title}</h3>
                    <p className="highlights" dangerouslySetInnerHTML={{__html: this.props.item.highlights}}/>
                    <a href={this.props.item.link}>{this.props.item.link}</a>
                </div>
            </li>
        );
    }
});

module.exports = HitItem;
