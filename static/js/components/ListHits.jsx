var React = require('react');
var HitItem = require('./HitItem.jsx');

var ListHits = React.createClass({

    getDefaultProps: function() {
        return {
            hits: [
                {
                    "highlights": "mecânica. Apresenta <b class=\"match term0\">queimaduras</b> nos pés e na",
                    "link": "http://feeds.jn.pt/~r/JN-PAIS/~3/CBbyAaH3gfs/concelho.aspx",
                    "summary": "A mulher de 50 anos que sofreu queimaduras \"em cerca de 90% do corpo\", na sequência de uma explosão numa habitação, em Paredes de Coura, morreu.",
                    "title": "Morreu mulher queimada na explosão em Paredes de Coura"
                },
                {
                    "highlights": "que a mulher \"sofreu <b class=\"match term0\">queimaduras</b> em cerca de",
                    "link": "http://feeds.jn.pt/~r/JN-PAIS/~3/c1pzSVdEWIw/concelho.aspx",
                    "summary": "Uma explosão ocorrida, esta sexta-feira de manhã, em Paredes de Coura, causou quatro feridos, dois dos quais em estado grave.",
                    "title": "Explosão em Paredes de Coura faz dois feridos graves"
                }
            ]
        };
    },


    render: function() {
        return (
            <ul>
                {this.props.hits.map(function(hit, index) {
                    return <HitItem key={index} data={hit}/>;
                })}
            </ul>
        )
    }

});

module.exports = ListHits;
