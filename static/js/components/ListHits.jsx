var React = require('react');
var HitItem = require('./HitItem.jsx');

var ListHits = React.createClass({

    getDefaultProps: function() {
        return {
            data: []
        };
    },

    render: function() {
        return (
            <ul>
                {this.props.data.map(function(hit, index) {
                    return <HitItem key={index} item={hit}/>;
                })}
            </ul>
        );
    }

});

module.exports = ListHits;
