const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: ['./mysite/forum/static_files/js/index.js'],
    plugins: [
       
        new MiniCssExtractPlugin({filename: 'css/app.css',})
      ],
    module: {
        rules: [
            {
              test: /\.s?css$/i,
              use: [MiniCssExtractPlugin.loader,  "css-loader", 'sass-loader'],
            },
          ],
    },
    output: {
        path: path.join(__dirname, "static"),
        filename: 'js/bundle.js'  
   }
  }