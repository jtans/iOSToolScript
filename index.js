/**
 * 使用方法Xcode run script
 * cd xxx(脚本目录)
 * usr/local/bin/npm install
 * usr/local/bin/npm index.js $PROJECT_SRC
 */
const process = require('process');
//工程目录
let projectDir = process.argv[2];

let { preConfigProject } = require('./prebuild')
preConfigProject(projectDir)