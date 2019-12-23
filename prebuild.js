var fs = require('fs');
var plist = require('plist');
const path = require('path');
let { config } = require('./config')

exports.preConfigProject = (projectDir) => {
    
    let projectName = config.projectName;
    //info.plist路径
    let infoPlistPath = path.resolve(projectDir, `./${projectName}/Info.plist`);
    var obj = plist.parse(fs.readFileSync(infoPlistPath, 'utf8'));
    let { CFBundleVersion, CFBundleShortVersionString, CFBundleDisplayName } = obj;
    //APP名字加上beta
    if (!CFBundleDisplayName.includes('beta')) {
        CFBundleDisplayName = `${CFBundleDisplayName}(Beta)`
        obj.CFBundleDisplayName = CFBundleDisplayName
    }
    //build自增
    CFBundleVersion = parseInt(CFBundleVersion) + 1;
    obj.CFBundleVersion = CFBundleVersion.toString()
    //version最后一位为日期， 1.0.1912231216
    let vers = CFBundleShortVersionString.split('.')
    if (vers && vers.length == 3) {
        let nt = new Date()
        let nowtime = nt.getFullYear().toString() + (nt.getMonth() + 1).toString() + nt.getDate().toString() + nt.getHours().toString() + nt.getMinutes();
        vers[2] = nowtime;
        obj.CFBundleShortVersionString = vers.join('.');
    }
    let rs = plist.build(obj)
    fs.writeFileSync(infoPlistPath, rs)
}
