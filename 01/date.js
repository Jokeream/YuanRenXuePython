// 使用 require 导入 atob.js 中的函数
const { hex_md5 } = require('./atob.js');

// 获取当前时间并添加偏移量
function generate_m() {
    var _0x2268f9 = Date.parse(new Date()) + 100000000;

    // 调用 hex_md5 函数并传入字符串
    var _0x57feae = hex_md5(_0x2268f9.toString());

    // 返回最终生成的值
    return _0x57feae + '丨' + (_0x2268f9 / 1000);
}

// 将函数导出，使其可以在 Python 中调用
module.exports = {
    generate_m
};
