'use strict';

var gulp = require('gulp');
var browserify = require('gulp-browserify');
var size = require('gulp-size');
var clean = require('gulp-clean');

gulp.task('transform', function() {
    return gulp.src('./static/js/main.jsx')
    .pipe(browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./static/dist'))
    .pipe(size());
});

gulp.task('clean', function() {
    return gulp.src(['./static/dist'], {read: false})
    .pipe(clean());
});

gulp.task('watch', function() {
    gulp.start('transform');
    gulp.watch('./static/js/**/*.*');
});

gulp.task('default', ['transform'], function() {});

