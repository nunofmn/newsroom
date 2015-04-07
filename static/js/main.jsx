var React = require('react');
var Search = require('./components/Search.jsx');
var HitList = require('./components/ListHits.jsx');

React.render(
    <div>
        <Search />
        <HitList />
    </div>,
    document.getElementById('app-search')
);
