const path = require('path');

module.exports = {
  entry: "./src/index.js",
  module: {
    rules: [
     {
      test: /\.js$/,
      exclude: /node_modules/,
      loader: "babel-loader",
      options: { presets: ["@babel/env"] }
     },
     {
      test: /\.tsx$/,
      exclude: /node_modules/,
      loader: "babel-loader",
      options: { presets: ["@babel/preset-typescript"] }
     }
    ]
  },
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "editor-bundle.js"
  }
};
