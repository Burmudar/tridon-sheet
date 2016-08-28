
////////////////////////////////
		//Setup//
////////////////////////////////

// Plugins
var gulp = require('gulp'),
      pjson = require('./package.json'),
      gutil = require('gulp-util'),
      sass = require('gulp-sass'),
      autoprefixer = require('gulp-autoprefixer'),
      cssnano = require('gulp-cssnano'),
      rename = require('gulp-rename'),
      del = require('del'),
      plumber = require('gulp-plumber'),
      pixrem = require('gulp-pixrem'),
      uglify = require('gulp-uglify'),
      imagemin = require('gulp-imagemin'),
      concat = require('gulp-concat'),
      exec = require('child_process').exec,
      runSequence = require('run-sequence'),
      browserSync = require('browser-sync').create(),
      mainBowerFiles = require('main-bower-files'),
      reload = browserSync.reload;


// Relative paths function
var pathsConfig = function (appName) {
  this.app = "./" + (appName || pjson.name);

  return {
    app: this.app,
    src: {
        css: this.app + '/frontend/styles',
        sass: this.app + '/frontend/styles',
        fonts: this.app + '/frontend/fonts',
        images: this.app + '/frontend/images',
        js: this.app + '/frontend/js',
        vendor: this.app + '/frontend/lib',
    },
    dst: {
        templates: this.app + '/templates',
        css: this.app + '/static/css',
        sass: this.app + '/static/sass',
        fonts: this.app + '/static/fonts',
        images: this.app + '/static/images',
        js: this.app + '/static/js',
    }
  }
};

var paths = pathsConfig();

////////////////////////////////
		//Tasks//
////////////////////////////////

gulp.task('fonts', function() {
    return gulp.src([paths.src.fonts + "/**/*", paths.src.vendor + "/font-awesome/fonts/**/*"])
        .pipe(gulp.dest(paths.dst.fonts));
});

// Styles autoprefixing and minification
gulp.task('styles', ['fonts'], function() {
  return gulp.src(mainBowerFiles({filter: "**/*.scss"}).concat([paths.src.sass + '/**/*.scss', paths.src.css + '/**/*.css']))
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(autoprefixer({browsers: ['last 2 version']})) // Adds vendor prefixes
    .pipe(pixrem())  // add fallbacks for rem units
    .pipe(concat("main.min.css"))
    .pipe(cssnano()) // Minifies the result
    .pipe(gulp.dest(paths.dst.css));
});

// Javascript minification
gulp.task('scripts', function() {
  return gulp.src([paths.src.js + '/**/*.js', mainBowerFiles({filter: "**/*.js"})])
    .pipe(plumber()) // Checks for errors
    .pipe(concat("main.min.js"))
    .pipe(uglify()) // Minifies the js
    .pipe(gulp.dest(paths.dst.js));
});

// Image compression
gulp.task('imgCompression', function(){
  return gulp.src(paths.src.images + '/*')
    .pipe(imagemin()) // Compresses PNG, JPEG, GIF and SVG images
    .pipe(gulp.dest(paths.dst.images))
});

// Run django server
gulp.task('runServer', function() {
  exec('python manage.py runserver', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });
});

// Browser sync server for live reload
gulp.task('browserSync', function() {
    browserSync.init(
      [paths.src.css + "/*.css", paths.src.js + "*.js", paths.dst.templates + '*.html'], {
        proxy:  "localhost:8000"
    });
});

// Default task
gulp.task('default', function() {
    runSequence(['styles', 'scripts', 'imgCompression'], 'runServer', 'browserSync');
});

////////////////////////////////
		//Watch//
////////////////////////////////

// Watch
gulp.task('watch', ['default'], function() {

  gulp.watch(paths.src.sass + '/*.scss', ['styles']);
  gulp.watch(paths.src.js + '/*.js', ['scripts']).on("change", reload);
  gulp.watch(paths.src.images + '/*', ['imgCompression']);
  gulp.watch(paths.dst.templates + '/**/*.html').on("change", reload);

});
